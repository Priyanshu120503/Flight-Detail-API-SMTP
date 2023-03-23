from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()

print('Welcome to Flight CLub')
print('We find the best flight deals and email you.')
while True:
    if 'n' == input('Add Member? (y/n): '):
        break
    f_name = input('Enter your first name:')
    l_name = input('Enter your last name:')
    email = input('Enter your email id: ')
    if email == input('Type your email again: '):
        data_manager.post_user(f_name, l_name, email)
        print('Success, your email has added.')
    else:
        print('Email does not match. Please try again!')

data_manager.put_city_code()
prices_sheet_data = data_manager.get_flight_data()
user_sheet_data = data_manager.get_user_data()
# print(prices_sheet_data)
ORIGIN_IATA = 'BOM'

today = datetime.now()

notification_manager = None

flight_search = FlightSearch()
for city in prices_sheet_data:
    flight = flight_search.get_flight_details(ORIGIN_IATA, city['iataCode'], today, today+timedelta(days=180))
    # flight is put in 'if' condition to check when flight=None
    if flight and flight.price < city['lowestPrice']:
        data_manager.update_price(city['id'], flight.price)
        if not notification_manager:
            notification_manager = NotificationManager()
        for user in user_sheet_data:
            notification_manager.send_mail(user['email'], 'Flight Price drop alert!!', str(flight))

if notification_manager:
    notification_manager.close_connection()
