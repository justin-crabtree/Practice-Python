age = 28

print("My age is {0} years".format(age))    # The {0} is replaced with the first format value in the list (age)

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
  .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, June: {1}, Jul: {2}, Aug: {1}, Sep: {2}, Oct: {1}, Nov: {2}, Dec: {1}"
  .format(28, 30, 31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {1}
Sep: {2}
Oct: {1}
Nov: {2}
Dec: {1}""".format(28, 30, 31))

