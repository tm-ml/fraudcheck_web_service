import requests


antifraud_api_endpoint = "https://antifroud-api.onrender.com/predict"
headers = {"Content-Type": "application/json"}

def make_request(json):
    response = requests.post(url=antifraud_api_endpoint, json=json, headers=headers)
    print(response)
    print(response.status_code)
    print(response.text)
    try:
        response_json = response.json()
        print(f"Response JSON: {response_json}")
        return response_json
    except ValueError:
        print("Response is not in JSON format!")




# json = {
#          "Month": "Dec",
#          "WeekOfMonth": 5,
#          "DayOfWeek": "Wednesday",
#          "Make": "Honda",
#          "AccidentArea": "Urban",
#          "DayOfWeekClaimed": "Tuesday",
#          "MonthClaimed": "Jan",
#          "WeekOfMonthClaimed": 1,
#          "Sex": "Female",
#          "MaritalStatus": "Single",
#          "Age": 21.0,
#          "Fault": "Policy Holder",
#          "PolicyType": "Sport - Liability",
#          "VehicleCategory": "Sport",
#          "VehiclePrice": "more than 69000",
#          "PolicyNumber": 1.0,
#          "RepNumber": 12,
#          "Deductible": 300,
#          "DriverRating": 1,
#          "Days_Policy_Accident": "more than 30",
#          "Days_Policy_Claim": "more than 30",
#          "PastNumberOfClaims": "none",
#          "AgeOfVehicle": "3 years",
#          "AgeOfPolicyHolder": "26 to 30",
#          "PoliceReportFiled": "No",
#          "WitnessPresent": "No",
#          "AgentType": "External",
#          "NumberOfSuppliments": "none",
#          "AddressChange_Claim": "1 year",
#          "NumberOfCars": "3 to 4",
#          "Year": 1994,
#          "BasePolicy": "Liability"
#      }

