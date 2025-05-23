import os

import utils

from datetime import datetime
from dotenv import load_dotenv

from flask import jsonify, session, render_template, redirect, url_for, request, Flask
from flask_bootstrap import Bootstrap5

from forms import  ClaimInfoForm, DriverInfoForm, PolicyInfoForm, VehicleInfoForm
from models import db, ClaimDataTable, DriverDataTable, PolicyDataTable, VehicleDataTable, RequestTable
from new_request import make_request


#load dependencies:
load_dotenv()

#Initilalise Flask application:
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
Bootstrap5(app)


#Initialise database:
db.init_app(app)


#Create database if not exist:
db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace("sqlite:///", "")
if not os.path.exists(db_path):
    with app.app_context():
        db.create_all()


@app.route('/')
def index():
    return render_template("index.html", show_header=True)


@app.route('/about')
def about():
    return render_template("about.html", show_header=True)


@app.route('/antifraud')
def antifraud():
    return render_template("antifraud.html", show_header=True)


@app.route('/add_driver', methods=["GET", "POST"])
def add_driver():
    title = "Add data about driver:"
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
        print("Driver data added!")
        return redirect(url_for("add_vehicle"))
    return render_template("predictions.html", form=form, title=title, show_header=False)


@app.route('/add_vehicle', methods=["GET", "POST"])
def add_vehicle():
    title = "Add data about vehicle:"
    form = VehicleInfoForm()
    if form.validate_on_submit():
        new_vehicle = VehicleDataTable(
            make=form.make.data,
            vehicle_category=form.vehicle_category.data,
            age=form.age.data,
            vehicle_price=form.vehicle_price.data
        )
        db.session.add(new_vehicle)
        db.session.commit()
        session["vehicle_id"] = new_vehicle.id
        print("Vehicle data added!")
        return redirect(url_for("add_policy"))
    return render_template("predictions.html", form=form, title=title, show_header=False)


@app.route('/add_policy', methods=["GET", "POST"])
def add_policy():
    title = "Add data about policy:"
    form = PolicyInfoForm()
    if form.validate_on_submit():
        new_policy = PolicyDataTable(
            policy_number=form.policy_number.data,
            policy_start_date=form.policy_start_date.data,
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
    return render_template("predictions.html", form=form, title=title, show_header=False)


@app.route('/add_claim', methods=["GET", "POST"])
def add_claim():
    title = "Add details about claim:"
    driver_id = session.get("driver_id")
    vehicle_id = session.get("vehicle_id")
    policy_id = session.get("policy_id")

    form = ClaimInfoForm()
    if form.validate_on_submit():
        new_claim = ClaimDataTable(
            driver_id=int(driver_id),
            vehicle_id=int(vehicle_id),
            policy_id=int(policy_id),
            collision_date=form.collision_date.data,
            claim_report_datetime=datetime.now(),
            accident_area=form.accident_area.data,
            fault=form.fault.data,
            police_report=form.police_report_field.data,
            witness_present=form.witness_present.data,
            address_change_claim=form.address_change_claim.data,
            rep_number=form.rep_number.data
        )
        db.session.add(new_claim)
        db.session.commit()
        print("New claim reported successfully!")

        #select driver, vehicle and policy records:
        new_driver = DriverDataTable.query.get(driver_id)
        new_vehicle = VehicleDataTable.query.get(vehicle_id)
        new_policy = PolicyDataTable.query.get(policy_id)

        #make new record in RequestTable:
        new_request = RequestTable(
            Month = new_claim.collision_date.month,
            WeekOfMonth = utils.week_of_months(new_claim.collision_date),
            DayOfWeek = new_claim.collision_date.strftime('%A'),
            Make = new_vehicle.make,
            AccidentArea = new_claim.accident_area,
            DayOfWeekClaimed = new_claim.claim_report_datetime.strftime('%A'),
            MonthClaimed = new_claim.claim_report_datetime.month,
            WeekOfMonthClaimed =  utils.week_of_months(new_claim.claim_report_datetime.date()),
            Sex = new_driver.sex,
            MaritalStatus = new_driver.marital_status,
            Age = new_driver.age,
            Fault = new_claim.fault,
            PolicyType = new_vehicle.vehicle_category + " - " + new_policy.base_policy,
            VehicleCategory = new_vehicle.vehicle_category,
            VehiclePrice = new_vehicle.vehicle_price,
            PolicyNumber = new_policy.policy_number,
            RepNumber = new_claim.rep_number,
            Deductible = new_policy.deductible,
            DriverRating = new_driver.driver_rating,
            Days_Policy_Accident = utils.date_difference(date_1=new_claim.collision_date,
                                                         date_2=new_policy.policy_start_date),
            Days_Policy_Claim = utils.date_difference(date_1=new_claim.claim_report_datetime.date(),
                                                      date_2=new_policy.policy_start_date),
            PastNumberOfClaims = new_driver.past_number_of_claim,
            AgeOfVehicle = new_vehicle.age,
            AgeOfPolicyHolder = new_policy.age_of_policy_holder,
            PoliceReportFiled = new_claim.police_report,
            WitnessPresent = new_claim.witness_present,
            AgentType = new_policy.agent_type,
            NumberOfSuppliments = new_policy.number_of_supplements,
            AddressChange_Claim = new_claim.address_change_claim,
            NumberOfCars = new_driver.number_of_cars,
            Year = datetime.now().year,
            BasePolicy = new_policy.base_policy,
        )
        db.session.add(new_request)
        db.session.commit()
        print("New request is added successfully")

        # make a JSON representation:
        request_entry = RequestTable.query.get(new_request.id)
        request_json_printable = utils.to_dict(request_entry)
        print(f"The JSON is: {request_json_printable}")

        # make a request and get a response:
        response = make_request(json=request_json_printable)
        session["response"] = response
        print(response)

        # add prediction and fraud probability data in RequestTable:
        request = RequestTable.query.get(new_request.id)
        prediction = response["Result"]
        request.prediction = prediction
        # request.fraud_probability = 0 # TODO: add fraud_probability if API provides information about fraud probability
        db.session.commit()
        print("New request is added successfully")

        return redirect(url_for("result", prediction=prediction))
    return render_template("predictions.html", form=form, title=title)

@app.route('/result')
def result():
    prediction = request.args.get("prediction")
    print(f"the prediction is: {prediction}")
    print(type(prediction))
    return render_template("result.html", prediction=prediction, show_header=True)


@app.route('/database')
def database():
    requests = RequestTable.query.all()
    headers = [column.name for column in RequestTable.__table__.columns]
    # request_data = [{header: getattr(req, header) for header in headers} for req in requests]
    return render_template("database.html", requests=requests, headers=headers, show_header=True)


@app.route('/contact')
def contact():
    return render_template("contact.html", show_header=True)


if __name__ == "__main__":
    app.run(debug = True)