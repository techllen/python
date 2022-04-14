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

class Rename_Overseer:
    all_carriers = []
    overseer = "FAA"
    
    @classmethod
    def rename_overseer(cls,new_name):
        cls.overseer = new_name
        
    @staticmethod
    def has_enough_workers(current_workforce,needed_workers):
        if(current_workforce >= needed_workers):
            print("Enough workers as is")
            return True
        elif(current_workforce <= needed_workers):
            print("Hire More Workers")
            return False