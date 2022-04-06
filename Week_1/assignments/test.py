# fruits = ["orange","pawpaw",2,2.5]
# myName = "allen"
# age = 29
# born = 1992
# print(f"{myName} {age} {born}")
# print(fruits)
# print("my name is" + str(age) )

# weight = 10.9
# print(int(weight))

# numbers = [78,22,11,1,2,3,4,5,6,7]

# print(numbers[1:])
# print(enumerate(numbers))
# print(min(numbers))
# print(sorted(numbers))


# x = "First string"
# y = "Second string"

# print(x +" "+ y)
# print(x,y)
# print(f"{x} {y}")

# x = [3,8,4]

# y = (-1,True,15)
# x.append("numbers")
# x.insert(2,99)
# x.remove(99)
# x.pop(3)
# x.reverse
# print(x)
# print(y)

# someDictionary = {
#     1:2,
#     2:200,
#     "cars": ["honda","toyota"]
# }

# print(someDictionary.get("cars"))

# def list_cars():
#     return ("camaro","ford")

# print(list_cars())



# fruits = {}

# fruits["core"]="mango"
# fruits["pulp"]="pawpaw"


# print(len(fruits))

# for val in "string":
#     if val == "i":
#         continue
#     print(val)

# x = 2

# if not x:
#     print("i am here")
    
    

from unicodedata import name


def cars(car1 = "subaru"):
    print(car1)
    
cars("tesla")

def names_and_age(first_name = "Majili",second_name = "Kilo",age = 50):
    print(f"{first_name}\n{second_name}\n{age}")
    
def names_and_age(first_name = "Majili",second_name = "Kilo"):
    print(f"{first_name}\n{second_name}")
    
names_and_age("kiiza","kisa",67);