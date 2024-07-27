# Structural Patterns 

# Facade - An outward appearence that is used to conceal a less pleasant or credible reality

class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2 # Array of capacity = 2 
    
    # Insert n in the last position of the array
    def pushback(self, n): 
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity 
        # complement
        for i in range(self.length):
            pass