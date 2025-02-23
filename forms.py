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
    agent_type = SelectField('Select type of agent:',
                            choices=[("", "---"), ('External', 'external'), ('Internal', 'internal')],
                            validators=[DataRequired()])
    number_of_supplements = SelectField('Select the number of supplements:',
                            choices=[("", "---"), ('none', 'none'), ('1 to 2', '1 to 2'),
                                     ('3 to 5', '3 to 5'), ('more than 5', 'more than 5')],
                            validators=[DataRequired()])

    age_of_policy_holder = SelectField('Enter the age of policy holder:',
                            choices=[("", "---"), ('18 to 20', '18 to 20'), ('21 to 25', '21 to 25'),
                                     ('26 to 30', '26 to 30'), ('31 to 35', '31 to 35'), ('36 to 40', '36 to 40'),
                                     ('41 to 50', '41 to 50'), ('51 to 65', '51 to 65'), ('over 65', 'over 65')],
                            validators=[DataRequired()])
    submit = SubmitField('Next >>', render_kw={"class": "btn-next"})


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
    witness_present = SelectField('Is a witness present?',
                                  choices=[("", "---"), ('No', 'no'), ('Yes', 'yes')],
                                  validators=[DataRequired()])
    address_change_claim = SelectField('Enter the number of adress change claim:',
                                      choices=[("", "---"), ('no change', 'no change'),
                                               ('under 6 months', 'under 6 months'), ('1 year', '1 year'),
                                               ('2 to 3 years', '2 to 3 years'), ('4 to 8 years', '4 to 8 years')],
                                      validators=[DataRequired()])
    rep_number = IntegerField('Select the individual number of insurance representative handling the claim (1-16):',
                                 validators=[DataRequired(), NumberRange(min=1, max=16)])
    submit = SubmitField('Request', render_kw={"class": "btn-next"})


# Form to collect data about driver:
class DriverInfoForm(FlaskForm):
    sex = SelectField('Select sex:',
                      choices=[("", "---"), ('Female', 'female'), ('Male', 'male')],
                      validators=[DataRequired(message="Please select gender.")])
    marital_status = SelectField('Select marital status:',
                                 choices=[("", "---"), ('Single', 'single'), ('Married', 'married'), ('Widow', 'widow'),
                                          ('Divorced', 'divorced')],
                                 validators=[DataRequired(message="Please select marital status.")])
    age = IntegerField('Age:',
                       validators=[DataRequired(message="Enter the age of driver:"),
                                   NumberRange(min=0, max=80, message="Age must be between 1 and 80")])
    driver_rating = SelectField('Select a rating of driver',
                             choices=[("", "---"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[DataRequired()])
    past_number_of_claim = SelectField('Select the number of past claims:',
                                       choices=[("", "---"), ('none', 'none'), ('1', '1'),
                                                ('2 to 4', '2 to 4'), ('more than 4', 'more than 4')],
                                       validators=[DataRequired()])
    number_of_cars = SelectField('Select the number of vehicles',
                             choices=[("", "---"), ('1 vehicle', '1 vehicle'), ('2 vehicles', '2 vehicles'),
                                      ('5 to 8', '5 to 8 vehicles'), ('more than 8', 'more than 8 vehicles')],
                             validators=[DataRequired()])
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
    age = SelectField('Select right age range:',
                       choices=[("", "---"), ('new', 'new'),
                                ('2 years', '2 years'), ('3 years', '3 years'), ('4 years', '4 years'),
                                ('5 years', '5 years'), ('6 years', '6 years'), ('7 years', '7 years'),
                                ('more than 7', 'more than 7')],
                       validators=[DataRequired()])
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
    submit = SubmitField('Next >>', render_kw={"class": "btn-next"})