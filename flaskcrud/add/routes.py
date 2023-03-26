from flask import Blueprint, render_template, url_for, flash, redirect, request
from flaskcrud import app, db
from flaskcrud.add.forms import EmployeeFrom
from flaskcrud.models import Employee

addBlueObj = Blueprint('add', __name__, template_folder='templates')

@addBlueObj.route('/', methods=['POST', 'GET'])
def add():
    form = EmployeeFrom()
    if form.validate_on_submit():
        emp_connection = Employee(name=form.emp_name.data,email=form.email.data,department=form.department.data)
        db.session.add(emp_connection)
        db.session.commit()
        flash(f"New Employee {form.emp_name.data} added successfully",'success')
        return redirect(url_for('home.home'))
    return render_template('add/add.html', title="FlaskCRUD | Add", form=form)