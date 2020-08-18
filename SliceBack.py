letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] # doesnt include 'a'
backwards2 = letters[::-1] 

print(backwards2)

# create a slice that = qpo
print(letters[16:13:-1])

# create a slice that = edcba
print(letters[4::-1])

# create a slice that = last 8 characters in reverse
print(letters[25:17:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])