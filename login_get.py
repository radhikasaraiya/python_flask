from flask import *  
app = Flask(__name__)  

@app.route('/submit',methods = ['GET'])  
def submit():  
      uname=request.args.get('t1')  
      pwd=request.args.get('t2') 
      if uname=="bca" and pwd=="bca":  
          return "Welcome %s" %uname  
      else:
        return "Sorry User"
   

app.run(debug = True)  

