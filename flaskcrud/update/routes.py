from flask import Blueprint, render_template, url_for, flash, redirect, request
from flaskcrud import app, db
from flaskcrud.update.forms import UpdateEmployeeFrom
from flaskcrud.models import Employee

updateBlueObj = Blueprint('update', __name__, template_folder='templates')

@updateBlueObj.route('/<int:empid>', methods=['POST', 'GET'])
def update(empid):
    form = UpdateEmployeeFrom()
    emp_conn = Employee.query.get_or_404(empid)
    if form.validate_on_submit():
        emp_conn.name = form.emp_name.data
        emp_conn.department = request.form.get('select-department')
        db.session.commit()
        flash(f"Employee {form.emp_name.data} updated successfully",'success')
        return redirect(url_for('home.home'))
    return render_template('update/update.html', title="FlaskCRUD | Update", form=form, empconn=emp_conn)