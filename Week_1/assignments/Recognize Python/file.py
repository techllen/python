num1 = 42 #variable declaration ,initialize Number
num2 = 2.3 #variable declaration ,initialize Number
boolean = True #variable declaration ,initialize Boolean
string = 'Hello World' #variable declaration ,initialize String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration ,initialize List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration ,initialize Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration ,initialize Tuple
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement

pizza_toppings.append('Mushrooms') #add value in a list
print(person['name']) #log statement
person['name'] = 'George' #accessing value in a dictionary
person['eye_color'] = 'blue' #accessing value in a dictionary
print(fruit[2]) #log statement

if num1 > 45:#conditions
    print("It's greater") #log statement
else:
    print("It's lower") #log statement

if len(string) < 5: #conditions and length check
    print("It's a short word!") #log statement
elif len(string) > 15:
    print("It's a long word!") #log statement
else:
    print("Just right!") #log statement

for x in range(5):#for loop
    print(x)   #log statement
for x in range(2,5): #for loop
    print(x)  #log statement
for x in range(2,10,3): #for loop
    print(x)  #log statement
x = 0 #variable declaration
while(x < 5): #while loop
    print(x) #log statement
    x += 1

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value

print(person) #log statement
person.pop('eye_color') #delete value
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #condition
        continue
    print('After 1st if statement')  #log statement
    if topping == 'Olives': #condition
        break  

def print_hello_ten_times(): #function
    for num in range(10):  #for loop
        print('Hello') #log statement

print_hello_ten_times() #calling a non parameterized function

def print_hello_x_times(x): #function
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_times(4) #calling a calling a function by passing an argument

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #calling a non parameterized function
print_hello_x_or_ten_times(4) #calling a function by passing an argument

#comment multiline
"""
Bonus section
"""

#comments single line

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)