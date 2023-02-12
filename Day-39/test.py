import requests
from data_manager import DataManager
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "N27qIIHF-40MQRK0UDcLPpJoqk73suKv"
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
headers = {"apikey" : TEQUILA_API_KEY}
city_name = get_destination_code(row["city"])
query = {"term": city_name, "location_types": "city"}
response = requests.get(url=location_endpoint, headers=headers, params=query)
results = response.json()["locations"]
print(results)
code = results[0]["code"]