import turtle
turtle.bgcolor ("black")

t=turtle.Turtle ()
t.speed (2000)
t.pensize (2)

for i in range (500):
    t.pencolor ("teal")
    t.fd(i)
    t.rt(144)
    t.fd(i)
done()