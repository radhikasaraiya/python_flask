from flask import Flask  
app = Flask(__name__)  
  
def about():  
    return "This is about page";  

def home():  
    return "This is Home page";  

app.add_url_rule("/about","about",about)  
app.add_url_rule("/home","home",home)  

app.run(debug = True)  