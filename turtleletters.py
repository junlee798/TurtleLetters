import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.setpos(40, 0)
        tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	tur.setheading(0)
	tur.pu()
      	tur.right(90)
	tur.fd(5)
        tur.left(90)
        tur.fd(5)
	tur.pd()
    elif letter == "M":
	tur.setheading(0)
	tur.pu()
	tur.left(90)
	tur.fd(5)
	tur.right(130)
	tur.fd(3)
	tur.left(40)
	tur.fd(3)
	tur.right(130)
	tur.fd(5)
	tur.pd()
    elif letter == "N":
	tur.setheading(0)
	tur.pu()
	tur.left(90)
	tur.fd(5)
	tur.right(130)
	tur.fd(5)
	tur.left(130)
	tur.fd(5)
	tur.pd()
    elif letter == "O":
	tur.setheading(0)
	tur.pu()
	tur.circle(5, 360)
	tur.pd()
    elif letter == "P":
	tur.setheading(0)
	tur.pu()
	tur.circle(3, 360)
	tur.left(90)
	tur.fd(5)
	tur.pd()		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
