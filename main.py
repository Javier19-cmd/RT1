from gl import * 
from utilidades import * #Archivo de utilidades.

def main(): 
    glCreateWindow(2028, 2028)  
    glClearColor(1, 1, 1) 
    glClear() 
    #Creando array para las esferas.
    glColor(1, 0, 0)
    #glSphere(3, 1, -16, 0.5)

    #Creando al Snowman.
    glSphere(3,        2, -16, 2, color(1, 0, 0)) #Esfera 1 color rojo.
    glSphere(3.8,     -1, -20, 2, color(0, 1, 0)) #Esfera 2 color verde.
    glSphere(3.45,   -3.5, -18, 1, color(0, 0, 1)) #Esfera 3 color azul.

    finish()

main()