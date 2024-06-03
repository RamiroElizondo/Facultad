import turtle
import math

# Crear una pantalla para dibujar
screen = turtle.Screen()

# Crear una tortuga y configurar el color y ancho del lápiz
t = turtle.Turtle()
t.pencolor("red")
t.pensize(3)

# Definir la amplitud y la longitud de la línea
amplitud = 20
longitud = 300

# Dibujar la línea ondulante
t.penup()
t.goto(-200, 0)
t.pendown()
for x in range(-200, 200):
    y = math.sin(x / 20) * amplitud
    t.goto(x, y)

# Cerrar la pantalla al hacer clic en ella


screen.exitonclick()

pyinstaller --onefile Turtle\Amor_copy.py
