activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
  # casefold() used to check for instance regardless of case sensitive
  print("But I want to go to the cinema")