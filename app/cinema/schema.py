from app.cinema.models import Cinemas
from app.ext import ma



class CinemaSchema(ma.ModelSchema):
    class Meta:
        model = Cinemas


cinema_schema = CinemaSchema
cinemas_schema = CinemaSchema(many=True)
