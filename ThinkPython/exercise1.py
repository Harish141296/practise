""" 
Welcome onBoard to this overall walkthrough of exercises that were covered in ThinkPython-V2 book, I wish you all the best in your coding Journey. 
exercise1 will cover ch1 - ch5
"""
"""
What is a program?
A program is a sequence of instructions that specifies how to perform a computation. 
Input -> math -> conditional execution -> repetition-> Output

"""

class chapter1:
    def __init__(self):
        print("fastern your seat belt coders.")
    def workingout_problems(self):
        # Since python is a dynamic programming, variable type will be defined only at the runtime.
        print('1' + '4' + '3') # string addition
        print(1 + 4 + 3) # integer addition
        print(144 - 1) # subtraction
        print(11 * 13) # multiplication
        print(286 / 2) # floating point division 
        print(143 ** 2 - 20306) # ** - exponential x ^ y

        # type() will return the type of anything that passed within.
        print(type(143)) # <class 'int'>

        print(type('143')) # <class 'str'>

        print(type(143.0)) # <class 'float'>

        print(1,000,000) # will result in (1, 0, 0)
        # instead use '_' 
        print(1_000_000)

        """
        Glossary
        problem solving: The process of formulating a problem, finding a solution, and expressing it.
        high-level language: A programming language like Python that is designed to be easy for humans to read and write.
        low-level language: A programming language that is designed to be easy for a computer to run; also called “machine language” or “assembly language”.
        portability: A property of a program that can run on more than one kind of computer.
        interpreter: A program that reads another program and executes it
        prompt: Characters displayed by the interpreter to indicate that it is ready to take input
        from the user.
        program: A set of instructions that specifies a computation.
        print statement: An instruction that causes the Python interpreter to display a value on the screen.
        operator: A special symbol that represents a simple computation like addition, multiplication, or string concatenation.
        value: One of the basic units of data, like a number or string, that a program manipulates.
        type: A category of values. The types we have seen so far are integers (type int), floating point numbers (type float), and strings (type str).
        integer: A type that represents whole numbers.
        floating-point: A type that represents numbers with fractional parts.
        string: A type that represents sequences of characters.
        natural language: Any one of the languages that people speak that evolved naturally.
        formal language: Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs; all programming languages are formal languages.
        token: One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language.
        syntax: The rules that govern the structure of a program.
        parse: To examine a program and analyze the syntactic structure.
        bug: Anerror in a program.
        debugging: The process of finding and correcting bugs.
        """

        try:
            print("print('we left closing paranthesis' \
                or unclosed paranthesis \
                or multiple operators inbetween operands(4++3) \
                or Leading Zeros 043 \
                or two operand with no operator 4 3 \
                -> will throw error")

        except Exception as e:
            print(e)

    def exercise(self):
        # How many seconds are there in 42minutes 42 seconds
        minute = 60
        print(f"Overall seconds => 42 x {minute} + 42 second = {42 * minute + 42}")
        # How many miles are there in 10 Kilometers? Hint: there are 1.61 Kilometers in 1 mile
        mile = 1.61 # kill
        kilometer = 1 / mile
        print(f"one Mile = {mile} kilometer, one kilometer = {kilometer} miles, so 10 kilometer = {10 * kilometer}")
        #  If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
        distance = 10
        kilometer = 10 / mile
        seconds = 42 * 60 + 42 
        speed = kilometer  / seconds 
        print(f"average speed = {speed}")


if __name__ == '__main__':
    ch1 = chapter1()
    ch1.workingout_problems()
 


