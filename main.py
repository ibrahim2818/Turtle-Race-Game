from turtle import Turtle, Screen
import random

is_race_on= False
screen = Screen()
screen.setup(width=500, height=400)
user_bet= screen.textinput(title='Make a bet', prompt=" which colour will win?")
print(user_bet)
ypos=[-70, -40, -10, 20, 50, 80]
color= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle=[]
for i in range(6):
    tim = Turtle(shape='turtle')
    tim.color(color[i])
    tim.penup()
    tim.goto(x=-230, y=ypos[i])
    all_turtle.append(tim)


if user_bet:
    is_race_on= True

while is_race_on:
    for i in all_turtle:
        if i.xcor()>230:
            is_race_on= False
            winColor= i.pencolor()
            if user_bet == winColor:
                print(f'you win, {user_bet} wins the race')
                break
            else:
                print(f'you lose, {winColor} wins the race')
                break
        distance = random.randint(0,10)
        i.forward(distance)



screen.exitonclick()
