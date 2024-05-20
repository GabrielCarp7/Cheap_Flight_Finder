from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData
from datetime import date
from datetime import timedelta
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

sheety_key = os.getenv("sheety_key")
tequila_key = os.getenv("tequila_key")

# Endpoints and Keys
sheety_endpoint = "https://api.sheety.co/d216b0ffd5472e65a6bc6c9875c4e518/flightDeals/prices"
sheety_key = sheety_key

tequila_endpoint = "https://tequila-api.kiwi.com"
tequila_endpoint_search = "https://api.tequila.kiwi.com/v2"
tequila_key = tequila_key

# Flight Data
flight_from = "LON"

# Format the date >> Search for flights in this time frame
now = date.today()
to = now + timedelta(days=183)
date_from = f"{now.strftime('%d/%m/%Y')}"
date_to = f"{to.strftime('%d/%m/%Y')}"

# Email Data >> Email and Password required depending on user
email = ""
password = ""

sheety = DataManager(api_key=sheety_key, endpoint=sheety_endpoint)

iata = FlightSearch(api_key=tequila_key, endpoint=tequila_endpoint)
flights = FlightSearch(api_key=tequila_key, endpoint=tequila_endpoint_search)

email = NotificationManager(email=email, password=password, to_addrs=email)

# Get data
sheet_data = sheety.get_data()["prices"]

# Get IATA codes >> iataCode
if sheet_data[len(sheet_data)-1] == "":
    row_id = len(sheet_data) + 1
    for n in range(len(sheet_data)):
        updated_data = {
            "price": {
                "iataCode": iata.get_iata_code(sheet_data[n]["city"])
            }
        }
        sheety.update_row(row_id=f"{row_id}", data=updated_data)
        row_id += 1

# Loop through all the cities in the sheet
for n in range(len(sheet_data)):
    flight_code = sheet_data[n]["iataCode"]
    flight = flights.get_flights(fly_from=flight_from, fly_to=flight_code, date_from=date_from, date_to=date_to)

    get_data = FlightData(flight)

    if get_data.price[0] < sheet_data[n]["lowestPrice"]:
        email.send_email(price=get_data.price, from_flight=get_data.departure_city, to_flight=get_data.city_to,
                         start_date=get_data.departure_date, end_date=get_data.return_date)
