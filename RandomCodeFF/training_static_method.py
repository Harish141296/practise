
class MathUtil:
    # @staticmethod
    def add(a, b):
        return a + b
    
    # @staticmethod
    def sub(a, b):
        return a - b 
    
add_result = MathUtil.add(3, 5) # Output: 8
sub_result = MathUtil.sub(10, 3) # Output: 7

print(add_result)
print(sub_result)

###############################################################################

class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b 
    
add_result = MathUtil.add(3, 5) # Output: 8
sub_result = MathUtil.sub(10, 3) # Output: 7

print(add_result)
print(sub_result)


###############################################################################


class MathUtil:
    # @staticmethod
    def add(a, b):
        return a + b

    # @staticmethod
    def sub(a, b):
        return a - b

    # @staticmethod
    def multiply(a, b):
        return a * b

# Utility methods
print(MathUtil.add(3, 5))  # Output: 8
print(MathUtil.sub(10, 3))  # Output: 7
print(MathUtil.multiply(4, 5))  # Output: 20

class AdvancedMathUtil(MathUtil):
    # @staticmethod
    def square(a):
        return a * a

# Still works fine
print(AdvancedMathUtil.add(2, 3))  # Output: 5
print(AdvancedMathUtil.square(4))  # Output: 16

###############################################################################

class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

# Utility methods
print(MathUtil.add(3, 5))  # Output: 8
print(MathUtil.sub(10, 3))  # Output: 7
print(MathUtil.multiply(4, 5))  # Output: 20

class AdvancedMathUtil(MathUtil):
    @staticmethod
    def square(a):
        return a * a

# Still works fine
print(AdvancedMathUtil.add(2, 3))  # Output: 5
print(AdvancedMathUtil.square(4))  # Output: 16

###############################################################################

