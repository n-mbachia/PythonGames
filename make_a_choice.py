#!/usr/bin/python3

print("The game requires you to make a choice as presented by the questions")
print("------****------*****------******---*******------*****------****------")
print("Win a gold coin based on the choices you make")
print("------****------*****------******---*******------*****------****------")

# REQUEST USER FOR NAME
name = input("Type your name: ")

print("Welcome", name, "to this adventure!")

# THIS GAME HAS A SERIES OF QUESTIONS FOR USER TO ANSWER GUIDED BY PARENTHESIS

answer = input("You are on a dirt road,its evening and the sun is already setting. You can only go left or right, which way will you go? (left or right) ",).lower()
print("------****------*****------******---*******------*****------****------")
if answer == "left":
    answer = input("You come to a river,you can either walk around it or swim across. What would you choose, (walk or swim)? ",)

    if answer == "swim":
        print("Unfortunately you just entered a crocodile infested river and have been devoured by the crocodiles!")

    elif answer == "walk":
        print("You been walking for along time, it is already dark Gameover")

elif answer == "right":
    answer = input("You been walking and come to a bridge, it looks wobbly.Do you (cross or go back)? ")
    if answer == "go back":
        print("You just choose to go back! Gameover!")
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you say hello or not ?")
        if answer == "not":
            print("You ignored the stranger, you loose. Gameover!")

        elif answer == "hello":
            print("You talk to the stranger,and he gives you a gold coin. You win :-)")

        else:
            print("Not a valid answer.You loose!")
    else:
        print("Not a valid answer. You loose")
else:
    print("Not a valid answer. You loose")
print("------****------*****------******---*******------*****------****------")

print("Thank you for trying", name)
