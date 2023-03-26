from flask import Blueprint, render_template, url_for, flash, redirect, request
from flaskcrud import app, db
from flaskcrud.models import Employee

homeBlueObj = Blueprint('home', __name__, template_folder='templates')

@homeBlueObj.route('/', methods=['POST', 'GET'])
def home():
    # Pagination
    page = request.args.get('page',1,type=int)
    # Check the length of employee database
    len_emp_db = len(Employee.query.all())
    # Select all Emp DB
    employeedb = Employee.query.order_by(Employee.id).paginate(page=page,per_page=5)

    return render_template('home/home.html', title="FlaskCRUD | Home", empdblen=len_emp_db, employee=employeedb)

# Delete Employee
@homeBlueObj.route('/delete/<int:empid>',methods=['GET','POST'])
def delete(empid):
    emp = Employee.query.get_or_404(empid)
    db.session.delete(emp)
    db.session.commit()
    flash(f"Employee {emp.name} deleted successfully",'success')
    return redirect(url_for('home.home'))