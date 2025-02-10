from datetime import date

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField , SelectField, SelectMultipleField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange


# Form to collect data to request API,
class FraudCheckForm(FlaskForm):
    collision_date = DateField('Select a day of collision:',
                               format='%d-%m-%Y', default=date.today,
                               validators=[DataRequired()])
    accident_area = SelectField('Select area of accident:',
                                choices=[("", "---"), ('Urban', 'urban'), ('Rural', 'rural')],
                                validators=[DataRequired(message="Please select area of accident.")])
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
    fault = SelectField('Select type of fault:',
                        choices=[("", "---"), ('Policy Holder', 'policy holder'), ('Third Party', 'third party')],
                        validators=[DataRequired()])
    #TODO
    policy_type = SelectField()
    vehicle_category = SelectField('Select type of fault',
                                   choices=[("", "---"), ('Sport', 'sport'),
                                            ('Utility', 'utility'), ('Sedan', 'sedan')],
                                   validators=[DataRequired()])
    vehicle_price = IntegerField('Enter vehicle price:',
                                 validators=[DataRequired(),NumberRange(min=0)])
    #TODO
    policy_number = IntegerField('Enter the number of policy:',
                                 validators=[DataRequired(),NumberRange(min=0)])
    deductible = SelectField('Select type deduction per claim',
                             choices=[("", "---"), ('300', '300'), ('400', '400'), ('500', '500'), ('700', '700')],
                             validators=[DataRequired()])
    driver_rating = SelectField('Select a rating of driver',
                             choices=[("", "---"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[DataRequired()])
    #TODO: do policzenia?
    # days_policy_accident =
    #TODO: do policzenia?
    # days_policy_claim =
    #TODO: zakodować:
    past_number_of_claim = IntegerField('Enter the number of past claims:',
                                         validators=[DataRequired(),NumberRange(min=0)])
    #TODO:
    # age_of_vehicle =
    # age_of_policy_holder =
    police_report_field = SelectField('Is there a police report? :',
                                      choices=[("", "---"), ('No', 'no'), ('Yes', 'yes')],
                                      validators=[DataRequired()])
    witness_present = SelectField('Is a witness present? :',
                                  choices=[("", "---"), ('No', 'no'), ('Yes', 'yes')],
                                  validators=[DataRequired()])
    gent_type = SelectField('Select type od agent:',
                            choices=[("", "---"), ('External', 'external'), ('Internal', 'internal')],
                            validators=[DataRequired()])
    #TODO: zakodować funkcja:
    number_of_supplements = IntegerField('Enter the number of supplements:',
                                         validators=[DataRequired(),NumberRange(min=0)])
    #TODO: zakodować funkcja:
    address_change_claim = IntegerField('Enter the number of supplements:',
                                         validators=[DataRequired(),NumberRange(min=0)])
    #TODO: zakodować funkcja:
    number_of_cars = IntegerField('Enter the number of cars:',
                                  validators=[DataRequired(),NumberRange(min=0)])
    #TODO: może usunąć od razu?
    # year =
    base_policy = SelectField('Select type of policy:',
                                choices=[("", "---"), ('Liability', 'liability'), ('Collision', 'collision'),
                                         ('All Perils', 'all perils')],
                                validators=[DataRequired()])
    submit = SubmitField('Request')



# class PolicyInfoForm(FlaskForm):
# class DamageInfoForm(FlaskForm):
# class DriverInfoForm(FlaskForm):
# class VehicleInfoForm(FlaskForm):