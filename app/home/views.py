from flask import Blueprint, jsonify
from sqlalchemy import func

from app.home.models import Area, Movies
from app.utils.json_utils import to_list

home = Blueprint('home', __name__)

keys = 'ABDEFGHIJKLMNOPQRSTUVWXYZ'


@home.route('/areas/')
def get_ares():
    result = {}
    ares = {}
    try:
        for key in keys:
            area_list = Area.query.filter(Area.key == key).all()
            if area_list:
                ares[key] = to_list(area_list)
        result.update(msg='success', status=200, ares=ares)
    except Exception as e:
        result.update(msg='查询失败', status=404)
    return jsonify(result)


@home.route('/moves/', methods=['POST', 'GET'])
def movies():
    result = {}
    try:
        movie = {}
        # 分组查询热门影片和热映影片数量
        counts = Movies.query.with_entities(Movies.flag, func.count('*')).group_by(Movies.flag).all()
        # 查询热门影片的前5部
        hot_movies = Movies.qeury.filter(Movies.flag == 1).limit(5).all()
        # 查询即将上映影片的前5部
        show_movies = Movies.query.filter(Movies.flag == 2).limit(5).all()
        movie.update(counts=counts, hot_movies=to_list(hot_movies), show_movies=to_list(show_movies))
        result.update(status=200, msg='success~~', data=movie)
    except:
        result.update(status=400, msg='查询失败~~', )
    return jsonify(result)










