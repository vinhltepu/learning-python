from flask import Blueprint

admin_bp = Blueprint('admins', __name__)

@admin_bp.route('/admins')
def admins():
    return '<h1>Đây là trang admins</h1>'