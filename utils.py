from datetime import datetime, date

def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}

def date_difference(date_1: date, date_2: date) -> int:
    print(type(date_1))
    print(type(date_2))
    date_diff = abs((date_2 - date_1).days)
    return date_diff

def week_of_months(date: date) -> int:
    first_day_of_month = date.replace(day=1)
    first_day_of_month_weekday = first_day_of_month.weekday()
    number_of_week = (date.day + first_day_of_month_weekday) // 7 + 1
    return number_of_week

def make_policy_type(veh_cat: str, base_policy: str) -> str:
    policy_type
    return policy_type


# month_mapping = {"01": "Jan", "02": 'Feb', "03": "Mar", "04": "Apr", "05": "May", "06": "Jun",
#                  "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
#
# DayOfWeek =
#
#
# {'Month': ['Dec', 'Jan', 'Oct', 'Jun', 'Feb', 'Nov', 'Apr', 'Mar', 'Aug', 'Jul', 'May', 'Sep']}
# {'DayOfWeek': ['Wednesday', 'Friday', 'Saturday', 'Monday', 'Tuesday', 'Sunday', 'Thursday']}
#
#
# {'Make': ['Honda', 'Toyota', 'Ford', 'Mazda', 'Chevrolet', 'Pontiac', 'Accura', 'Dodge', 'Mercury', 'Jaguar', 'Nisson', 'VW', 'Saab', 'Saturn', 'Porche', 'BMW', 'Mecedes', 'Ferrari', 'Lexus']}
# {'AccidentArea': ['Urban', 'Rural']}
# {'DayOfWeekClaimed': ['Tuesday', 'Monday', 'Thursday', 'Friday', 'Wednesday', 'Saturday', 'Sunday']}
# {'MonthClaimed': ['Jan', 'Nov', 'Jul', 'Feb', 'Mar', 'Dec', 'Apr', 'Aug', 'May', 'Jun', 'Sep', 'Oct']}
# {'Sex': ['Female', 'Male']}
# {'MaritalStatus': ['Single', 'Married', 'Widow', 'Divorced']}
# {'Fault': ['Policy Holder', 'Third Party']}
# {'PolicyType': ['Sport - Liability', 'Sport - Collision', 'Sedan - Liability', 'Utility - All Perils', 'Sedan - All Perils', 'Sedan - Collision', 'Utility - Collision', 'Utility - Liability', 'Sport - All Perils']}
# {'VehicleCategory': ['Sport', 'Utility', 'Sedan']}
# {'VehiclePrice': ['more than 69000', '20000 to 29000', '30000 to 39000', 'less than 20000', '40000 to 59000', '60000 to 69000']}
# {'Days_Policy_Accident': ['more than 30', '15 to 30', 'none', '1 to 7', '8 to 15']}
# {'Days_Policy_Claim': ['more than 30', '15 to 30', '8 to 15']}
# {'PastNumberOfClaims': ['none', '1', '2 to 4', 'more than 4']}
# {'AgeOfVehicle': ['3 years', '6 years', '7 years', 'more than 7', '5 years', 'new', '4 years', '2 years']}
# {'AgeOfPolicyHolder': ['26 to 30', '31 to 35', '41 to 50', '51 to 65', '21 to 25', '36 to 40', '16 to 17', 'over 65', '18 to 20']}
# {'PoliceReportFiled': ['No', 'Yes']}
# {'WitnessPresent': ['No', 'Yes']}
# {'AgentType': ['External', 'Internal']}
# {'NumberOfSuppliments': ['none', 'more than 5', '3 to 5', '1 to 2']}
# {'AddressChange_Claim': ['1 year', 'no change', '4 to 8 years', '2 to 3 years', 'under 6 months']}
# {'NumberOfCars': ['3 to 4', '1 vehicle', '2 vehicles', '5 to 8', 'more than 8']}
# {'BasePolicy': ['Liability', 'Collision', 'All Perils']}