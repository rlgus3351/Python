
import requests

customers_endpoint = "https://api.sheety.co/36d3616055838ab20a2732fa45eb70e9/flightPrices/user"
response = requests.get(url=customers_endpoint)
data = response.json()
customers_data = data['user']
print(customers_data)

