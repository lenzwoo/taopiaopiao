import datetime

from app.ext import db


class Area(db.Model):
    area_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    parent_id = db.Column(db.Integer, index=True)
    pingyin = db.Column(db.String(100), nullable=False, index=True)
    key = db.Column(db.String(10))
    is_hot = db.Column(db.Boolean, default=False)


#
# class Cinemas(db.Model):
#     __tablename__ = 'cinemas'
#     cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(255), index=True, nullable=True)
#     city = db.Column(db.String(255), index=True)
#     district = db.Column(db.String(255))
#     address = db.Column(db.String(255))
#     phone = db.Column(db.String(255))
#     score = db.Column(db.Float)
#     hallnum = db.Column(db.Integer)
#     servicecharge = db.Column(db.Float)
#     astrict = db.Column(db.Integer)
#     flag = db.Column(db.Boolean, default=True)
#     isdelete = db.Column(db.Boolean, default=False)
#
#
# class Movies(db.Model):
#     __tablename__ = 'movies'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     showname = db.Column(db.String(255), index=True)
#     shownameen = db.Column(db.String(255))
#     director = db.Column(db.String(255))
#     leadingRole = db.Column(db.String(255))
#     type = db.Column(db.String(255))
#     country = db.Column(db.String(255))
#     language = db.Column(db.String(255))
#     duration = db.Column(db.Integer)
#     creeningmodel = db.Column(db.String(255))
#     openday = db.Column(db.DateTime, default=datetime.datetime.now())
#     backgroundpicture = db.Column(db.String(255))
#     flag = db.Column(db.Boolean, default=True)
#     isdelete = db.Column(db.Boolean, default=False)


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    showname = db.Column(db.String(100))  # 中文名
    shownameen = db.Column(db.String(200))  # 英文名
    director = db.Column(db.String(100))  # 导演
    leadingRole = db.Column(db.String(300))  # 主演
    type = db.Column(db.String(50))  # 类型
    country = db.Column(db.String(100))  # 国家
    language = db.Column(db.String(50))  # 语言
    duration = db.Column(db.Integer)  # 电影时长
    screeningmodel = db.Column(db.String(20))  # 放映模式(2D 3D 4D),可以使用枚举
    openday = db.Column(db.DateTime)  # 上映时间
    backgroundpicture = db.Column(db.String(100))  # 背景图片
    flag = db.Column(db.Integer)  # 状态(热映 即将上映)
    isdelete = db.Column(db.Boolean, default=False)  # 是否删除,默认未删除


class Cinemas(db.Model):
    __tablename__ = 'cinemas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))  # 影院名
    city = db.Column(db.String(50))  # 所在城市
    district = db.Column(db.String(50))  # 区域
    address = db.Column(db.String(200))  # 地址
    phone = db.Column(db.String(20))  # 电话
    score = db.Column(db.Float)  # 评分
    hallnum = db.Column(db.Integer)  # 影厅数量
    servicecharge = db.Column(db.Float)  # 服务费
    astrict = db.Column(db.Integer)  # 限购数量
    flag = db.Column(db.Integer)  # 状态(营业1，休息0)
    isdelete = db.Column(db.Boolean, default=False)  # 是否删除
