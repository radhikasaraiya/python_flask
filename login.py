from flask import *  
app = Flask(__name__)  


@app.route('/submit',methods = ['POST'])  
def submit():  
      uname=request.form['t1']  
      pwd=request.form['t2']  
      if uname=="bca" and pwd=="bca":  
          return "Welcome %s" %uname  
      else:
        return "Sorry User"
   

app.run(debug = True)  
