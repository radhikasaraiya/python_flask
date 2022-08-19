from flask import Flask  
app = Flask(__name__)  


#http://127.0.0.1:5000/study
@app.route('/study')  
def study():  
    return "Hello From Study";  
    
#http://127.0.0.1:5000/test/34
@app.route('/test/<int:age>')  
def test(age):  
    return "Age = %d "%age;  

#http://127.0.0.1:5000/user/34/intellect
@app.route('/user/<int:age>/<string:name>')  
def home(age,name):  
    return "Age = %d , Name=%s"%(age,name);  
  
if __name__ =="__main__":  
    app.run(debug = True)  