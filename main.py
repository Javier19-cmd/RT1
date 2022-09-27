from gl import * 

def main(): 
    glCreateWindow(1024, 1024)  
    glClearColor(1, 1, 1) 
    glClear() 
    glColor(0, 0, 0)
    #point(400, 300)
    cast_ray(V3(0, 0, -5), V3(0, 0, -5))
    finish()

main()