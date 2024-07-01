import requests
from brewery import Brewery


class Breweries:
    # set base url on initialisation.
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/v1/breweries"

    # Function to get the list of all the breweries.
    def all(self):
        response = requests.get(self.base_url)

        return self.get_list(response.json())

    # Function that gets all breweries of a certain state.
    def by_state(self, state):
        state_params = {
            "by_state": state
        }
        response = requests.get(self.base_url, params=state_params)
        return self.get_list(response.json())

    # Function that gets a list of breweries closest to a certain location (in latitude/longitude)
    def by_distance(self, lat, long):
        distance_params = {
            "by_dist": f"{lat},{long}"

        }
        response = requests.get(self.base_url, params=distance_params)
        return self.get_list(response.json())

    # Function that gets a list of breweries of a certain type
    def by_type(self, type):
        type_params = {
            "by_type": type
        }
        response = requests.get(self.base_url, params=type_params)
        return self.get_list(response.json())

    # Function that converts the API result into a list of Brewery objects
    def get_list(self, API_text):
        list = []
        for location in API_text:

            list.append(Brewery(location["id"], location["name"], location["brewery_type"], location["address_1"], location["state"], location["phone"], location["website_url"]))
        return list