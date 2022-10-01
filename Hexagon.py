import turtle 

t=turtle.Turtle()
colors = ["red","purple", "blue","green", "yellow", "orange"]
t.hideturtle()

u=turtle.Screen()
u.bgcolor("black")

for x in range (360):
    t.color(colors[x%6])
    t.width(int(x / 100+1))
    t.forward(x)
    t.left(59)
    t.speed(15)
    
turtle.done()
















