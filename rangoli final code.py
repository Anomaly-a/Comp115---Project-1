import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(750, 750)
turtle.title("Rangoli")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

def move_to(angle, distance):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(distance)

def petal(angle, size, outline, fill):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    for _ in range(2):
        t.circle(size, 60)
        t.left(120)
    t.end_fill()

points = []
angle = 0  # running total
for _ in range(24):
    move_to(angle, 290)
    points.append(t.pos())
    angle += 360 / 24

t.color("gold")
t.pensize(2)
for i in range(24):
    t.penup()
    t.goto(points[i])
    t.pendown()
    t.goto(points[(i + 9) % 24])

t.pensize(2)
layers = [(24, 230, "gold", ["black", "orange"]),
    (16, 150, "gold", ["black", "black"]),
    (12, 80, "black", ["white", "gold"]),
    (8, 50, "orange", ["gold", "black"])]

for petals, size, outline, fills in layers:
    angle = 0  # running total
    for i in range(petals):
        petal(angle, size, outline, fills[i % len(fills)])
        angle += 360 / petals

angle = 0
for i in range(48):
    move_to(angle, 262)
    if i % 2 == 0:
        t.dot(14, "gold")
    else:
        t.dot(8, "white")
    angle += 360 / 48

t.penup()
t.goto(0, 0)
t.dot(32, "orange")
t.dot(22, "black")
t.dot(10, "white")


turtle.done()
