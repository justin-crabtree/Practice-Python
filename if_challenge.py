name = input("What is your name? ")
age = int(input("How old are you, {}? ".format(name)))

# alt way of doing it
# if age >= 18 and age <= 30:
#   print("Welcome {}, to your vacation!".format(name))
# else:
#   print("Fuck off")

if age in range(18, 31):
  print("Welcome {}, to your vacation!".format(name))
else:
  print("Fuck off")