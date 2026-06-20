import random 
random_ = random.randint(1,100)

while True:
  guess_ = int(input("Guess the Correct number (1 - 100) : "))
  
  if(guess_ == random_):
    print(" Congratulations ! You Guessed a correct number.")
    break
  elif(guess_ < random_):
    print("You Guessed too low")
  elif(guess_ > random_):
    print("You Guessed too high")
  else :
    print("Enter Valid number between 1 to 100")
