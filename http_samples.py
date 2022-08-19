from flask import Flask  
app = Flask(__name__)  
 

#http://127.0.0.1:5000/study
@app.route('/study', methods=['POST'])  
def study():  
    return "Hello From POST";  
    
 
@app.route('/study2', methods=['GET'])  
def study2():  
    return "Hello From GET";  

@app.route('/studydelete', methods=['DELETE'])  
def studydelete():  
    return "Hello From Delete";  

@app.route('/studyput', methods=['PUT'])  
def studyput():  
    return "Hello From PUT";  

app.run(debug = True)  