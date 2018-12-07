# Flask-WTF Forms
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# forms

class CompanySearch(FlaskForm):
    """
    This sets up the input field of the app
    """
    symbol = StringField('symbol', validators=[DataRequired()])
