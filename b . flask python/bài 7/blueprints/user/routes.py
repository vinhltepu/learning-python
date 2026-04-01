from flask import Flask, blueprints

user_bp = blueprints.Blueprint('user', __name__)

user_bp.route('/users')
def user():
    return '<h1>Đây là trang user</h1>' 