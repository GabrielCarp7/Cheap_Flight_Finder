import requests
"""

API response structure 
{
  "data": [
    {
      "price": 420.99,        # Total price of the flight (including taxes)
      "route": [
        {
          "cityFrom": "London",  # Departure city name
          "flyFrom": "LON",       # Departure airport IATA code
          "cityTo": "New York",   # Arrival city name
          "flyTo": "JFK",        # Arrival airport IATA code
          "local_departure": "2024-04-10T12:00:00",  # Departure date and time (UTC)
          "local_arrival": "2024-04-11T18:00:00"   # Arrival date and time (UTC)
        },
        {
          # Information about the return leg (similar structure)
        }
      ],
      "airline": "BA",        # Airline code
      "bags_recheck_required": false  # Whether baggage recheck is required
    },
    // More flight options...
  ]
}

"""


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def get_iata_code(self, city_name):
        location_endpoint = f"{self.endpoint}/locations/query"
        headers = {"apikey": self.api_key}
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, params=query, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data["locations"]:
            return data["locations"][0]["code"]
        else:
            return None

    # Connect to the API and look for cheap flights anytime in the next 6 months
    def get_flights(self, fly_from, fly_to, date_from, date_to):
        endpoint = f"{self.endpoint}/search"
        headers = {"apikey": self.api_key}
        parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
        }
        response = requests.get(url=endpoint, headers=headers, params=parameters)
        response.raise_for_status()
        return response.json()
