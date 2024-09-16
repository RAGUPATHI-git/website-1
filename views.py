from flask import Blueprint, render_template, Response

views  = Blueprint('views,' , __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/interface')
def interface():
    return "this is interface page"

@views.route('/video')
def video():
    return  "../assets/Silent spring.mp4"
    
     