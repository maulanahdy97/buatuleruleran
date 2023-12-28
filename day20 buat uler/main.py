import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Uler-Uleran")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.moveup, "Up")
screen.onkey(snake.movedown, "Down")
screen.onkey(snake.moveleft, "Left")
screen.onkey(snake.moveright, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.goto(food)

    #Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collission with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on : False
            scoreboard.game_over()

screen.exitonclick()
