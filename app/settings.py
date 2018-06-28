class Config():
    DEBUG = False
    SECRET_KEY = '451345134132'


def get_db_uri(database: dict):
    user = database.get('USER') or 'root'
    password = database.get('PASSWORD') or '123456'
    host = database.get('HOST') or '127.0.0.1'
    port = database.get('PORT') or '3306'
    name = database.get('NAME')
    db = database.get('DB') or 'mysql'
    driver = database.get('DRIVER') or 'pymysql'
    charset = database.get('CHARSET') or 'utf8'
    return '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(db, driver, user, password, host, port, name, charset)


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'NAME': 'tpp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'wuguyeshu@163.com'
    MAIL_PASSWORD = 'qq123456'


class ProductConfig(Config):
    DEBUG = True
    DATABASE = {
        'DB': 'mysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'tpp',
        'DRIVER': 'pymysql',
        'CHARSET': 'utf8',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


env = {
    # 开发环境
    'dev': DevelopConfig,
    # 生产环境
    'pro': ProductConfig,
}
