class Sphere(object): #Clase para esferas.
    def __init__(self, center, radius): #Recibe el centro y el radio.
        self.center = center
        self.radius = radius
    
    def ray_intersect(self, orig, dir): #Recibe el origen y la dirección del rayo.
        return True