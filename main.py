import time
from turtle import Screen


from snake import Snake
from control import Control
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#2e2929")
screen.title("My Snake Game")
screen.tracer(0)

cobra = Snake()
comando = Control(cobra)
comida = Food()
score = Scoreboard()

screen.listen()
screen.onkey(comando.up, "Up")
screen.onkey(comando.down, "Down")
screen.onkey(comando.left, "Left")
screen.onkey(comando.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    cobra.move()

    # Detectar colisões com alimentos
    if cobra.head.distance(comida) < 15:
        comida.refresh()
        cobra.extend()
        score.increase_score()

    # Detectar colisões com parede
    if cobra.head.xcor() > 300 or cobra.head.xcor() < -300 or cobra.head.ycor() > 300 or cobra.head.ycor() < -300:
        score.reset()
        cobra.reset()

    # Detectar colisões com a calda
    for segment in cobra.segments:
        if segment == cobra.head:
            pass
        elif cobra.head.distance(segment) < 10:
            score.reset()
            cobra.reset()













screen.exitonclick()