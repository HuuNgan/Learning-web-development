#   Dictionaries are used in order to map certain values on to other values
#   They're often used when we want to try and indicate some sort of
# relationship between a former value and a latter value.

ages = {"Alice": 22, "Bob": 27}    # Alice is key and 22 is value
ages["Charlie"] = 30               # Add Charlie to dictionary
ages["Alice"] += 1                 # Increase value (age) of Alice by 1

print(ages)
