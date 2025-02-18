import json
import requests

from main import app

from sqlalchemy.orm import sessionmaker
from models import db, ClaimDataTable, DriverDataTable, PolicyDataTable, VehicleDataTable


#get data from database:
# def get_claim_data():
#     claim_data = db.get_or_404(ClaimDataTable, 1)
#     print(claim_data.driver.sex)
#     claim_details = []
#     # for claim in claim_data:
#     #     print(claim)
#     #
#     # claims_list = []
#     ########
#     "Month": "Dec",
#     "WeekOfMonth": 5,
#     "DayOfWeek": "Wednesday",
#     "Make": "Honda",
#     "AccidentArea": "Urban",
#     "DayOfWeekClaimed": "Tuesday",
#     "MonthClaimed": "Jan",
#     "WeekOfMonthClaimed": 1,
#     "Sex": "Female",
#     "MaritalStatus": "Single",
#     "Age": 21,
#     "Fault": "Policy Holder",
#     "PolicyType": "Sport - Liability",
#     "VehicleCategory": "Sport",
#     "VehiclePrice": "more than 69000",
#     "PolicyNumber": 1,
#     "RepNumber": 12,
#     "Deductible": 300,
#     "DriverRating": 1,
#     "Days_Policy_Accident": "more than 30",
#     "Days_Policy_Claim": "more than 30",
#     "PastNumberOfClaims": "none",
#     "AgeOfVehicle": "3 years",
#     "AgeOfPolicyHolder": "26 to 30",
#     "PoliceReportFiled": "No",
#     "WitnessPresent": "No",
#     "AgentType": "External",
#     "NumberOfSuppliments": "none",
#     "AddressChange_Claim": "1 year",
#     "NumberOfCars": "3 to 4",
#     "Year": 1994,
#     "BasePolicy": "Liability"
#     ############
#     return claims_list


with app.app_context():
    get_claim_data()





# def convert_to_json(data):
#     return json.dumps(data, default=str)
#
# def request(data):
#     url = ""
#     headers = ""
#
#     response = requests.post(url, data=data, headers=headers)
#
#     if response.status_code == 200:
#         print("Data sent successfully!")
#     else:
#         print(f"Error: {response.status.code} - {response.tect}")
#
# def main():
#     claim_data = get_claim_data()
#
#     json_data = convert_to_json(claim_data)
#
#     request(json_data)