from flask import Blueprint, request, jsonify

from app.cinema.models import Cinemas

from app.utils.json_utils import to_list

cinema_blue = Blueprint('cinema_blue', __name__)


@cinema_blue.route('/list/')
def cinema():
    result = {}
    try:
        page = request.values.get('page', default=1, type=int)
        size = request.values.get('size', default=10, type=int)
        dist = request.values.get('dist')
        sort = request.values.get('sort', default=0, type=int)
        city = request.values.get('city')
        # 影院查找索索栏数据
        keyword = request.values.get('keyword')
        if city:
            query = Cinemas.query.filter(Cinemas.city == city)
            if dist:
                query = query.filter(Cinemas.district == dist)

            if keyword:
                query = query.filter(Cinemas.name.like('%' + keyword + '%'))
            if sort:
                if sort == 1:
                    query = query.order_by(Cinemas.score.desc())
                else:
                    # 降序 排列
                    query = query.order_by(Cinemas.score)

            pagination = query.paginate(page=page, per_page=size, error_out=False)
            result.update(status=200, msg='success', cinemas=to_list(pagination.items))
        else:
            result.update(status=-1, msg='no param city')
    except Exception as e:
        result.update(status=404, msg='fail')
    return jsonify(result)
