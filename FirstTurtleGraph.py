
import turtle
wn = turtle.Screen()
sailesh = turtle.Turtle()
sailesh.pensize(5)

sailesh.speed("normal")




sailesh.left(217)
sailesh.up()
sailesh.forward(450)

sailesh.down()
sailesh.left(143)
sailesh.color("black","blue")
sailesh.begin_fill()
sailesh.forward(700)
sailesh.left(90)
sailesh.forward(400)
sailesh.left(90)
sailesh.forward(700)
sailesh.left(90)
sailesh.forward(400)
sailesh.end_fill()

sailesh.left(90)
sailesh.forward(30)
sailesh.left(90)
sailesh.forward(200)
sailesh.right(90)
sailesh.forward(130)

sailesh.back(130)
sailesh.forward(65)
sailesh.up()
sailesh.left(90)
sailesh.forward(100)
sailesh.down()
sailesh.pensize(2)
sailesh.color("black","yellow")
sailesh.begin_fill()
sailesh.circle(25)
sailesh.end_fill()    #end point of sun

sailesh.color("black")
sailesh.right(180)
sailesh.up()
sailesh.forward(100)
sailesh.left(90)
sailesh.forward(65)
sailesh.right(90)
sailesh.down()
sailesh.pensize(5)
sailesh.forward(25)
sailesh.up()
sailesh.right(90)

sailesh.forward(25)
sailesh.down()
sailesh.pensize(2)
sailesh.color("black","yellow")
sailesh.begin_fill()
sailesh.forward(80)
sailesh.left(90)
sailesh.forward(35)
sailesh.left(90)
sailesh.forward(80)
sailesh.left(90)
sailesh.forward(35)
sailesh.end_fill()
sailesh.left(90)
sailesh.forward(40)
sailesh.left(90)
sailesh.forward(35)
sailesh.left(90)
sailesh.forward(40)
sailesh.left(90)
sailesh.forward(35)

sailesh.up()
sailesh.right(90)
sailesh.forward(25)
sailesh.down()
sailesh.pensize(5)
sailesh.right(90)
sailesh.forward(55)

sailesh.right(90)
sailesh.up()
sailesh.forward(25)
sailesh.down()
sailesh.pensize(2)                #point
sailesh.color("black","yellow")
sailesh.begin_fill()
sailesh.forward(80)
sailesh.left(90)
sailesh.forward(35)
sailesh.left(90)
sailesh.forward(80)
sailesh.left(90)
sailesh.forward(35)
sailesh.end_fill()
sailesh.left(90)
sailesh.forward(40)
sailesh.left(90)
sailesh.forward(35)
sailesh.left(90)
sailesh.forward(40)
sailesh.left(90)
sailesh.forward(35)

sailesh.color("black")
sailesh.right(90)
sailesh.up()
sailesh.forward(25)
sailesh.down()
sailesh.pensize(5)
sailesh.right(90)
sailesh.forward(50)

sailesh.right(90)
sailesh.up()
sailesh.forward(40)
sailesh.down()
sailesh.pensize(5)


sailesh.color("black","silver")
sailesh.begin_fill()
sailesh.forward(50)
sailesh.left(90)
sailesh.forward(70)
sailesh.left(90)
sailesh.forward(50)
sailesh.left(90)
sailesh.forward(70)
sailesh.end_fill()

sailesh.left(90)
sailesh.forward(25)
sailesh.left(90)
sailesh.forward(70)

sailesh.left(90)
sailesh.forward(65)
sailesh.left(90)
sailesh.forward(70)    #end point of first house



sailesh.forward(30)      #starting of new house
sailesh.up()
sailesh.right(90)
sailesh.forward(30)
sailesh.down()
sailesh.forward(20)   #try

sailesh.color("black","yellow")
sailesh.pensize(30)
sailesh.begin_fill()
for i in [0,1,2,3]:
    sailesh.forward(90)
    sailesh.left(90)
sailesh.end_fill()
sailesh.pensize(2)
sailesh.forward(45)
sailesh.left(90)
sailesh.forward(90)
sailesh.left(90)
sailesh.forward(45)
sailesh.left(90)
sailesh.forward(45)
sailesh.left(90)
sailesh.forward(90)
sailesh.right(90)
sailesh.forward(45)
sailesh.right(90)
sailesh.forward(110)
sailesh.right(180)

sailesh.pensize(5)      #end of try


sailesh.color("black","silver")
sailesh.begin_fill()



sailesh.forward(130)
sailesh.right(90)
sailesh.forward(100)
sailesh.right(90)
sailesh.forward(130)
sailesh.right(90)
sailesh.forward(100)
sailesh.end_fill()

sailesh.right(180)
sailesh.forward(10)
sailesh.up()
sailesh.left(90)
sailesh.forward(10)

sailesh.down()
sailesh.color("black","yellow")

sailesh.pensize(2)
sailesh.begin_fill()
for i in [0,1,2,3]:
    sailesh.forward(40)
    sailesh.right(90)
