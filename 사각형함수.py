import turtle
t=turtle.Turtle()
t.shape("turtle")
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
        t.up()
        t.goto(length*2,0)
        t.down()
        
square(100)
square(100)
square(100)

