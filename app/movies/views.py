from flask import Blueprint, request, jsonify

from app.cinema.models import Cinemas, HallSchedule
from app.ext import db
from app.home.models import Movies
from app.movies.schema import movies_schema
from app.utils.json_utils import to_dict, to_list

movies_blue = Blueprint('moives', __name__)


@movies_blue.route('/list/')
def movie():
    result = {}
    try:
        flag = request.values.get('flag', default=1, type=int)
        # 分页参数
        page = request.values.get('page', default=1, type=int)
        size = request.values.get('size', default=10, type=int)
        # 分页查询数据
        paginate = Movies.query.filter(Movies.flag == flag).paginate(page=page, per_page=size, error_out=False)
        # 封装前端界面需要的数据
        pagination = {'total': paginate.total, 'pages': paginate.pages}
        movies = movies_schema.dump(paginate.items)
        # 组装返回的数据
        result.update(status=200, msg='success', data=movies.data, paginate=pagination)
    except:
        result.update(status=200, msg='fail')
    return jsonify(result)


# 显示电影的详细信息
# 必要参数 城市名称  电影的id
@movies_blue.route('/detail/')
def show_detail():
    result = {}
    try:
        # 获取提交过来的电影id
        mid = request.values.get('mid', type=int)
        # 获取提交过来的城市名称
        city = request.values.get('city')
        # 获取影片详情信息（要显示的字段）
        movie = db.session.Query(Movies.id, Movies.backgroundpicture, Movies.director).get(mid)
        # 查询地区的相关信息
        districts = Cinemas.query.with_entities(Cinemas.district).filter(Cinemas.city == city).all()
        # 查询区域的影城信息
        cinemas = Cinemas.query.order_by(Cinemas.id).filter(Cinemas.city == city).all()
        hall_schedule = HallSchedule.query.filter(HallSchedule.cid == Cinemas[0].id).filter(
            HallSchedule.movie_id == mid).all()
        result.update(status=200, msg='success', movie=to_dict(movie), districts=to_list(districts),
                      cinemas=to_list(cinemas), hall_schedule=to_list(hall_schedule))
    except Exception as e:
        result.update(status=404, msg='fail')
    return jsonify(result)
