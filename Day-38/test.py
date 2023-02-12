import requests

GENDER = "male"
WEIGHT_KG = 168.5
HEIGHT_CM = 63.5
AGE = 25


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_ID = "4909a917"
API_KEY = "eab3d0332a4f35176b5ce1f5fbeb629e"

headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

body_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url = exercise_endpoint, json=body_data, headers=headers)
result = response.json()



for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            # "date": today_date,
            # "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

print(sheet_inputs)
