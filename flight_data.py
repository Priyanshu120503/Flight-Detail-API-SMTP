class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, from_city: str, from_airport: str, to_city: str, to_airport: str, out_bound_route: str, out_bound_stopovers: int, in_bound_route: str, in_bound_stopovers: int, departure_date: str, return_date: str, price: float):
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.out_date = departure_date
        self.return_date = return_date
        self.price = price
        self.out_route = out_bound_route
        self.out_stopovers = out_bound_stopovers
        self.return_route = in_bound_route
        self.return_stopovers = in_bound_stopovers

    def __str__(self):
        return f'From: {self.from_city}     From Airport: {self.from_airport}\n' \
               f'To: {self.to_city}     To Airport: {self.to_airport}\n' \
               f'Departure: {self.out_date}     Return: {self.return_date}\n' \
               f'Price: Rs. {self.price}\n' + \
               (f'Flight has {self.out_stopovers} stop over for {self.from_city} to {self.to_city}. '
                f'{self.out_route}\n' if self.out_stopovers >= 1 else '\n') + \
               (f'Flight has {self.return_stopovers} stop over for {self.to_city} to {self.from_city}. '
                f'{self.return_route}\n' if self.return_stopovers >= 1 else '\n')