sailesh.end_fill()

sailesh.up()
sailesh.right(90)
sailesh.forward(90)
sailesh.left(90)
sailesh.forward(70)
sailesh.left(90)
sailesh.forward(10)

sailesh.down()
sailesh.begin_fill()
for i in [0,1,2,3]:
    sailesh.forward(40)
    sailesh.right(90)
sailesh.end_fill()   #end of second house



sailesh.up()
sailesh.right(90)
sailesh.forward(50)
sailesh.left(90)
sailesh.forward(60)

sailesh.color("black","green")
sailesh.begin_fill()
sailesh.right(50)
sailesh.down()
sailesh.forward(100)
sailesh.right(85)
sailesh.forward(192)
sailesh.right(135.5)
sailesh.forward(210.5)

sailesh.end_fill()   #end of first mountain

sailesh.up()
sailesh.right(90)
sailesh.forward(70)
sailesh.right(50)
sailesh.forward(100)
sailesh.right(85)
sailesh.forward(40)
sailesh.left(80)

sailesh.down()
sailesh.color("black","green")
sailesh.begin_fill()
sailesh.forward(200)
sailesh.right(70)
sailesh.forward(135)
sailesh.right(55)
sailesh.forward(144)
sailesh.right(90)
sailesh.forward(169)
sailesh.right(44.5)
sailesh.forward(150)
sailesh.end_fill()

sailesh2 = turtle.Turtle()
sailesh2.right(38.5)
sailesh2.up()
sailesh2.forward(438)
sailesh2.speed("fastest")
sailesh2.right(141.5)
sailesh2.pensize(1)   #starting the base of tree




#start of tree with sailesh2

sailesh2.down()
sailesh2.forward(67.5)
sailesh2.color("black","red")
sailesh2.begin_fill()
sailesh2.right(90)
sailesh2.pensize(2)
sailesh2.forward(50)
sailesh2.left(90)
sailesh2.forward(15)
sailesh2.left(90)
sailesh2.forward(50)
sailesh2.left(90)
sailesh2.forward(15)
sailesh2.end_fill()    #end of base of tree

sailesh2.left(90)
sailesh2.forward(50)
sailesh2.right(90)
sailesh2.color("black","green")
sailesh2.begin_fill()
sailesh2.forward(37.5)
sailesh2.left(140)
sailesh2.forward(35)
sailesh2.right(140)
sailesh2.forward(20)
sailesh2.left(140)
sailesh2.forward(17.5)
sailesh2.right(140)
sailesh2.forward(12.5)
sailesh2.left(140)
sailesh2.forward(55)
sailesh2.left(90)
sailesh2.forward(50)
sailesh2.left(140)
sailesh2.forward(12.5)
sailesh2.right(140)
sailesh2.forward(17.5)
sailesh2.left(140)
sailesh2.forward(20)
sailesh2.right(150)
sailesh2.forward(35)
sailesh2.left(140)
sailesh2.forward(37.5)
sailesh2.end_fill()     #end of tree




sailesh3 = turtle.Turtle()
sailesh3.pensize(2)
sailesh3.color("black","orange")
sailesh3.begin_fill()
sailesh3.forward(60)
sailesh3.right(120)
sailesh3.forward(30)
sailesh3.left(120)
sailesh3.forward(20)
sailesh3.left(60)
sailesh3.forward(30)
sailesh3.right(60)
sailesh3.forward(40)
sailesh3.left(45)
sailesh3.forward(35)
sailesh3.left(135)
sailesh3.forward(20)
sailesh3.left(45)
sailesh3.forward(20)
sailesh3.right(45)
sailesh3.forward(30)
sailesh3.right(120)
sailesh3.forward(30)
sailesh3.left(120)
sailesh3.forward(20)
sailesh3.left(60)
sailesh3.forward(20)
sailesh3.right(60)
sailesh3.forward(40)
sailesh3.left(38)
sailesh3.forward(30)
sailesh3.end_fill()


sailesh3.left(180)
sailesh3.forward(20)
sailesh3.right(38)
sailesh3.forward(20)
sailesh3.left(38)
sailesh3.forward(10)
sailesh3.left(142)
sailesh3.forward(10)
sailesh3.left(38)
sailesh3.forward(10)#end of plane

sailesh3.up()
sailesh3.forward(150)
sailesh3.color("black","black")


sailesh4 = turtle.Turtle()
sailesh4.up()
sailesh4.forward(60)
sailesh4.right(120)
sailesh4.forward(30)
sailesh4.left(120)
sailesh4.forward(20)
sailesh4.left(60)
sailesh4.forward(30)
sailesh4.right(60)
sailesh4.forward(40)
sailesh4.left(45)
sailesh4.forward(25)
sailesh4.left(135)
sailesh4.forward(13)
sailesh4.down()
sailesh4.color("black","blue")
sailesh4.begin_fill()
sailesh4.circle(4)
sailesh4.end_fill()

wn.exitonclick()

               






