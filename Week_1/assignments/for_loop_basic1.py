# 1.Basic - Print all integers from 0 to 150.
for number in range(0,151):
    print(number)


# 2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for multiple_of_five in range(5,1001,5):
    print(multiple_of_five)

# 3.Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" 
# instead. If divisible by 10, print "Coding Dojo"
for integer in range(1,101):
    if(integer%10 == 0):
        print("Coding Dojo")
    elif(integer%5 == 0):
        print("Coding")
    else:
        (print(integer))

#4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0

for integer in range(0,500000):
    sum=sum+integer
print(sum)

#5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours
for positive_number in range(2018,0,-4):
    print(positive_number)

#6.Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going 
# through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, 
# highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 10
mult = 3

for integer in range(lowNum,highNum):
    if(integer%mult == 0):
        print(integer)

