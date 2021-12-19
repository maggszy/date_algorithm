from turtle import *


def koch_curve(rank, length_step, angle=60):
    if rank == 0:
        forward(length_step)
        return
    koch_curve(rank - 1, length_step/3)
    left(angle)
    koch_curve(rank - 1, length_step/3)
    right(180-angle)
    koch_curve(rank - 1, length_step/3)
    left(angle)
    koch_curve(rank - 1, length_step/3)


def draw_koch_curve(rank=3, length_step=300):
    screen = Screen()

    speed('fastest')
    title("Koch Curve")

    penup()
    backward(length_step/2)
    pendown()

    koch_curve(rank, length_step)

    screen.exitonclick()


def draw_koch_snowflake(rank=4, length_step=300):
    screen = Screen()

    speed('fastest')
    title("Koch Snowflake")

    penup()
    backward(length_step / 2)
    pendown()

    for i in range(rank-1):
        koch_curve(rank, length_step)
        right(120)

    screen.exitonclick()


if __name__ == "__main__":
    # draw_koch_curve()
    draw_koch_snowflake()