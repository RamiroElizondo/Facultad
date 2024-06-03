import turtle

# Crear una pantalla para dibujar
screen = turtle.Screen()

# Crear una tortuga
t = turtle.Turtle()

# Configurar el color y el tamaño del lápiz
t.pencolor("blue")
t.pensize(3)

# Dibujar un círculo
t.circle(50)

# Mover la tortuga a una nueva ubicación
t.penup()
t.goto(-75, 75)
t.pendown()

# Cambiar el color del lápiz y dibujar un triángulo
t.pencolor("red")
for i in range(3):
    t.forward(100)
    t.left(120)

# Cerrar la pantalla al hacer clic en ella
screen.exitonclick()
