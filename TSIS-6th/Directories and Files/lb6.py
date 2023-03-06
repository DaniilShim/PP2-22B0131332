import string
import os

alphabet = string.ascii_uppercase

for letter in alphabet:
    filename = letter + ".txt"
    with open(filename, "w") as f:
        pass
