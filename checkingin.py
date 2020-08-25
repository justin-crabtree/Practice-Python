parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
  print("{} is in the word {}".format(letter, parrot))
else:
  print("{} is NOT in word {}".format(letter, parrot))