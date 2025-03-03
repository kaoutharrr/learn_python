class MyClass:
    # constructor  
    # self is passed in to every method of a class
    # SELF IS LIKE THIS KEYWORD IN CPP
    def __init__(self, nums):
        # create member vars
        self.nums = nums
        self.size = len(nums)
    
    # self keyword required s param 
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()
    
nums = [1, 2, 3]
obj = MyClass(nums)

print(obj.getLength())         # Output: 3
print(obj.getDoubleLength())   # Output: 6
