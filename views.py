from flask import Blueprint, render_template, Response
from LLM import llm

views  = Blueprint('views,' , __name__)

def catch():
     llm("little boy")



@views.route('/')
def home():
    return render_template("home.html")

@views.route('/interface')
def interface():
        catch()
        return "check the file"


@views.route('/video')
def video():
    return  "../assets/Silent spring.mp4"



    
     