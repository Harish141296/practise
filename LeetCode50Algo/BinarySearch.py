"""
Algorithm: 
Step1: initialize two pointers left = 0 and right = len(array) -1
Step2: Start while loop left <= right, loop runs len(array) times
Step3: find the midpoint of the array.
Step4: if array[mid] == target then return mid
Step5: elif array[mid] < target -> means mid is lesser than the target
       then increase the left pointer to mid + 1
Step6:elif array[mid] > target -> means mid is greater than the target
      then decrease the right pointer to mid - 1
Step7: If target not found then simple return -1 -> means not found.
"""

class Solution:
    def binarySearch(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                #arr[mid] > target:
                right = mid - 1
        return -1
    
arr = [1,2,3,4,5,6]
tgt = 6

sol = Solution()
result = sol.binarySearch(arr=arr, target=tgt)
if result != -1:
    print(f"The target found at the index: {result}")
else:
    print("The target not found in the given array.")


print("sUccess depends on the second letter.   - J")