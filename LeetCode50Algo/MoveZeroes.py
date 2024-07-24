"""
Algorithm Explanation Step wise:
Step 1: Start 
Step 2: Instead of focusing on zero, lets find the non_zero and move it to the Zero's position
Step 3: Initialize J(any variable) = 0, idea of this is, to move the first non zero element to this j's position
Step 4: Loop the length of the array with range function to swap the elements of the array by index position
Stpe 5: If arr[iter] is not zero then assign it to arr[j] = arr[iter], then inc j by 1.
Step 6: once the loop completed, all the non zero elements present in the left side.
Step 7: Now need to replace the remaining j - len(arr) as zero
Step 8: loop through num with range(j - len(arr))
Step 9: arr[num] = 0 # will moved zero to the right side
Step 10: End

In short, one variable will be iterated by one only if that is non zero, for swaping the data simultaneously and keep track of non-zero total length to add the remaining with zeroes. 
"""
class Solution:
    def moveZeroes(self, arr):
        j = 0
        for num in range(len(arr)):
            if arr[num] != 0:
                arr[j] = arr[num]
                j += 1
        for num in range(j , len(arr)):
            arr[num] = 0

        return arr     

input_arr = [0, 1, 0, 4, 0, 0, 3]
sol = Solution()
print(sol.moveZeroes(input_arr))


print("sUccess depends on the second letter.   - J")