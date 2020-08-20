answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())         

if guess != answer:
  if guess < answer:
    print("One more try, guess higher")
  else:
    print("One more try, guess lower")
  guess = int(input())
  if guess == answer:
    print("Correct!")
  else:
    print("Incorrect!")
else:
  print("Beginners luck...")


# if guess < answer:    
#   print("One more try, guess higher")
#   guess = int(input())
#   if guess == answer:
#     print("Well done, you guessed it!")
#   else:
#     print("Sorry, you guessed incorrectly") 
# elif guess > answer:
#   print("One more try, guess lower")
#   guess = int(input())
#   if guess == answer:
#     print("Well done, you guessed it!")   
#   else:
#     print("Sorry, you guessed incorrectly")
# else:
#   print("Correct!")

