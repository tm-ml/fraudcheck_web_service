from datetime import date

from flask_wtf import FlaskForm
from wtforms.fields import IntegerField , SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange


# Form to collect data about policy:
class PolicyInfoForm(FlaskForm):
    policy_number = IntegerField('Enter the number of policy:',
                                 validators=[DataRequired(),NumberRange(min=0, max=15420)])
    policy_start_date = DateField('Select a policy start date:',
                               default=date.today,
                               validators=[DataRequired()])
    deductible = SelectField('Select type deduction per claim',
                             choices=[("", "---"), ('300', '300'), ('400', '400'), ('500', '500'), ('700', '700')],
                             validators=[DataRequired()])
    base_policy = SelectField('Select type of policy:',
                                choices=[("", "---"), ('Liability', 'liability'), ('Collision', 'collision'),
                                         ('All Perils', 'all perils')],
                                validators=[DataRequired()])
    agent_type = SelectField('Select type od agent:',
                            choices=[("", "---"), ('External', 'external'), ('Internal', 'internal')],
                            validators=[DataRequired()])
    number_of_supplements = IntegerField('Enter the number of supplements:',
                                         validators=[DataRequired(),NumberRange(min=0)])
    age_of_policy_holder = IntegerField('Enter the name of policy holder:',
                                             validators=[DataRequired(),NumberRange(min=0)])
    submit = SubmitField('Next >>')


# Form to collect data about claim:
class ClaimInfoForm(FlaskForm):
    collision_date = DateField('Select a day of collision:',
                               default=date.today,
                               validators=[DataRequired()])
    accident_area = SelectField('Select area of accident:',
                                choices=[("", "---"), ('Urban', 'urban'), ('Rural', 'rural')],
                                validators=[DataRequired()])
    fault = SelectField('Select type of fault:',
                        choices=[("", "---"), ('Policy Holder', 'policy holder'), ('Third Party', 'third party')],
                        validators=[DataRequired()])
    police_report_field = SelectField('Is there a police report? :',
                                      choices=[("", "---"), ('No', 'no'), ('Yes', 'yes')],
                                      validators=[DataRequired()])
    witness_present = SelectField('Is a witness present? :',
                                  choices=[("", "---"), ('No', 'no'), ('Yes', 'yes')],
                                  validators=[DataRequired()])
    address_change_claim = IntegerField('Enter the number of adress change claim:',
                                         validators=[DataRequired(),NumberRange(min=0)])
    rep_number = IntegerField('Select the individual number of insurance representative handling the claim (1-16):',
                                 validators=[DataRequired(), NumberRange(min=1, max=16)])
    submit = SubmitField('Request')


# Form to collect data about driver:
class DriverInfoForm(FlaskForm):
    sex = SelectField('Select sex:',
                      choices=[("", "---"), ('Female', 'female'), ('Male', 'male')],
                      validators=[DataRequired(message="Please select gender.")])
    marital_status = SelectField('Select marital status:',
                                 choices=[("", "---"), ('Single', 'single'), ('Married', 'married'), ('Widow', 'widow'),
                                          ('Divorced', 'divorced')],
                                 validators=[DataRequired(message="Please select marital status.")])
    age = IntegerField('Age',
                       validators=[DataRequired(message="Select marital status:"),
                                   NumberRange(min=0, max=125, message="Age must be between 1 and 99")])
    driver_rating = SelectField('Select a rating of driver',
                             choices=[("", "---"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[DataRequired()])
    past_number_of_claim = IntegerField('Enter the number of past claims:',
                                         validators=[DataRequired(),NumberRange(min=0)])
    number_of_cars = IntegerField('Enter the number of cars:',
                                  validators=[DataRequired(),NumberRange(min=0)])
    submit = SubmitField('Next >>', render_kw={"class": "btn-next"})


class VehicleInfoForm(FlaskForm):
    make = SelectField('Select type of fault',
                       choices=[("", "---"), ('Honda', 'Honda'), ('Toyota', 'Toyota'), ('Ford', 'Ford'),
                                ('Mazda', 'Mazda'), ('Chevrolet', 'Chevrolet'), ('Pontiac', 'Pontiac'),
                                ('Acura', 'Acura'), ('Dodge', 'Dodge'), ('Mercury', 'Mercury'),
                                ('Jaguar', 'Jaguar'), ('Nissan', 'Nissan'), ('VW', 'VW'), ('Saab', 'Saab'),
                                ('Saturn', 'Saturn'), ('Porsche', 'Porsche'), ('BMW', 'BMW'), ('Mercedes', 'Mercedes'),
                                ('Ferrari', 'Ferrari'), ('Lexus', 'Lexus')],
                       validators=[DataRequired()])
    year_of_production = IntegerField('Enter year od production:',
                                 validators=[DataRequired(),NumberRange(min=0)])
    vehicle_category = SelectField('Select type of fault',
                                   choices=[("", "---"), ('Sport', 'sport'),
                                            ('Utility', 'utility'), ('Sedan', 'sedan')],
                                   validators=[DataRequired()])
    vehicle_price = SelectField('Select the estimated range of vehicle price:',
                       choices=[("", "---"), ('less than 20000', 'less than 20000'),
                                ('20000 to 29000', '20000 to 29000'), ('30000 to 39000', '30000 to 39000'),
                                ('40000 to 59000', '40000 to 59000'), ('60000 to 69000', '60000 to 69000'),
                                ('more than 69000', 'more than 69000')],
                       validators=[DataRequired()])
    submit = SubmitField('Next >>')