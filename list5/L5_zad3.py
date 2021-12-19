from turtle import *


def hilbert_curve(rank, step, angle=90):
    if rank <= 0:
        return

    left(angle)
    hilbert_curve(rank-1, step, -angle)

    forward(step)
    right(angle)
    hilbert_curve(rank-1, step, angle)

    forward(step)
    hilbert_curve(rank-1, step, angle)

    right(angle)
    forward(step)
    hilbert_curve(rank-1, step, -angle)

    left(angle)


def draw_hilbert_curve(rank=4, step=10):
    if not (isinstance(rank, int) and isinstance(step, int)):
        raise TypeError("Wrong input")

    screen = Screen()

    speed('fastest')
    title("Hilbert Curve")

    hilbert_curve(rank, step)

    screen.exitonclick()


if __name__ == "__main__":
    draw_hilbert_curve(3, 10)