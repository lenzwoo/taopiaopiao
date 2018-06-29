import datetime

from app.ext import db


class Area(db.Model):
    area_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    parent_id = db.Column(db.Integer, index=True)
    pingyin = db.Column(db.String(100), nullable=False, index=True)
    key = db.Column(db.String(10))
    is_hot = db.Column(db.Boolean, default=False)


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


