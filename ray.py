from library import * #Importando la librería de raytracer.
from utilidades import * #Archivo de utilidades.
from utilidades import * #Archivo de utilidades.
from math import *
from vector import * #Importando el archivo de vectores.
from sphere import * #Importando el archivo de esferas.

#Clase para el raytracer.
class Raytracer(object):
    def __init__(self, width, height): #Constructor para la clase Raytracer.
        self.width = width
        self.height = height
        self.framebuffer = [] #Frame buffer.
        self.scene = [] #Lista de objetos.
        self.clear_color = color(0, 0, 0) #Color para limpiar el framebuffer.
        self.current_color = color(1, 1, 1) #Color actual.
        self.density = 1 #Densidad.
        #self.clear() #Limpia el framebuffer.
    
    def clear(self): #Limpia el framebuffer.
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def point(self, x, y, c = None): #Punto para dibujar.
        if (y >= 0 and y < self.height) and (x >= 0 and x < self.width): #Si el punto está dentro del framebuffer.
            self.framebuffer[y][x] = c or self.current_color 
    
    def write(self, filename): #Escribe el archivo.
        writebmp(filename, self.width, self.height, self.framebuffer)
    
    def render(self): #Renderiza el framebuffer.
        fov = int(pi/2) #Ángulo de visión.
        aspect_ratio = self.width / self.height #Relación de aspecto.
        tana = tan(fov/2) #Tangente del ángulo de visión.


        for y in range(self.height): 
            for x in range(self.width):
                i = (2 * (x + 0.5) / self.width - 1) * tana * aspect_ratio
                j = (1 - 2 * (y + 0.5) / self.height) * tana

                direction = V3(i, j, -1).normalice() #Dirección del rayo.
                origin = V3(0, 0, 0) #Origen del rayo.
                c = self.cast_ray(origin, direction) #Lanza el rayo.
                self.point(x, y, c)
    
    def cast_ray(self, origin, direction): #Método para lanzar rayos.
        #s = Sphere(V3(-3, 0, -16), 2) #Creando una esfera.
        #print(self.scene)
        for o in self.scene:
            if o.ray_intersect(origin, direction): #Si el rayo intersecta con la esfera.
                return color(0, 1, 0)
        else: #Si no intersecta.
            return self.current_color