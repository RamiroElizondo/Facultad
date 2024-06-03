import turtle

ventana = turtle.Screen()
puntero = turtle.Turtle()

ventana.bgcolor('#ffc8dd')
puntero.hideturtle()
puntero.pensize(3)

#Letra T
puntero.fillcolor('red')
puntero.penup()
puntero.goto(-300,-50)
puntero.pendown()          

#Arriba
puntero.begin_fill()
puntero.left(90)
puntero.forward(100)

#palo izquierdo
puntero.left(90)
puntero.forward(40)

#palo sube
puntero.right(90)
puntero.forward(40)

#techo
puntero.right(90)
puntero.forward(120)

#palo baja
puntero.right(90)
puntero.forward(40)

#palo derecho
puntero.right(90)
puntero.forward(40)

#abajo
puntero.left(90)
puntero.forward(100)

#base
puntero.right(90)
puntero.forward(40)
puntero.end_fill()


#Letra E
puntero.fillcolor('red')
puntero.begin_fill()
puntero.penup()
puntero.goto(-185,-50)
puntero.pendown()

#Arriba
puntero.right(90)
puntero.forward(140)

#Primer Palo
puntero.right(90)
puntero.forward(100)

puntero.right(90)
puntero.forward(30)

puntero.right(90)
puntero.forward(70)

puntero.left(90)
puntero.forward(25)

#Segundo Palo
puntero.left(90)
puntero.forward(70)

puntero.right(90)
puntero.forward(30)

puntero.right(90)
puntero.forward(70)

puntero.left(90)
puntero.forward(25)

#Tercer Palo
puntero.left(90)
puntero.forward(70)

puntero.right(90)
puntero.forward(30)

puntero.right(90)
puntero.forward(100)
puntero.end_fill()


#Corazon
puntero2 = turtle.Turtle()

puntero2.fillcolor('red')
puntero2.begin_fill()
puntero2.penup()
puntero2.goto(120,-50)
puntero2.pendown()


puntero2.pensize(3)
puntero2.left(50)
puntero2.forward(133)
puntero2.circle(50,200)
puntero2.right(140)
puntero2.circle(50,200)
puntero2.forward(133)

puntero2.end_fill()

ventana.exitonclick()