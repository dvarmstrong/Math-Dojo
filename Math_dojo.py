#Practice creating a class and creating new instances
# Practice chaining methods
# Practice writing flexible functions that can take a varying number of arguments


class MathDojo:
    def __init__(self):
        self.result = 0 
        
    def add(self, num, *nums):
        self.result += num 
        for i in nums:
            self.result += i 
        return self
        # for i in num:
        #     print(x + sum(nums))
        #     return self
    def sub(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i 
        return self



md = MathDojo()
x = md.add(5).add(6,2,3).sub(6,2,3).result 
print(x)

