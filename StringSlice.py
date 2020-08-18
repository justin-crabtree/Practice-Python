parrot = "Norwegian Blue"

# slice is up to but not including the last index
print(parrot[0:6])    # Norweg
print(parrot[3:5])    # we
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])  # Blue
print(parrot[10:])    # Blue

print(parrot[:6])     # Starts at the first index and goes until index 6
print(parrot[6:])     # Starts at index 6 and goes to the end of the string

print(parrot[:6] + parrot[6:])

print(parrot[:])      # doesnt have a start or stop value, so it prints the whole string 

# Negative Slicing
print(parrot[-4:-2])    # starts at index -4 and prints up to index -2
print(parrot[-4:12])    # starts at index -4 and prints up to index 12
print(parrot[-14:-8])   # Norweg

# Step Slicing
print(parrot[0:6:2])    # starts at index 0 and prints up to index 6 in increments of 2
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
number2 = "9,223;372:036 854,775;807"
print(number[1::4])     # starts at index 1 and slices every 4th character

seperators = number2[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number2).split()
print([int(val) for val in values])
