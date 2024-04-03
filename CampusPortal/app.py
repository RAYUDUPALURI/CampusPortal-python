from flask import Flask, render_template, request

app = Flask(_name_)

# Sample data for courses and grades
students = {
    "John Doe": {"courses": ["Math", "Physics", "History"], "grades": {"Math": 85, "Physics": 78, "History": 92}},
    "Jane Smith": {"courses": ["Biology", "Chemistry", "Literature"], "grades": {"Biology": 90, "Chemistry": 82, "Literature": 88}},
    "Alice Johnson": {"courses": ["Computer Science", "Art", "Geography"], "grades": {"Computer Science": 95, "Art": 76, "Geography": 87}}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        student_name = request.form['student_name']
        if student_name in students:
            student_info = students[student_name]
            return render_template('student.html', student_name=student_name, courses=student_info['courses'], grades=student_info['grades'])
        else:
            return render_template('error.html', message="Student not found!")
    else:
        return render_template('search_student.html')

if _name_ == '_main_':
    app.run(debug=True)