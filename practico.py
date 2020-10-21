import numpy
import pygame

from pygame.locals import *
from OpenGL.GL import *
from obj import *

def main():

    #--------------------------------------------------------------------------------------- 

    # Instrucciones para levantar ventana grafica
    
    pygame.init()
    cw = 800
    ch = 600
    display = (cw,ch)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #---------------------------------------------------------------------------------------  

    # Cargar archivos .obj.
      
    knight = obj()
    knight.objParser("./Animaciones/knight_animado/knight_stand_0.obj")

    weapon_k = obj()
    weapon_k.objParser("./Animaciones/weapon_knight_animada/weapon_k_stand_0.obj")

    hueteotl = obj()
    hueteotl.objParser("./Animaciones/hueteotl_animado/hueteotl_stand_0.obj")

    weapon_h = obj()
    weapon_h.objParser("./Animaciones/weapon_hueteotl_animada/weapon_stand_0.obj")
    
    #---------------------------------------------------------------------------------------

    # Activo las texturas ( 8 disponibles).

    glEnable(GL_TEXTURE_2D)                         
    glActiveTexture(GL_TEXTURE0)                   

    text = loadTexture("./knight_good.png")         # Funcion que levanta la textura a memoria de video

    text2 = loadTexture("./knight.png")         

    text3 = loadTexture("./Animaciones/weapon_knight_animada/weapon_k.png")

    text5 = loadTexture("./Animaciones/hueteotl_animado/hueteotl.png")

    text6 = loadTexture("./Animaciones/weapon_hueteotl_animada/weapon.png")

    #---------------------------------------------------------------------------------------
    
    #glShadeModel(GL_SMOOTH) # El pipeline estatico use Gouraud Shading (sombreado suave).

    # Seteao los parametros del material del objeto a dibujar.

    glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.4, 0.4, 0.4,1]) # Color difuso.
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1,0.1,0.1,1])   # Color ambiente (iluminacion indirecta).
    glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1,1,1,1])        # Color especular, para la parte de Lambert extendida por Phong.
    glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 32)              # Coeficiente especular.


    # Activo las luces ( 0 a 7 )

    glEnable(GL_LIGHT0)   
    glLight(GL_LIGHT0, GL_DIFFUSE, [1,1,1,1])       # Color difuso de la luz (intensidad y color).
    glLight(GL_LIGHT0, GL_POSITION, [0,0,0,1])      # En que parte de la escena se encuentra el foco, con luz puntual.
    #glLight(GL_LIGHT0, GL_POSITION, [0,0,0,0])     # En que parte de la escena se encuentra el foco, con luz direccional.
    glLight(GL_LIGHT0, GL_AMBIENT, [0.1,0.1,0.1,1]) # Cuanto aporta esta luz a la intensidad ambiente (iluminacion indirecta).
    glLight(GL_LIGHT0, GL_SPECULAR, [1,1,1,1])      # El color especular de la luz.

    glEnable(GL_DEPTH_TEST)                         # Comparaciones de profundidad y actualizar el bufer de profundidad.
    
    #---------------------------------------------------------------------------------------

    glMatrixMode(GL_PROJECTION)          # Activo el stack de matrices para la proyeccion.
    glLoadIdentity()                    # Cargo una identidad para asegurarme que comience vacio.
    glViewport(0,0,cw*2,ch*2)            # Crea la matriz de escala, transforma de unidades arbitrarias a pixels.
    glFrustum(-1, 1, -1, 1, 1, 1000)     # Crea la matriz de Proyeccion. volumen de vista.

    #glClearColor(0,0,1,1)               # Color de fondo.
    #---------------------------------------------------------------------------------------

    # Variables
    ang = 0.0
    vel = 0.0

    mode = GL_FILL
    zBuffer = True
    bfc = False
    bfcCW = True

    light = False
    wire = False

    #---------------------------------------------------------------------------------------
    
    while True:
        
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:       
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:    # Evento tecla presionada.

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_l:     # Con la letra L prendo y apago la iluminacion
                    light = not light
                    if(light):
                        glEnable(GL_LIGHTING)
                    else:
                        glDisable(GL_LIGHTING)

                if event.key == pygame.K_m:     # Con la letra m, lo deja en formato malla o no (con o sin fondo).
                    if mode == GL_LINE:
                        mode = GL_FILL
                    else:
                        mode = GL_LINE
                    glPolygonMode( GL_FRONT_AND_BACK, mode)

                if event.key == pygame.K_z:     # Con la letra z, activa el z-buffer
                    zBuffer = not zBuffer
                    if(zBuffer):
                        glEnable(GL_DEPTH_TEST)
                    else:
                        glDisable(GL_DEPTH_TEST)

                if event.key == pygame.K_b:     # Con la letra b, activo cullface
                    bfc = not bfc
                    if(bfc):
                        glEnable(GL_CULL_FACE)
                    else:
                        glDisable(GL_CULL_FACE)

                if event.key == pygame.K_c:     # Con la letra c
                    bfcCW = not bfcCW
                    if(bfcCW):
                        glFrontFace(GL_CW)
                    else:
                        glFrontFace(GL_CCW)

    #---------------------------------------------------------------------------------------
    
        glMatrixMode(GL_MODELVIEW)                          # Activo el stack de matrices MODELVIEW.           
        glLoadIdentity()                                    # Limpio todas la transformaciones previas.
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)    # Limpio el buffer de colores donde voy a dibujar.
        
        # Habilito arrays.

        glEnableClientState(GL_VERTEX_ARRAY)                
        glEnableClientState(GL_NORMAL_ARRAY)               
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)        

    #---------------------------------------------------------------------------------------    

        glPushMatrix()

        glTranslatef(-30,0,-60) # Traslacion (derecha, arriba, hacia adentro).


        glRotatef(-90, 1,0,0)   # Rotacion (angulo, eje x, eje y, eje z).


        glVertexPointer(3, GL_FLOAT, 0, knight.vertFaces)          
        glNormalPointer(GL_FLOAT, 0, knight.normalFaces)           
        glTexCoordPointer(2, GL_FLOAT, 0, knight.texturesFaces)    

        glBindTexture(GL_TEXTURE_2D, text)                         
        glDrawArrays(GL_TRIANGLES, 0, len(knight.vertFaces)*3)    

        glPopMatrix()

    #---------------------------------------------------------------------------------------    

        glPushMatrix()

        glTranslatef(-30,0,-60) # Traslacion. (derecha, arriba, hacia adentro).


        glRotatef(-90, 1,0,0)   # Rotacion. (angulo, eje x, eje y, eje z).

        glVertexPointer(3, GL_FLOAT, 0, weapon_k.vertFaces)          
        glNormalPointer(GL_FLOAT, 0, weapon_k.normalFaces)           
        glTexCoordPointer(2, GL_FLOAT, 0, weapon_k.texturesFaces)   

        glBindTexture(GL_TEXTURE_2D, text3)      
        glDrawArrays(GL_TRIANGLES, 0, len(weapon_k.vertFaces)*3)     

        glPopMatrix()

    #---------------------------------------------------------------------------------------

        glPushMatrix()

        glTranslatef(30,0,-60)
        glRotatef(-90, 1,0,0)   # Rotacion. (angulo, eje x, eje y, eje z).
        glRotatef(230, 0,0,1)
        

        glVertexPointer(3, GL_FLOAT, 0, hueteotl.vertFaces)         
        glNormalPointer(GL_FLOAT, 0, hueteotl.normalFaces)           
        glTexCoordPointer(2, GL_FLOAT, 0, hueteotl.texturesFaces)    

        glBindTexture(GL_TEXTURE_2D, text5)                  
        glDrawArrays(GL_TRIANGLES, 0, len(hueteotl.vertFaces)*3)     

        glPopMatrix()

    #---------------------------------------------------------------------------------------

        glPushMatrix()

        glTranslatef(30,0,-60)
        glRotatef(-90, 1,0,0)   # Rotacion. (angulo, eje x, eje y, eje z).
        glRotatef(243, 0,0,1)
        

        glVertexPointer(3, GL_FLOAT, 0, weapon_h.vertFaces)          
        glNormalPointer(GL_FLOAT, 0, weapon_h.normalFaces)           
        glTexCoordPointer(2, GL_FLOAT, 0, weapon_h.texturesFaces)    

        glBindTexture(GL_TEXTURE_2D, text6)                  
        glDrawArrays(GL_TRIANGLES, 0, len(weapon_h.vertFaces)*3)     

        glPopMatrix()

    #---------------------------------------------------------------------------------------
    
        # Luego de dibujar, desactivo todo.

        glBindTexture(GL_TEXTURE_2D, 0)                     

        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_NORMAL_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        
        pygame.display.flip()       # Hago flip de los buffers, para que se refresque la imagen en pantalla

    glDeleteTextures([text])
    pygame.quit()
    quit()

