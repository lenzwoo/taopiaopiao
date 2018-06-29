from app.ext import ma
from app.home.models import Movies


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movies


movie_schema = MovieSchema
movies_schema = MovieSchema(many=True)
