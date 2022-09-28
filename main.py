from gl import * 

def main(): 
    glCreateWindow(2028, 2028)  
    glClearColor(1, 1, 1) 
    glClear() 
    #Creando array para las esferas.
    glColor(1, 0, 0)
    #glSphere(3, 1, -16, 0.5)

    glSphere(3, 2, -16, 2)
    
    #glSphere(-4, 3, -16, 2)
    
    #Creando esferas.
    #glSphere(0, 0, -5, 1)
    #glSphere(-3, 2, -16, 2)
    glSphere(-4, -1, -5, 2)
    #glSphere(0, -100.5, -1, 100)
    # glSphere(1, 0, -5, 1)
    # glSphere(-1, 0, -5, 1)
    

    finish()

main()