from app import db

class Student(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.String(11), nullable=False, unique=True)
    student_name = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Student: {}>".format(self.student_name)