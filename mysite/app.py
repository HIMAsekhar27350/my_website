from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/myresume")
def myresume():
    return render_template('myresume.html')

if __name__ == '__main__':
    app.run(debug=True)
