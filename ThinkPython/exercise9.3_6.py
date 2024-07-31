"""
Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?

Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa”?

Exercise 9.5. Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?

Exercise 9.6. Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?

"""

class Solution:
    def __init__(self):
        pass 
    def exercise_9_3(self, word : str , forbidden_letter : list)-> bool:
        """avoids function modifed as exercise_9_3"""
        for letter in forbidden_letter:
            if letter in word:
                return False
        return True

        
    def exercise_9_4(self, word, available):
        """uses_only function modified as exercise_9_4
        If we find a letter in
        word that is not in available, we can return False."""
        for letter in word:
            if letter not in available:
                return False
        return True
    
    def exercise_9_5(self, word, required):
        """uses_all function modified as exercies_9_5"""
        for letter in required: 
            # return exercise_9_4(word, required)
            if letter not in word:
                return False
        return True
    
    def exercise_9_6(self, word):
        previous = word[0]
        for c in word:
            if c < previous:
                return False
            previous = c
        return True
    
    """An alternative is to use recursion:
    def is_abecedarian(word):
        if len(word) <= 1:
            return True
        if word[0] > word[1]:
            return False
        return is_abecedarian(word[1:])

    Another option is to use a while loop:
    def is_abecedarian(word):
        i = 0
        while i < len(word)-1:
            if word[i+1] < word[i]:
            return False
            i = i+1
        return True """



if __name__ == '__main__':
    sol = Solution()
    word = input("Enter the word: ")
    forbidden_letter = input("Enter the forbidden letter: ").split(" ") # a b c -> ['a', 'b', 'c']
    sol.exercise_9_3(word, forbidden_letter)
    
    available = input("Enter the available letter: ")
    sol.exercise_9_4(word, available)

    required = input("Enter the required letter")
    sol.exercise_9_5(word, required)

    sol.exercise_9_6(word)
