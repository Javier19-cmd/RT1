from ray import *
from utilidades import *


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
def point(x, y): 
    if y > 0 and y < c1.height and x > 0 and x < c1.width:
        c1.framebuffer[y][x] = color(0, 0, 0)

def finish():
    c1.write()