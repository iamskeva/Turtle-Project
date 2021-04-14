import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()
tim.shape("triangle")
tim.color("black")
tim.speed("fastest")
direction = [0, 90, 180, 270]

# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shapes_sides in range(3, 11):
#     tim.color(random.choice(colours))
#     tim.pensize(2)
#     draw_shapes(shapes_sides)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colours = (r, g, b)
    return colours


# for _ in range(4000):
#     tim.color(random_color())
#     tim.pensize(10)
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(3)


screen.exitonclick()