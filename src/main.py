from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
x_pos = [0, -20, -40]
all_snakes = []

snake = Turtle("square")
snake.color("white")

for snake_idx in range(0,3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(x=x_pos[snake_idx], y=0)
    all_snakes.append(snake)




screen.exitonclick()