
class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.destination = data
        self.price = data["data"][0]["price"],
        self.departure_city = data["data"][0]["route"][0]["cityFrom"],
        self.departure_airport_code = data["data"][0]["route"][0]["flyFrom"],
        self.city_to = data["data"][0]["route"][0]["cityTo"],
        self.arrival_airport_code = data["data"][0]["route"][0]["flyTo"],
        self.departure_date = data["data"][0]["route"][0]["local_departure"].split("T")[0],
        self.return_date = data["data"][0]["route"][1]["local_departure"].split("T")[0]
