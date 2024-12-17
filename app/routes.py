from flask import Flask             #from the flask module import the Flask class
#OOP -Object Oriented Paradigm
app = Flask(__name__)               #When you create an instance of a class, you get an object; app is now an object

@app.get("/aboutme")                       #Flask decorator that allows us to define routes
def home():
    me = {                          #Python3 disctionary
        "first_name": "Samuel",
        "last_name": "Dominguez",
        "hobbies": "Videogames",
        "is_online": True
    }

    return me                       #When return a dictionary from a flask view function, it's converted to JSON