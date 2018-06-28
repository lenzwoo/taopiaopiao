import redis

Host = '127.0.0.1'
PORT = 6379
DB = 0

pool = None
rds = redis.ConnectionPool(host=Host, port=PORT, db=DB)


# 或者直接链接
# rds = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

def get_redis():
    return redis.Redis(connection_pool=rds)
