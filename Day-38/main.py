import requests
from datetime import datetime


YOUR_USERNAME = "gihyun"
YOUR_PASSWORD = "rkskekfk1!"

GENDER = "male"
WEIGHT_KG = 168.5
HEIGHT_CM = 63.5
AGE = 25

API_ID = "4909a917"
API_KEY = "eab3d0332a4f35176b5ce1f5fbeb629e"
sheet_endpoint = "https://api.sheety.co/36d3616055838ab20a2732fa45eb70e9/exercise/test1"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
test_endpoint = "https://api.sheety.co/36d3616055838ab20a2732fa45eb70e9/exercise/test1"
    

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,
}

body_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
email = {
    "name": "test1",
	"email": "rlgus8395@gmail.com"
}

response = requests.post(url = exercise_endpoint, json=body_data, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    sheet_response = requests.post(test_endpoint, json=sheet_inputs) 

    print(sheet_response.text)