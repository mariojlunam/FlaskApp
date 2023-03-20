from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional


class BboxForm(FlaskForm):

    x1 = FloatField("Lon Point 1", validators=[DataRequired()])
    y1 = FloatField("Lat Point 1", validators=[DataRequired()])
    x2 = FloatField("Lon Point 2", validators=[DataRequired()])
    y2 = FloatField("Lat Point 2", validators=[DataRequired()])
    srid = IntegerField("srid", validators=[Optional()])
    submit = SubmitField("Submit")
