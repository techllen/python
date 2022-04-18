from unittest import result


class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        self.result =+ num
        for number in nums:
            self.result += number
    	# your code here
        return self
    
    def subtract(self, num, *nums):
    	# your code here
        self.result =- num
        for number in nums:
            self.result =- number
        return self
# create an instance:
md = MathDojo()
# to test:

# TESTING ADD METHOD
# x = md.add(2)
# x = md.add(1,3)
# x = md.add(2,3,4,5,6)

# TESTING SUBTRACT METHOD
# x = md.subtract(2)
# x = md.subtract(-1,3)
# x = md.subtract(2,3,4,-5)

# CHAINING ALL METHODS
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

