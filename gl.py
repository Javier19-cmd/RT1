from ray import *
from utilidades import *
from math import *
from vector import *
from sphere import *

c1 = Raytracer(); #Instancia de la clase Raytracer.


def glCreateWindow(width, height): #Función para crear la ventana.
    c1.width = width; #Se le asigna el ancho.
    c1.height = height; #Se le asigna el alto.

def glClearColor(r, g, b): #Función para el color de fondo.
    c1.color = color(r, g, b); #Se le asigna el color.

def glClear(): #Función para limpiar la pantalla.
    c1.framebuffer = [[c1.color for x in range(c1.width)] for y in range(c1.height)]; #Se crea el framebuffer.

def glColor(r, g, b): #Función para el color de la figura.
    c1.colorPunto = color(r, g, b); #Se le asigna el color.

#Defininiendo el point.
def point(x, y, c): 
    c1.framebuffer[y][x] = c; #Se le asigna el color.

def cast_ray(orig, direction): #Método para el rayo. 

    s = Sphere(V3(-3, 0, -16), 2) #Creando la esfera.
    
    if s.ray_intersect(orig, direction): #Si el rayo intersecta con la esfera.
        #Retornando un color.
        return color(1, 0, 0)
    else: #Si no intersecta.
        return c1.color

def finish():

    aspectRatio = c1.width / c1.height #Relación de aspecto.
    tana = tan(60 * 0.5 * pi / 180) #Tangente del ángulo.

    for y in range(c1.height):
        for x in range(c1.width):
            i = ((2 * (x + 0.5) / c1.width) - 1) * tana * aspectRatio
            j = -(2 * (y + 0.5) / c1.height) * tana
            direction = (V3(i, j, -1)).normalice()

            c = cast_ray(V3(0, 0, 0), direction) #Llamando al método para el rayo.

            point(x, y, c)
    c1.write()