from flask import request, session
from flask_restx import Resource, Namespace, fields
from flask_login import login_required, login_user, logout_user
from app import login_manager
from models import *
from flask_bcrypt import Bcrypt

UserManagement = Namespace(
    name='UserManagement',
    description="사용자 관련한 로그인, 회원 가입 등 API",
)
bcrypt = Bcrypt()
login_fields = UserManagement.model('Login', {
    'login_id': fields.String(description="id", example="elice"),
    'login_pw': fields.String(description="pw", example="1234")
})
register_fields = UserManagement.model('Register', {
    'id': fields.String(description="id", example="elice"),
    'pw': fields.String(description="pw", example="1234"),
    'pw2': fields.String(description="pw2", example="1234")
})


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()


@UserManagement.route('/login')
class Login(Resource):
    @UserManagement.expect(login_fields)
    @UserManagement.response(200, 'success')
    @UserManagement.response(202, 'already_exists')
    @UserManagement.response(500, 'fail')
    def post(self):
        user_id = request.json.get('login_id')
        user_pw = request.json.get('login_pw')

        user_data = User.query.filter(User.id == user_id).first()
        if not user_data:
            # 아이디 틀림
            return {'result': 'login_error'}, 500
        elif not bcrypt.check_password_hash(user_data.pw, user_pw):
            # 비밀번호 틀림
            return {'result': 'login_error'}, 500
        else:
            login_user(user_data)
            # 로그인 진행
            return {'result': 'success'}


@UserManagement.route('/logout')
class Logout(Resource):
    @login_required
    def get(self):
        """로그인 되어있는 경우에 로그아웃하고 메인 페이지로 돌아가기"""
        session.clear()
        logout_user()
        return {'result': 'success'}, 200


@UserManagement.route('/register')
class Register(Resource):
    @UserManagement.expect(register_fields)
    @UserManagement.response(200, 'success')
    @UserManagement.response(500, 'fail')
    def post(self):
        user_data = User.query.filter(User.id == request.json.get('id')).first()
        if not user_data:
            if not request.json.get('pw')==request.json.get('pw2'):
                #비밀번호 불일치
                return {'result': 'unmatched_pw'}, 500
            user_id = request.json.get('id')
            pw_hash = bcrypt.generate_password_hash(request.json.get('pw'))
            user = User(user_id, pw_hash, None)
            db.session.add(user)
            db.session.commit()
            #회원가입 성공
            return {'result': 'success'}, 200
        else:
            return {'result': 'id_already_exists'}, 202
