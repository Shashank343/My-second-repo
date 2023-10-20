# Let's create a game called Snake,Water & Gun and play with computer

# Let's import random to let the computer choose any one number
import random
random.randint(1, 3)

# Enter your name to play the game
Name = input("Enter your name to the play: ")

# Let's explain the rules to the player
print(f"!!Hello, player {Name} Here are some rules to play the game:-")
r = "1)Choose a number between 1 to 3\n2) 1-Snake\t2-Water \t3)3-Gun\n3)If you enter any other key then computer wins the game"
print(r)

# Let's take the input in form of numbers form the player to play the game 
n = int(input("Enter a number: "))

# Let's compare the values given by the computer & User and decide who wins 