"""calculator app"""
class Calculator:
    def __init__(self, user_input):
        self.num1 = user_input[0] 
        self.num2 = user_input[1] 
    
    def add(self):
        return self.num1 + self.num2 

    def sub(self):
        return self.num1 - self.num2 
    
    def mul(self):
        return self.num1 * self.num2 
    
    def div(self):
        return self.num1 / self.num2 # which return float division 
    
    def integerdiv(self):
        return self.num1 // self.num2 # integer division
    
    def modulodiv(self):
        return self.num1 % self.num2 # integer division
    
    def __del__(self):
        # this is the destructor will execute at the end of this class .
        print("program ends here.")

user_commands = input('Enter the commands (add, sub, mul, div, integerdiv, modulodiv) with linespace: ').split(' ')
user_input = list(map(int, input("Enter the two numbers to perform operation :").split(' ')))


cal = Calculator(user_input)
answers = ['***************************************************']
for command in user_commands:
    if command == 'add' or command == '+' or command == 'addition':
        answers.append(f"Addition of two numbers {cal.num1} and {cal.num2} =  {cal.add()}")

    elif command == 'sub' or command == '-' or command == 'subtraction':
        answers.append(f"Subtraction of two numbers {cal.num1} and {cal.num2} =  {cal.sub()}")

    elif command == 'mul' or command == '*' or command == 'multiplication':
        answers.append(f"Multiplication of two numbers {cal.num1} and {cal.num2} =  {cal.mul()}")

    elif command == 'div' or command == '/' or command == 'division':
        answers.append(f"Division of two numbers {cal.num1} and {cal.num2} =  {cal.div()}")

    elif command == 'integerdiv' or command == '//' or command == 'integerdivision':
        answers.append(f"Integerdivision of two numbers {cal.num1} and {cal.num2} =  {cal.integerdiv()}")

    elif command == 'modulodiv' or command == '%' or command == 'modulodivision':
        answers.append(f"Modulodivision of two numbers {cal.num1} and {cal.num2} =  {cal.modulodiv()}")
    else:
        answers.append("Unknown commands")

answers.append('***************************************************')
for answer in answers:
    print(answer)
print("\n sUccess depends on the second letter.   -JH")


"""
Sample Input : 
Enter the commands (add, sub, mul, div, integerdiv, modulodiv) with linespace: add sub mul div integerdiv modulodiv success
Enter the two numbers to perform operation : 24 12
Sample Output: 
***************************************************
Addition of two numbers 24 and 12 =  36
Subtraction of two numbers 24 and 12 =  12
Multiplication of two numbers 24 and 12 =  288
Division of two numbers 24 and 12 =  2.0
Integerdivision of two numbers 24 and 12 =  2
Modulodivision of two numbers 24 and 12 =  0
Unknown commands
***************************************************
"""