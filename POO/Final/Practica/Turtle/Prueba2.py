import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

def figura(lados):
  for i in range(lados):
    flecha.forward(100)
    flecha.left(360/lados)

figura(3)
figura(4)
figura(5)

turtle.done()