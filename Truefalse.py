day = "Saturday"
temp = 90
raining = True

if day == "Saturday" and temp > 80 or not raining:
  print("Go swimming")
else:
  print("Stay inside and play video games")

if 0:
  print("True")
else:
  print("False")

name = input("Please enter your name ")
# if name:
if name != "":
  print("Hello, {}".format(name))
else:
  print("Are you the man with no name?")