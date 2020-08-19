# for i in range(1, 13):
#   print("The number {} squared is {} and cubed is {:4}".format(i, i ** 2, i **3))
# print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
#print(age)

if age >= 18:
  print("You're old enough to vote!")
  print("Please put an X in the box")
else:
  print("Please come back in {0} years to vote!".format(18 - age))
