from flask import Flask, render_template
app = Flask(__name__)
#flask always look to templates directory for rendering templates...
@app.route("/")
def index():
    headLine = "Hello World!"
    return render_template("index.html",headline=headLine)

