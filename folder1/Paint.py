"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from math import sqrt, tanh
from turtle import *
from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    #Levantar el lapiz
    up()
    #Mueve el lapiz a coordenada (start.x,start.y)
    goto(start.x, start.y)
    #Baja el lapiz
    down()
    #Mueve a la posicion en (end.x,end.y)
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    #Levantar el lapiz
    up()
    #Mueve el lapiz a coordenada (start.x,start.y)
    goto(start.x, start.y)
    #Baja el lapiz
    down()
    #Activa el relleno
    begin_fill()

    for count in range(4): #secuencia de 0,1,2,3
        forward(end.x - start.x)
        left(90)

    end_fill()
   

def circle3(start, end):
    """Draw circle from start to end."""
    circle(start.x,start.y)


def rectangle(start, end):
    """Draw rectangle from start to end."""
    #Levantar el lapiz
    up()
    #Mueve el lapiz a coordenada (start.x,start.y)
    goto(start.x, start.y)
    #Baja el lapiz
    down()
    #Activa el relleno
    begin_fill()    
    for count in range(2): #secuencia de 0,1,2
        forward((end.x - start.x)*1.5)
        left(90)
        forward(end.x - start.x)
        left(90)
    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    #Levantar el lapiz
    up()
    #Mueve el lapiz a coordenada (start.x,start.y)
    goto(start.x, start.y)
    #Baja el lapiz
    down()
    #Activa el relleno
    begin_fill()    
    for count in range(3): #secuencia de 0,1,2
        forward(end.x - start.x)
        left(120)
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
#ancho, alto, startx( posicion de la esq.sup izq de la ventana)
setup(420, 420, 370, 0)
#Definir la funcion que atendera los eventos del mouse se la llama fx callback
onscreenclick(tap)
#Escucha los elementos del teclado
listen()
#Ejecuta funcion sin argumentos
onkey(undo, 'u')
onkey(lambda: color('black','yellow'), 'K')
#color (color_Del_Contorno, Color_Del_Relleno, Key de activacion)
onkey(lambda: color('white', '#FF5733'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle3), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
