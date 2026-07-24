FAST-API-GROCERY/
├── main.py                         → Khởi tạo app, đăng ký router, tạo DB
├── requirements.txt
└── app/
    ├── core/config.py              → Cấu hình tên app, database URI
    ├── db/
    │   ├── base.py                 → Base + đăng ký models
    │   └── session.py              → Engine + SessionLocal
    ├── models/
    │   ├── product.py              → Product → PaintingProduct, WoodProduct (STI)
    │   ├── customer.py             → Customer → RegularCustomer, VIPCustomer (STI)
    │   └── invoice.py              → Invoice + InvoiceDetail
    ├── schemas/
    │   ├── product.py              → Validate input/output sản phẩm
    │   ├── customer.py             → Validate input/output khách hàng
    │   └── invoice.py              → Validate input/output hóa đơn
    └── api/
        ├── deps.py                 → get_db()
        └── endpoints/
            ├── products.py         → CRUD + filter sản phẩm
            ├── customers.py        → CRUD + tìm kiếm khách hàng
            ├── invoices.py         → Tạo hóa đơn, trừ kho, tích điểm
            └── stats.py            → Thống kê tồn kho, doanh thu, top KH


## 1. JWT là gì?

- JWT (JSON Web Token) là một chuẩn mở (open standard) được dùng rất phổ biến trong lập trình web hiện đại, đặc biệt là khi xây dựng REST API. Về bản chất, JWT là một chuỗi ký tự được server sinh ra, dùng để:

1. Xác thực (Authentication) — chứng minh "bạn là ai" mà không cần phải gửi lại Username/Password ở mỗi request.

2. Truyền thông tin an toàn giữa Client và Server — nhờ có chữ ký (Signature), dữ liệu bên trong token khó bị giả mạo hoặc chỉnh sửa mà không bị phát hiện.
### Cơ chế "Stateless" (không trạng thái)

Đây là điểm cốt lõi giúp JWT khác với cách xác thực cũ (session):

- Server không lưu trạng thái đăng nhập của bất kỳ ai trong bộ nhớ.
- Toàn bộ thông tin cần thiết để xác thực nằm gọn trong chính chuỗi JWT.
- Client tự lưu JWT và tự gửi lên mỗi khi cần.

## Luồng hoạt động tổng quát 
Đăng nhập
   ↓
Server kiểm tra tài khoản (đúng)
   ↓
Sinh JWT
   ↓
Trả JWT về Client
   ↓
Client lưu JWT (Cookie / LocalStorage)
   ↓
Các lần sau: gửi JWT kèm theo Request
   ↓
Server kiểm tra JWT hợp lệ
   ↓
Cho phép truy cập


## 2. Cấu trúc của JWT

Một JWT gồm 3 phần, nối với nhau bằng dấu chấm:

- Header.Payload.Signature
- xxxxx.yyyyy.zzzzz


### 2.1. Header

Chứa thông tin về thuật toán mã hóa được dùng.

{
  "alg": "HS256",
  "typ": "JWT"
}


### 2.2. Payload

Chứa thông tin của người dùng — đây là dữ liệu server muốn gửi đi.

{
  "user_id": 1,
  "username": "admin",
  "role": "admin"
}

# Lưu ý : Payload chỉ được mã hóa Base64, không phải mã hóa bảo mật — ai cũng decode đọc được nội dung bên trong không dược lưu trong Payload :

- Mật khẩu (Password)
- Thông tin ngân hàng
- CCCD / số định danh cá nhân
- Bất kỳ dữ liệu nhạy cảm nào khác


### 2.3. Signature (chữ ký)

Server dùng 3 thứ để tạo ra Signature:

- Header
- Payload
- Secret Key (khóa bí mật, chỉ server biết)


HMACSHA256(
  Header + Payload + SecretKey
)


Nếu ai đó cố tình sửa Payload (ví dụ đổi `role` từ `staff` thành `admin`), Signature sẽ sai lệch ngay lập tức và bị server từ chối.


## 3. JWT hoạt động như thế nào?

