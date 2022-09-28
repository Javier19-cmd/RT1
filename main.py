#Importando el archivo de raytracer.
from ray import *
from sphere import *
from vector import *

#Creando la ventana.
r = Raytracer(1024, 1024)

r.clear() #Limpia el framebuffer.


#Creando un círculo.
# r.scene.append(Sphere(V3(0, 0, -5), 1))
# r.scene.append(Sphere(V3(-3, 0, -16), 2))

r.scene = [
    Sphere(V3(-3, 0, -5), 1),
    Sphere(V3(-3, 0, -16), 2) 
]

#r.point(512, 512, color(1, 0, 0)) #Dibujando punto de momento.
r.render() #Renderizando.

r.write("out.bmp")