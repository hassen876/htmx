
from flask import Flask, render_template, request

app=Flask(__name__)

languages_frameworks={
   'python':['Django', 'flask', 'fastAPI'],
   'ruby' :['sinatra', 'rails'],
   'javascript': ['express', 'hapi']
}

@app.get("/")
def home():
    return render_template("home.html")


@app.get("/frameworks")
def frameworks():
    language=request.args.get("language")
    list_of_frameworks=languages_frameworks[language]
    return render_template("options.html", list_of_frameworks=list_of_frameworks)