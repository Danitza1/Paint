"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end): # de donde a donde va el rectangulo ((x, y )en vector star y (x ,y) en vector end )
    """Draw line from start to end."""
    up()#levantar el lapiz 
    goto(start.x, start.y)#Mueve el lapiz a la coordenada  x, y 
    down()#Baja el lapiz para empezar a escribir ya en el papel 
    goto(end.x, end.y)#Regresar el lapiz,  mueve el pen a la pos end x, end y 


def square(start, end):
    """Draw square from start to end."""
    up()#levantar el lapiz 
    goto(start.x, start.y)#Mueve el lapiz a la posicion o coordenada star x, y 
    down()#Bjamos el lapiz 
    begin_fill()#Empieza a rellenar 

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


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
#ancho, alto, startx, stary (posicion de la esq. sup izq de la ventana )
setup(420, 420, 370, 0)
#define la funcion que atendera los eventos del mouse se le llama fx callback 
onscreenclick(tap)
#Activar  escuchar todos los eventos del teclado 
listen()
#Ejecuta la fx sin argumentos, la aejecuta cuanto el usuario oprime la tecla definida en el 2 argumento
onkey(undo, 'u')
#color(color_del_contorno, color_relleno)
onkey(lambda: color('black', 'black'), 'K')
onkey(lambda: color('white', '#A3E4D7'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')#store (diccionario)
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')#Radio 
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
