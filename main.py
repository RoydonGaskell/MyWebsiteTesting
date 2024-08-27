from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/home")
@app.route('/')
def index():
    return render_template("index.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/esports")
def esports():
    return render_template("esports.html")
@app.route("/programming")
def programming():
    return render_template("programming.html")
@app.route("/general")
def general():
    return render_template("general.html")







if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
