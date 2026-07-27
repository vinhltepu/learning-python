from datetime import datetime, timedelta, timezone
import jwt
from app.core.security import hash_password , verify_password
# khóa dùng để mã hóa và giải mã jwwt
SECRET_KEY = "quangthuy-secret-key"

# thuật toán mã hóa Token
ALGORITHM = "HS256"

# thời gian sống của Access Token (30 phút)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# thời gian sống của Refresh Token (7 ngày)
REFRESH_TOKEN_EXPIRE_DAYS = 7


# mã hóa mật khẩu trước khi lưu vào database
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# tạo access token để xác thực người dùng khi truy cập API. Access token có thời gian sống ngắn hơn refresh token.
def create_access_token(data: dict):


    # sao chép dữ liệu truyền vào
    payload = data.copy()

    # thời gian hết hạn
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # thêm thời gian hết hạn vào Token
    payload["exp"] = expire

    # trả về chuỗi JWT
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# tạo refresh token để làm mới access token khi access token hết hạn. Refresh token có thời gian sống dài hơn access token.
def create_refresh_token(data: dict):

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        days=REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload["exp"] = expire

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )



# kiểm tra và giải mã JWT. Nếu Token hợp lệ sẽ trả về dữ liệu. Nếu Token sai hoặc hết hạn sẽ trả về None.
def decode_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None

# mã hóa mật khẩu
def hash_password(password: str):

    return pwd_context.hash(password)


# kiểm tra mật khẩu
def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )