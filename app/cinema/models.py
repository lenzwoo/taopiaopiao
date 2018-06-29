from app.ext import db


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


class Hall(db.Model):
    hid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer, db.ForeignKey('cinemas.id'))
    name = db.Column(db.String(100), index=True, unique=True, nullable=True)
    # 座位数
    seats = db.Column(db.Integer, default=0)
    # 影厅的状态  1.未放映   2.正在放映
    status = db.Column(db.String(64), default=1)
    is_delete = db.Column(db.Boolean, default=False)


# 影厅档期
class HallSchedule(db.Model):
    hs_id = db.Column(db.Integer, primary_key=True)
    original_price = db.Column(db.Numeric(10, 2))
    dis_price = db.Column(db.Numeric(10, 2))
    start_time = db.Column(db.DateTime)
    # 1未开始   2 正在放映
    status = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)
    # 关联影院外键
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    hid = db.Column(db.Integer, db.ForeignKey('hall.hid'))
    cid = db.Column(db.Integer, db.ForeignKey('cinemas.id'))