def loadTexture(path):
    #Cargo la imagen a memoria. pygame se hace cargo de decodificarla correctamente
    surf = pygame.image.load(path)
    surf = pygame.transform.flip(surf, False, True) #espejar la imagen
    #Obtengo la matriz de colores de la imagen en forma de un array binario
    #Le indico el formato en que quiero almacenar los datos (RGBA) y que invierta la matriz, para poder usarla correctamente con OpenGL
    image = pygame.image.tostring(surf, 'RGBA', 1)
    #Obentego las dimensiones de la imagen
    ix, iy = surf.get_rect().size
    #Creo una textura vacia en memoria de video, y me quedo con el identificador (texid) para poder referenciarla
    texid = glGenTextures(1)
    #Activo esta nueva textura para poder cargarle informacion
    glBindTexture(GL_TEXTURE_2D, texid)
    #Seteo los tipos de filtro a usar para agrandar y achivar la textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    #Cargo la matriz de colores dentro de la textura
    #Los parametros que le paso son:
    # - Tipo de textura, en este caso GL_TEXTURE_2D
    # - Nivel de mipmap, en este caso 0 porque no estoy usando mas niveles
    # - Formato en que quiero almacenar los datos en memoria de video, GL_RGB en este caso, porque no necesito canal Alfa
    # - Ancho de la textura
    # - Alto de la textura
    # - Grosor en pixels del borde, en este caso 0 porque no quiero agregar borde a al imagen
    # - Formato de los datos de la imagen, en este caso GL_RGBA que es como lo leimos con pygame.image
    # - Formato de los canales de color, GL_UNSIGNED_BYTE quiere decir que son 8bits para cada canal
    # - La imagen, en este caso la matriz de colores que creamos con pygame.image.tostring
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    #Una vez que tengo todo cargado, desactivo la textura para evitar que se dibuje por error mas adelante
    #Cada vez que quiera usarla, puedo hacer glBindTexture con el identificador (texid) que me guarde al crearla
    glBindTexture(GL_TEXTURE_2D, 0)
    #devuelvo el identificador de la textura para que pueda ser usada mas adelante
    return texid

main()  
