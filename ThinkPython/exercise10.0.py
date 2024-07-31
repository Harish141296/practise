def reverse_int(age):
    reversed_number = ''
    length = len(str(age))
    while length >= 0 and age != 0:
        reminder = age % 10 # 0
        quotient = age // 10 # 1
        reversed_number += str(reminder)
        length -= 1
    return reversed_number

print(reverse_int(10))
print(reverse_int(100))