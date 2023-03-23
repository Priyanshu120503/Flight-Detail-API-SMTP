import requests
from flight_search import FlightSearch


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/<your_sheety_code>/flightDeals/prices'
        self.SHEETY_USERS_ENDPOINT = 'https://api.sheety.co/<your_sheety_code>/flightDeals/users'

    def get_flight_data(self):
        response = requests.get(url=self.SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        print(response.json())
        # date = response.json()['price']
        # flights = []
        return response.json()['prices']

    def get_user_data(self):
        response = requests.get(url=self.SHEETY_USERS_ENDPOINT)
        response.raise_for_status()
        print(response.json())
        # date = response.json()['price']
        # flights = []
        return response.json()['users']

    def put_city_code(self):
        f = FlightSearch()
        for (index, city) in enumerate(self.get_flight_data(), start=2):
            if city['iataCode'] != '':
                continue
            put_endpoint = f'{self.SHEETY_PRICES_ENDPOINT}/{index}'
            city_code = f.get_city_code(city['city'])
            data = {
                'price': {
                    'iataCode': city_code
                }
            }
            response = requests.put(url=put_endpoint, json=data)
            # print(response.text)

    def post_user(self, f_name, l_name, email):
        data = {
            'user': {
                'firstName': f_name,
                'lastName': l_name,
                'email': email
            }
        }
        response = requests.post(url=self.SHEETY_USERS_ENDPOINT, json=data)
        print(response.text)

    def update_price(self, row_id: int, new_price):
        put_endpoint = f'{self.SHEETY_PRICES_ENDPOINT}/{row_id}'
        data = {
            "price": {
                'lowestPrice': new_price
            }
        }
        response = requests.put(url=put_endpoint, json=data)
        # print(response.text, end='\n\n')


if __name__ == "__main__":
    d = DataManager()
    # d.put_city_code()
