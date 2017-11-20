import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
length = int(input("How Long?"))
sides = int(input("How many sides?"))
for i in range(sides):
    alex.forward(length)
    alex.left(360/sides)











wn.mainloop