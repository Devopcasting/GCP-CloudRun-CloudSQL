from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,Email,ValidationError
from flaskcrud.models import Employee

# Employee Form
class EmployeeFrom(FlaskForm):
    emp_name = StringField("Name",validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    department = SelectField('Department', choices=[('Finance','Finance'),('IT','IT'),('Human Resource','Human Resource')])
    submit = SubmitField('Add')

    def validate_email(self,email):
        emp = Employee.query.filter_by(email=email.data).first()
        email_emp = email.data
        if email_emp.split('@')[1] != "gmail.com":
            raise ValidationError('Please enter your valid Gmail ID')
        if emp:
            raise ValidationError('Gmail ID is already taken')
