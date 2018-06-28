from flask_caching import Cache

from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def init_ext(app):
    init_db(app)
    init_mail(app)
    init_cache_config(app)


db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    db.init_app(app=app)
    migrate.init_app(app, db)


mail = Mail()


def init_mail(app):
    mail.init_app(app)


# 配置缓存
'''
安装
1>flask-caching
2>redis
配置
'''

cache = Cache(config={'CACHE_TYPE': 'redis',
                      })
def init_cache_config(app):
    cache.init_app(app)
