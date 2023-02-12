#Todo 1. Modify the data. py file (dont'change the main.py)
#Todo 2. Make a get() request to fetch 10 True or False questions.
#Todo 3. Parse the JSON response and replace the value of question_data(don't change the variable name)  

from xmlrpc.client import boolean
import requests
parameters = {
    "amount": 10,
    "type" : "boolean",
    "category" : 18,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

