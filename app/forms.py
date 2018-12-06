# Flask-WTF Forms
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# forms

class StockSearchForm(FlaskForm):
    """
    This sets up the input field of the app
    """
    stock_name = StringField('name', validators=[DataRequired()])
