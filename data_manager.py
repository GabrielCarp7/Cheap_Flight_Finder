import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def get_data(self):
        # Retrieves data from a specified Sheety sheet.
        url = f"{self.endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def update_row(self, row_id, data):
        # Updates a specific row in a Sheety sheet.
        url = f"{self.endpoint}/{row_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()

    def add_row(self, data):
        # Adds a new row to a Sheety sheet.
        url = f"{self.endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
