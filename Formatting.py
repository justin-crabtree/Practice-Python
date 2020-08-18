for i in range(1, 13):
  print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))    # {0:2} the :2 is the width, in this case it's 2 characters

print()

for i in range(1, 13):
  print("No. {0:2} squared is {1:>3} and cubed is {2:^4}".format(i, i ** 2, i ** 3)) # the < symbol left aligns the grid, > is right, and ^ centers

print("Pi is approx {0:12}".format(22 / 7))
print("Pi is approx {0:12f}".format(22 / 7))
print("Pi is approx {0:12.50f}".format(22 / 7))
print("Pi is approx {0:52.50f}".format(22 / 7))
print("Pi is approx {0:62.50f}".format(22 / 7))
print("Pi is approx {0:72.50f}".format(22 / 7))