from app import app, db
from flask import render_template, redirect, request, url_for
from app.models import Student

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/students')
def students():
    title = 'Show Students'
    page = request.args.get('page', 1, type=int)
    students = Student.query.paginate(page=page, per_page=3)

    return render_template('students.html', title=title, students=students)

@app.route('/student/new', methods=['GET', 'POST'])
def new_student():
    title = 'New Student'
    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        faculty = request.form['faculty']

        student = Student(student_id=student_id, student_name=student_name, faculty=faculty)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('students'))

    return render_template('new_student.html', title=title)