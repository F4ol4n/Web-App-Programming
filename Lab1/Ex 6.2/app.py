from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    student = {
        "name": "Nguyen Minh Chinh",
        "student_id": "2275106050051",
        "academic_year": "2nd year",
        "major": "Information Technology",
        "hobbies": ["Reading books", "Sleeping", "Listening to Music"],
    }
    return render_template('student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)