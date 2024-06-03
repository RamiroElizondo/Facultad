import turtle

# Crear una pantalla para dibujar
screen = turtle.Screen()

# Crear una tortuga
t = turtle.Turtle()


# Configurar el tamaño y la fuente del texto
t.pensize(3)
t.write("Hola, mundo!", font=("Arial", 16, "normal"))

# Mover la tortuga a una nueva ubicación
t.penup()
t.goto(0, -50)
t.pendown()

# Configurar el color y el tamaño del lápiz
t.pencolor("blue")
t.pensize(2)

# Dibujar un cuadrado
for i in range(4):
    t.forward(100)
    t.right(90)

# Cerrar la pantalla al hacer clic en ella
screen.exitonclick()