def countdown(number):
    countdown_list = []
    for count in range(number,-1,-1):
        countdown_list.append(count)
    return  countdown_list

print(countdown(5))

def print_and_return(two_number_list):
    for index in range(len(two_number_list)):
        if index == 0 :
            print(two_number_list[index])
        else:
            return two_number_list[index]
        
print(print_and_return([1,2]))

def first_plus_length(my_list):
    return len(my_list) + my_list[0]

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(input_list):
    if len(input_list) > 1:
        second_value = input_list[1]
        greater_than_second_value_list = []
        for index in range(len(input_list)):
            if input_list[index] > second_value:
                greater_than_second_value_list.append(input_list[index])
        print(len(greater_than_second_value_list))
    else:
        greater_than_second_value_list = False
    return greater_than_second_value_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5]))

def this_length_that_value(size,value):
    generated_list = []
    for index in range(size):
        generated_list.append(value)
    return generated_list

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))