Bước 1 Người dùng nhập Username + Password → Server kiểm tra Database |
Bước 2 Nếu đúng → Server sinh JWT (chứa id, role...) → trả về Client |
Bước 3 Client lưu JWT (Cookie / LocalStorage / SessionStorage) |
Bước 4 Mỗi lần gọi API, Client gửi kèm header: `Authorization: Bearer <JWT>` |
Bước 5 Server kiểm tra Signature, hạn dùng, tính hợp lệ → cho phép hoặc trả về `401 Unauthorized` |

## 4. Ưu điểm của JWT

- Không cần lưu Session trên Server → giảm tải bộ nhớ máy chủ.

- Dễ mở rộng, dùng chung nhiều nền tảng → Website, Mobile App, Desktop App đều có thể xài chung một cơ chế xác thực.

- Tốc độ nhanh → chỉ cần gửi Token, không phải truy vấn Session nhiều lần.

- Phù hợp với REST API→ cách xác thực phổ biến nhất hiện nay.

- Có chữ ký (Signature) → nếu bị sửa nội dung, server phát hiện được ngay.

## 5. Nhược điểm của JWT

- Nếu JWT bị đánh cắp → hacker có thể giả mạo người dùng cho đến khi token hết hạn (không giống session, không thể "xóa" token đã phát hành khỏi server).

- Khó thu hồi Token → muốn thu hồi phải dùng Blacklist, Refresh Token, hoặc đổi Secret Key.

- Token quá lớn nếu lưu nhiều thông tin trong Payload → request nặng hơn, giảm hiệu suất → chỉ nên lưu thông tin cần thiết.

- Không nên lưu dữ liệu nhạy cảm (Password, số tài khoản, CCCD...) vì Payload có thể đọc được.


## 6. Refresh Token là gì?

- Refresh Token là một loại token đặc biệt, đi kèm với Access Token, nhưng có mục đích và vòng đời khác hẳn. Trong khi Access Token dùng để "mở khóa" và gọi các API mỗi ngày, thì Refresh Token chỉ có một nhiệm vụ duy nhất: khi Access Token hết hạn, Client sẽ dùng Refresh Token để xin server cấp một Access Token mới, mà không cần người dùng phải nhập lại Username/Password.

## 7. Vì sao cần Refresh Token?

- Nếu để Access Token sống quá lâu (ví dụ 30 ngày), khi bị hacker lấy được, hacker có thể dùng trong suốt 30 ngày đó → rất nguy hiểm.

Giải pháp
- Access Token chỉ sống ngắn (ví dụ 15 phút) rồi hết hạn.
- Khi hết hạn, dùng Refresh Token để xin cấp Access Token mới, mà không cần đăng nhập lại.

## 8. Cơ chế hoạt động của Refresh Token

Người dùng đăng nhập
   ↓
Server tạo: Access Token + Refresh Token
   ↓
Client lưu cả hai
   ↓
Sau 15 phút, Access Token hết hạn
   ↓
Client gửi Refresh Token lên Server
   ↓
Server kiểm tra Refresh Token hợp lệ
   ↓
Sinh Access Token mới
   ↓
Client tiếp tục sử dụng (không cần đăng nhập lại)


## 13. JWT được dùng trong dự án như thế nào?

Trong dự án quản lý cửa hàng Quang Thúy, JWT được sử dụng cho:

1. Đăng nhập (Login): Server kiểm tra tài khoản, trả về Access Token + Refresh Token.
2. Xác thực (Authentication): Mỗi request lên API phải kèm `Authorization: Bearer <token>`.
3. Phân quyền (Authorization): Server đọc `role` trong JWT để quyết định người dùng được làm gì (Admin / Quản lý / Nhân viên).
4. Làm mới phiên đăng nhập: Khi Access Token hết hạn, Client dùng Refresh Token để xin Access Token mới, không cần đăng nhập lại.
5. Đăng xuất (Logout): Xóa token phía Client, thu hồi Refresh Token phía Server (nếu có lưu).


