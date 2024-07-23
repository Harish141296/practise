"""
Given an integer array nums, return an array answer sunch that answer[i] is equal to the product of all the elements of nums except nums[i]
the product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operator.
Example1: I/p: [ 1, 2, 3, 4]
          O/p: [24, 12, 8, 6]

"""
class Solution:
    def productExceptSelf(self, nums: list[int])-> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]

        return res 
    
num = [ 1, 2, 3, 4]
sol = Solution()
res = sol.productExceptSelf(nums = num)
print(res)

print("sUccess depends on the second letter   - J")