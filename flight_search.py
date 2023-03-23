import requests
from flight_data import FlightData
from datetime import datetime, timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.TEQUILA_API_KEY = '<api_key>'
        self.TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": self.TEQUILA_API_KEY,
        }

    def get_flight_details(self, fly_from: str, fly_to: str, date_from: datetime, date_to: datetime) -> FlightData:
        parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "INR",
            "max_stopovers": 4,
            "adults": 1,
            "max_sector_stopovers": 4,
            "limit": 1
        }
        response = requests.get(url=f'{self.TEQUILA_ENDPOINT}/v2/search', params=parameters, headers=self.headers)
        response.raise_for_status()
        print(fly_from, fly_to, date_from, date_to, end='\n\n')
        try:
            data = response.json()['data'][0]
        except IndexError:
            return None
        date = data['local_departure'].split('T')[0].split('-')
        departure_date = datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]))
        return_date = departure_date + timedelta(days=data['nightsInDest'])
        route_1 = [f'{r["cityFrom"]} -> {r["cityTo"]}' for r in data['route'] if r['return'] == 0]
        route_2 = [f'{r["cityFrom"]} -> {r["cityTo"]}' for r in data['route'] if r['return'] == 1]
        flight = FlightData(data['cityCodeFrom'], data['flyFrom'], data['cityCodeTo'], data['flyTo'], ', '.join(route_1),
                            len(route_1)-1, ', '.join(route_2), len(route_2)-1, departure_date.strftime('%d/%m/%Y'),
                            return_date.strftime('%d/%m/%Y'), float(data['price']))
        # return float(response.json()['data'][0]['price'])
        return flight

    def get_city_code(self, city_name: str):
        parameters = {
            "term": city_name,
            "limit": 1
        }
        response = requests.get(url=f'{self.TEQUILA_ENDPOINT}/locations/query', params=parameters, headers=self.headers)
        response.raise_for_status()
        print(response.json()['locations'])
        return response.json()['locations'][0]['code']


if __name__ == "__main__":
    f = FlightSearch()
    print(f.get_flight_details('LON', 'DPS', datetime.now(), datetime.now() + timedelta(days=28)))
    # print(f.get_city_code('New York'))
