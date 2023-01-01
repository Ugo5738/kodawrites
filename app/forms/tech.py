from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField("Article Title:")#, validators=[DataRequired()])
    keywords = StringField("Article Keywords:")
    submit = SubmitField("Write")