from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField


class SearchForm(FlaskForm):
    text = StringField('Text')
    cities = SelectMultipleField("list", choices=[
        ("1", "item_1"),
        ("2", "item_2")
    ])
    subm = SubmitField("submit")
    but = SubmitField("Button")