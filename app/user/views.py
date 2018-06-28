import json

from flask import Blueprint, request, jsonify, render_template
from flask_mail import Message

from app.ext import db, mail, cache
from app.home.models import Area
from app.user.models import User
from app.utils.redis_utils import get_redis

user = Blueprint('user', __name__)


@user.route('/login/')
def login():
    pass


@user.route('/reg/', methods=['POST', 'GET'])
def register():
    result = {}
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        email = request.values.get('email')
        if username and password and email:
            user = User.query.filter(User.username == username or User.email == email).all()
            # user = User.query.withenties(username=username)
            if user:
                result.update(msg='账号或邮箱已存在！！', status=-2)
            else:
                user = User(username=username, password=password, email=email)
                db.session.add(user)
                db.session.commit()
            msg = Message('激活邮件',
                          body='用户您好',
                          sender='wuguyeshu@163.com',
                          recipients=[email],
                          )
            get_redis().set('username', username, ex=10 * 60)
            mail.send(msg)
            result.update(msg='邮件已发送', status=1)
        else:
            result.update(msg='必要参数不能为空！！！', status=-1)
    else:
        result.update(msg='错误的请求方式！！！', status=400)
    return jsonify(result)


@user.route('/activate/')
def activate_account():
    result = {}
    username = request.values.get('username')
    res = get_redis.get('username')
    if username == res:
        user = User.query.filter(User.username == username).first()
        if user:
            user.is_active = True
            db.session.update(user)
            db.session.commit()
            result.update(status=200, msg='激活成功')
        else:
            result.update(status=-3, msg='用户不存在！')
    else:
        result.update(status=-4, msg='激活链接已失效，请重新激活')
    return jsonify(result)


@user.route('/1/', methods=['POST', 'GET'])
def test_send():
    msg = Message('激活邮件',
                  body='用户您好',
                  html="<a href=''>激活</a>",
                  sender='wuguyeshu@163.com',
                  recipients=['wuguyeshu@163.com']
                  )
    mail.send(msg)
    return '请激活'


# @user.route('/add/')
# def add_json_data():
#     keys = 'ABDEFGHIJKLMNOPQRSTUVWXYZ'
#     with open(r'D:\Projects\taopiaopiao\app\json\area.json', 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         obj = data.get('returnValue')
#         for key in keys:
#             cities = obj.get(key)
#             for city in cities:
#                 db.session.add(Area(name=city.get('regionName'),
#                                     pingyin=city.get('pinYin'),
#                                     parent_id=city.get('parentId'),
#                                     area_id=city.get('cityCode'),
#                                     key=key,
#                                     ))
#                 db.session.commit()
#     return 'success~~~~~'


@user.route('/test/')
def test():
    return '1111111test'
