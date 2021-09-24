import turtle
home=turtle.Turtle()
turtle.title("Home")

#home.hideturtle()
home.begin_fill()
for i in range(4):
    home.forward(200)
    home.left(90)
home.fillcolor("yellow")
home.end_fill()

    
home.begin_fill()     
home.goto(50,0)
home.left(90)
home.forward(200)
home.left(30)

home.forward(50)


home.goto(0,200)


home.up()
home.begin_fill()
home.goto(25,245)
home.right(120)
home.down()
home.forward(180)
home.left(-80)
home.forward(45)
home.left(266)
home.forward(16)
home.fillcolor("brown")
home.end_fill()
home.up()

home.home()
home.goto(10,0)
home.begin_fill()
home.down()
home.left(90)
home.forward(50)
home.right(90)
home.forward(30)
home.right(90)
home.forward(50)
home.fillcolor("black")
home.end_fill()
home.up()
home.home()

home.goto(150,100)
home.begin_fill()
home.pendown()
for i in range(4):
    home.forward(40)
    home.left(90)
home.fillcolor("black")
home.end_fill()
home.up()
home.home()
home.goto(25,210)
home.down()
home.begin_fill()
home.circle(4)
home.fillcolor("black")
home.end_fill()

home.hideturtle()

 
