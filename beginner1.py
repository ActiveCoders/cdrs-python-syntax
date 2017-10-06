# Python comments start with the hashtag
# Title: beginner1
# Description: start coding in Python
# Purpose: demo some essential Python code syntax
# Version: 0.1
# Good use of comments can earn you easy points

print("Hello World!")

# create some variables - string, integer, boolean
playerName = "Pinball Wizard"
score = 0
gameOver = False
# change the above score to test the below if statements

# print some messages to the screen (Python console)
print("Welcome " + playerName)
print("Your score is:")
print(score)
print("But is the game over yet?")
print(gameOver)

# the conditional if statement examples
if gameOver:
    print("The game is over!")
    print("And your score was:")
    print(score)
else:
    print("The game is not over yet!")
    print("Your score so far is:")
    print(score)

# adding elif (else if) to the Python if statement
if (score==0):
    print("You have scored nothing")
elif (score>0 and score<10):
    print("You've started scoring points")
elif (score>=10):
    print("You have a high score")
else:
    print("Error - Negative score")

# conditional loop using while
while (score<10):
    print("Stay in this loop until score goes to 10 or above")
    print(score)
    print("Here are 2 points for doing nothing!")
    score = score + 2
print("I'm outside the while loop and your score is now:")
print(score)
