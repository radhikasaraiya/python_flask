from flask import *  
   
app = Flask(__name__)  

#http://127.0.0.1:5000/admin  
@app.route('/admin')  
def admin():  
    return 'admin'  
#http://127.0.0.1:5000/staff  
@app.route('/staff')  
def staff():  
    return 'staff'  
  
@app.route('/student')  
def student():  
    return 'student'  
  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'staff':  
        return redirect(url_for('staff'))  
    if name == 'student':  
        return redirect(url_for('student'))  

app.run(debug = True)  