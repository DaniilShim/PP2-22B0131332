def all_true(tup):
    return all(tup)

tup1 = (True, True, True)
tup2 = (True, False, True)
tup3 = ()
print(all_true(tup1)) # Output: True
print(all_true(tup2)) # Output: False
print(all_true(tup3)) # Output: True
