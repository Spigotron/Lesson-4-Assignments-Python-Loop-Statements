import random

items = ["ball", "cup", "stick"]
random_item = random.choice(items)
print(random_item)
player_guess = input("Guess an item. ")
if player_guess == random_item:
    print("Congratulations! You guessed correctly!")
else:
    print("Sorry, wrong guess!")