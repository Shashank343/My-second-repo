# Let's create a game called Snake,Water & Gun and play with computer

# Let's import random to let the computer choose any one number
import random
Computer = random.randint(1, 3)

# Enter your name to play the game
Name = input("Enter your name to the play: ")

# Let's explain the rules to the player
print(f"!!Hello, {Name} Here are some rules to play the game:-")
r = "1)Choose a number between 1 to 3\n2) 1-Snake\t2)2-Water \t3)3-Gun\n3)If you enter any other key then computer wins the game"
print(r)

# Let's take the input in form of numbers form the player to play the game 
User = int(input("Enter a number: "))

# Let's compare the values given by the computer & User and decide who wins 
if User > Computer:
    print("Yahoo... You have won the game")

elif Computer > User:
    print("Sorry! Computer won the game")

elif Computer == User:
    print("This Game is draw!!! you and computer choosen same option")

else:
    print("Your have given the wrong input pls see and type the above option's")