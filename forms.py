from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired 

class Buttons(FlaskForm):
	random = SubmitField('Random Haiku')
	word = StringField('Write a Word', validators = [DataRequired()])
	submit = SubmitField("Let's Go")

