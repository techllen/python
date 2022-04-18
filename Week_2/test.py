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

from http.client import SWITCHING_PROTOCOLS


x = 2

# if not x:
#     print("i am here")

# from unicodedata import name

# def cars(car1 = "subaru"):
#     # print(car1)
#     return x
# return x
    
# print(cars())
    
# cars("tesla")

# def names_and_age(first_name = "Majili",second_name = "Kilo",age = 50):
#     print(f"{first_name}\n{second_name}\n{age}")
    
# def names_and_age(first_name = "Majili",second_name = "Kilo"):
#     print(f"{first_name}\n{second_name}")
    
# names_and_age("kiiza","kisa",67);

# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# integers = [3,4,7]

# for integer in integers:
#     if(integer%2 == 0):
#         print(f"{integer} is even")
#     elif(integer%2 == 1):
#         print(f"{integer} is odd")
        
        
# def sum_list(list_of_numbers):
#     sum = 0
#     for number in list_of_numbers:
#         sum = sum + number
#     return sum

# print(sum_list([7,9,9,8]))

# class User:
    
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
        

def varargs(arg1, *args):
    # print("Got ", arg1, " and ", args)
    for a in args:
        print(a)
    
varargs("one") # output: Got one and ()
varargs("one", "two") # output: Got one and ('two',)
varargs("one", "two", "three") # output: Got one and ('two', 'three')


    

