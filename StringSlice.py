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