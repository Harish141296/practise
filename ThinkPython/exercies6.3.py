"""
is_palindrome(word) # madam
"""

class Solution:
    def __init__(self, word):
        self.word = word

    def is_palindrome(self):
        i, j = 0, len(self.word) - 1
        while i < j:
            if self.word[i] != self.word[j]:
                return False 
            i += 1
            j -= 1
        return True 
    
word = input("Enter the word to check the palindrome: ")
sol = Solution(word)
if sol.is_palindrome():
    print(f"Given word {word} is palindrome.")
else:
    print(f"Given word {word} is not a palindrome.")