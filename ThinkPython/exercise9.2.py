"""
Exercise 9.2. In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to
do.
In fact, it is difficult to construct a solitary thought without using that most common symbol. It is
slow going at first, but with caution and hours of training you can gradually gain facility.
All right, I’ll stop now.
Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
it.
Write a program that reads words.txt and prints only the words that have no “e”. Compute the
percentage of words in the list that have no “e”.
"""
def has_no_e(word: str) -> bool:
    # e = 0
    # for letter in word: # O(n)
    #     if letter == 'e':
    #         e += 1
    initial_count = len(word)
    replaced_count = len(word.replace('e',''))
    e_times = initial_count - replaced_count
    # print(e_times) # O(1)
    return e_times 


if __name__ == '__main__':
    example_input_words = ['counterdemonstrations','hyperaggressivenesses','microminiaturizations']
    word = input("Enter the word to check 'e' present in it or not: ") # ip = 
    if e:=has_no_e(word): # ':=' this Erlang will evaluate the function as well as store the result in the variable at condition checking time.
        print(f"The word {word} has count of : {e} e in it ")
        
    else:
        print(f"The word {word} has no e in it.")