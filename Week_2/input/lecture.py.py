# class Carrier:
#     overseer = "FAA"

#     def __init__(self,year,name,city):
#         self.year = year
#         self.name = name
#         self.city = city

# carrier1 = Carrier(2022,"Coding Dojo Airlines","Dojo City")
# carrier2 = Carrier(2020,"Burger King Airline","Burlington City")

# print(carrier1.name)
# print(carrier2.name)

# class Rename_Overseer:
#     all_carriers = []
#     overseer = "FAA"
    
#     @classmethod
#     def rename_overseer(cls,new_name):
#         cls.overseer = new_name
        
#     @staticmethod
#     def has_enough_workers(current_workforce,needed_workers):
#         if(current_workforce >= needed_workers):
#             print("Enough workers as is")
#             return True
#         elif(current_workforce <= needed_workers):
#             print("Hire More Workers")
#             return False

class Carrier: # Define your class here
    all_carriers = [] # Class variable: list that will hold your carriers
    overseer = "Federal Aviation Administration" # Class variable

    def __init__(self, year, name, city):
        self.year = year
        self.name = name
        self.city = city
        self.flights = [] # List of flights
        self.total_workers = 0 # Workforce for this carrier
        Carrier.all_carriers.append(self) # Add this carrier

class Flight:
    def __init__(self, number, starting_city, ending_city):
        self.number = number
        self.starting_city = starting_city
        self.ending_city = ending_city


cd_airlines = Carrier(2022, "Coding Dojo Airlines", "Dojo City")
my_airline = Carrier(1903, "Wright Bros. Flights", "Kitty Hawk")
flight_one = Flight(555, "Seattle", "Reno")
flight_two = Flight(100, "Phoenix", "London")

cd_airlines.flights.append(flight_one)
cd_airlines.flights.append(flight_two)

my_airline.flights.append(flight_one)
my_airline.flights.append(flight_two)

print(str(cd_airlines.flights[0]))




