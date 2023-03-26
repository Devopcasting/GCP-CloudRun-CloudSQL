from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,Email,ValidationError
from flaskcrud.models import Employee

# Employee Form
class UpdateEmployeeFrom(FlaskForm):
    emp_name = StringField("Name",validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Update')

