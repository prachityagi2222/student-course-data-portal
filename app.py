import sys
from jinja2 import Template
import matplotlib.pyplot as plt
import csv


#---------------Templates-----------------
error_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Something went wrong</title>
</head>
<body>
    <h1>Wrong Inputs</h1>
    <p>Something went wrong.</p>
    
</body>
</html>
"""

student_template = """<!DOCTYPE html>
<html >
<head>
    <title>Student Data</title>
</head>
<body>
    <h1>Student Details</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Student ID</th>
                <th>Course ID</th>
                <th>Marks</th>
            </tr>
        </thead>
        <tbody>
            {% for course_id, marks in student.items() %}
            <tr>
                <td>{{id}}</td>
                <td>{{course_id}}</td>
                <td>{{marks}}</td>
            </tr>
            {% endfor %}
            <tr>
                <td colspan="2">Total Marks</td>
                <td>{{total}}</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

course_template = """<!DOCTYPE html>
<html >
<head>
    <title>Course Data</title>
</head>
<body>
    <h1>Course Details</h1>
    <table border="1" >
        <tr>
            <td>Average Marks</td>
            <td>Maximum Marks</td>
        </tr>
        <tr>
            <td>{{average}}</td>
            <td>{{max}}</td>
        </tr>
    </table>
    <img height="300" src="histogram.png" alt="histogram of marks"/>
</body>
</html>
"""


#------------Data Loading-------------
def load_data():
    file = open("data.csv", "r")
    reader = csv.DictReader(file)
    return list(reader)
data = load_data()

#------------Validation-----------------
def isValid(s, id):
    student_ids = [int(row["Student id"]) for row in data]
    course_ids = [int(row[" Course id"]) for row in data]
    if (s == "c"):
        if id in course_ids:
            return True
    else:
        if id in student_ids:
            return True
    return False

#-------------------------Business Logic--------------------
def get_student_data(id):
    required_data = {} #course_id: marks
    sum = 0
    for row in data:
        student_id = int(row["Student id"])
        if (student_id == id):
            course_id = int(row[" Course id"])
            mark = int(row[' Marks'])
            sum += mark
            required_data[course_id] = mark
    return required_data, sum

def get_course_data(id):
    required_marks = []
    for row in data:
        course_id = int(row[' Course id'])
        if course_id == id:
            mark = int(row[" Marks"]) 
            required_marks.append(mark)
    total = sum(required_marks)
    average = total/len(required_marks)
    return total, average, required_marks

def generate_histogram(nums):
    plt.hist(nums, bins=5, color='skyblue', edgecolor='black')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')

#-----------------------------Main-----------------------------
def main():
    #accepting input
    id_type = sys.argv[1]
    id = int(sys.argv[2])

    #genrate template and render template
    html_doc = error_template

    #course details page
    if (id_type == "-c" and isValid("c", id)):
        template = Template(course_template)
        total, average, required_marks = get_course_data(id)
        generate_histogram(required_marks)
        html_doc = template.render( max=max(required_marks), average=average)

    #for student details page
    elif (id_type == "-s" and isValid("s", id)):
        template = Template(student_template)
        student_data, total_marks = get_student_data(id)
        html_doc = template.render(id=id, student=student_data, total=total_marks)

    #write template
    file = open("output.html", "w")
    file.write(html_doc)
    file.close()

if __name__ == "__main__":
    main()

