from email.headerregistry import HeaderRegistry
import requests
from datetime import datetime

USERNAME = "kwongihyun"
TOKEN = "rkskekfk1!"
GRAPH_ID = "graph1"
#------------------------------------------step 1------------------------------------------
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

#------------------------------------------step 2------------------------------------------

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url = graph_endpoint, json= graph_config, headers=headers)
# print(response.text)

#------------------------------------------step 3------------------------------------------
# https://pixe.la/v1/users/kwongihyun/graphs/graph1.html 

#------------------------------------------step 4------------------------------------------
pixel_creation_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime(year= 2022, month=7, day=23)

# print(today.strftime("%Y%m%d"))


pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "9.74",
}

# response =requests.post(url = pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

#------------------------------------------step 5------------------------------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220722"

update_data = {
    "quantity" : "9.74",
}

response = requests.put(url = update_endpoint, json=update_data, headers=headers)
print(response.text)

#------------------------------------------step 6------------------------------------------
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210725"

# response = requests.delete(url = delete_endpoint, headers=headers)
# print(response.text)