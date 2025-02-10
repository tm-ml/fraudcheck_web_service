from datetime import date

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from forms import FraudCheckForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "My top secret password!"
Bootstrap5(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predictions', methods=["GET", "POST"])
def predictions():
    form = FraudCheckForm()
    if form.validate_on_submit():

        print("Everything is OK!")
    return render_template("predictions.html", form=form)


@app.route('/database')
def database():
    return render_template("database.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")





if __name__ == "__main__":
    app.run(debug = True)