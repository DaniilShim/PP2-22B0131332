import math
import time

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)  # convert milliseconds to seconds
    result = math.sqrt(number)
    return result

number = int(input("Enter a number: "))
milliseconds = int(input("Enter the number of milliseconds to wait: "))

result = square_root_after_milliseconds(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

