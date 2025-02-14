import os

from datetime import datetime, date
from dotenv import load_dotenv

from flask import session, render_template, redirect, url_for, Flask
from flask_bootstrap import Bootstrap5

from forms import  ClaimInfoForm, DriverInfoForm, PolicyInfoForm, VehicleInfoForm
from databases import db, Base, ClaimDataTable, DriverDataTable, PolicyDataTable, VehicleDataTable

#load dependencies:
load_dotenv()

#Initilalise Flask application:
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
Bootstrap5(app)

#Initialise database:
db.init_app(app)

#Create database:
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predictions', methods=["GET", "POST"])
def predictions():
    form = DriverInfoForm()
    if form.validate_on_submit():
        new_driver = DriverDataTable(
            sex=form.sex.data,
            marital_status=form.marital_status.data,
            age=form.age.data,
            driver_rating=form.driver_rating.data,
            past_number_of_claim=form.past_number_of_claim.data,
            number_of_cars=form.number_of_cars.data
        )
        db.session.add(new_driver)
        db.session.commit()
        session["driver_id"] = new_driver.id
        print(session.get("driver_id"))
        print("Driver data added!")
        return redirect(url_for("add_vehicle"))
    return render_template("predictions.html", form=form)

@app.route('/add_vehicle', methods=["GET", "POST"])
def add_vehicle():
    form = VehicleInfoForm()
    if form.validate_on_submit():
        new_vehicle = VehicleDataTable(
            make=form.make.data,
            vehicle_category=form.vehicle_category.data,
            year_of_production=form.year_of_production.data
        )
        db.session.add(new_vehicle)
        db.session.commit()
        session["vehicle_id"] = new_vehicle.id
        print("Vehicle data added!")
        return redirect(url_for("add_policy"))
    return render_template("predictions.html", form=form)

@app.route('/add_policy', methods=["GET", "POST"])
def add_policy():
    form = PolicyInfoForm()
    if form.validate_on_submit():
        new_policy = PolicyDataTable(
            policy_number=form.policy_number.data,
            deductible=form.deductible.data,
            base_policy=form.base_policy.data,
            agent_type=form.agent_type.data,
            number_of_supplements=form.number_of_supplements.data,
            age_of_policy_holder=form.age_of_policy_holder.data
        )
        db.session.add(new_policy)
        db.session.commit()
        session["policy_id"] = new_policy.id
        print("Policy data added!")
        return redirect(url_for("add_claim"))
    return render_template("predictions.html", form=form)


###############
@app.route('/add_claim', methods=["GET", "POST"])
def add_claim():
    form = ClaimInfoForm()
    if form.validate_on_submit():
        new_claim = ClaimDataTable(
            driver_id=session.get("driver_id"),
            vehicle_id=session.get("vehicle_id"),
            policy_id=session.get("policy_id"),
            collision_date=form.collision_date.data,
            claim_report_date=datetime.now(),
            accident_area=form.accident_area.data,
            fault=form.fault.data,
            police_report=form.police_report_field.data,
            witness_present=form.witness_present.data,
            address_change_claim=form.address_change_claim.data
        )
        db.session.add(new_claim)
        db.session.commit()
        print("New record added successfully!")
    return render_template("predictions.html", form=form)





@app.route('/database')
def database():
    return render_template("database.html")



@app.route('/contact')
def contact():
    return render_template("contact.html")

# @app.route('/index')
# def database():
#     return render_template("index.html")




if __name__ == "__main__":
    app.run(debug = True)