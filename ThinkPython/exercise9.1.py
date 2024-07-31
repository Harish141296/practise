"""
 Write a program that reads words.txt and prints only the words with more than 20
 characters (not counting whitespace).
"""

def jerry_h(file_path):
    with open(file_path,'r') as f:
        words = f.readlines()

    cleaned_words = [word.replace('\n','') for word in words]
    print(cleaned_words)
    return cleaned_words

if __name__ == '__main__':
    words = jerry_h(file_path = '/workspaces/practise/ThinkPython/words.txt')
    for word in words:
        if len(word.replace(' ','').strip()) > 20:
            print(word)

    print("sUccess depends on the second letter.   -J ")