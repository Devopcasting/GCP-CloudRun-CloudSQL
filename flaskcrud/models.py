from flaskcrud import db, app

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(5))
    email = db.Column(db.String(120),unique=True,nullable=False)
    department = db.Column(db.String(20),nullable=False)

app.app_context().push()
db.create_all()
