
class Solution:
    def maxSum(self, input_arr, k):
        
        length = len(input_arr)
        if length <= k:
            return -1

        window_sum = sum([input_arr[num] for num in range(k)])
        max_sum = window_sum

        for num in range(length - k):
            window_sum = window_sum - input_arr[num] + input_arr[num+k]
            max_sum = max(window_sum, max_sum)
        
        return max_sum


sol = Solution()
input_arr = [80, -50, 90, 100]
k = 2 # limitation
result = sol.maxSum(input_arr, k)
if result == -1:
    print("Invalid Operation")
else:
    print(f"result is: {result}")
# print(result)


print("sUccess depends on the second letter.   - J")