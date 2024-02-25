from flask import Flask
 
app = Flask(__name__)
 
# Define a route to display company name, developer's name, and student ID
@app.route('/')
def index():
    company_name = "<span style='font-weight: bold; color: #007bff;'>Wild Rydes</span>"
    developer_name = "Developer: Mahara Mahara"
    student_id = "Student ID: 100944755"
    return f"<h1>{company_name}</h1><br>{developer_name}<br>{student_id}"
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

