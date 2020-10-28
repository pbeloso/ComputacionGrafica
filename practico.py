import numpy
import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from obj import *
from event import *

def main():

    #--------------------------------------------------------------------------------------- 

    # Instrucciones para levantar ventana grafica
    
    pygame.init()
    cw = 800
    ch = 600
    display = (cw,ch)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGLBLIT)
    

    background_image = pygame.image.load("prueba.png").convert()

    #---------------------------------------------------------------------------------------  
    
    # Cargar archivos .obj.

    stand = 39
    wave = 10
    salute = 10
    run = 5
    point = 11
    pain = 3
    jump = 5
    flip = 11
    fallback = 16
    death = 5
    attack = 7
    crouch_attack = 8

    #---------------------------------------------------------------------------------------

    #. obj stand

    knight_Stand = obj().objAnimation("./Animaciones/knight_animado/","knight_stand_",stand)
    knight = knight_Stand[0]

    weaponK_Stand = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_stand_",stand)
    weapon_k = weaponK_Stand[0]

    hueteotl_Stand = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_stand_",stand)
    hueteotl = hueteotl_Stand[0]

    weaponH_Stand = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_stand_",stand)
    weapon_h = weaponH_Stand[0]
    
    #---------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------------------

    #. obj stand
    knight_Attack = obj().objAnimation("./Animaciones/knight_animado/","knight_attack_",attack)
    knightAttack = knight_Attack[0]

    weaponK_Attack = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_attack_",attack)
    weapon_k_Attack = weaponK_Attack[0]

    hueteotl_Death = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_death_fallback_",death)
    hueteotlDeath = hueteotl_Death[0]

    weaponH_Death = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_death_fallback_",death)
    weapon_h_Death = weaponH_Death[0]
    
    #---------------------------------------------------------------------------------------

    # Activo las texturas ( 8 disponibles ).

    glEnable(GL_TEXTURE_2D)                         
    glActiveTexture(GL_TEXTURE0)       

    # Funcion que levanta la textura a memoria de video            

    text = loadTexture("./knight_good.png")         

    text2 = loadTexture("./knight.png")         

    text3 = loadTexture("./Animaciones/weapon_knight_animada/weapon_k.png")

    text5 = loadTexture("./Animaciones/hueteotl_animado/hueteotl.png")

    text6 = loadTexture("./Animaciones/weapon_hueteotl_animada/weapon.png")

    #---------------------------------------------------------------------------------------
    
    #glShadeModel(GL_SMOOTH) # El pipeline estatico use Gouraud Shading (sombreado suave).

    # Seteao los parametros del material del objeto a dibujar.
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [1,1,1,1])
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.2,0.2,0.2,1])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1,1,1,1])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128)           


    # Activo las luces ( 0 a 7 )

    glEnable(GL_LIGHT0)   
    glLight(GL_LIGHT0, GL_DIFFUSE, [1.0,0.0,0.0,1])      
    glLight(GL_LIGHT0, GL_AMBIENT, [1,1,1,1])       
    glLight(GL_LIGHT0, GL_POSITION, [0,100,-50,1])      # [0,0,0,1] es luz puntual, [0,0,0,0] es luz direccional
    glLight(GL_LIGHT0, GL_SPECULAR, [1,0,0,1])

    #---------------------------------------------------------------------------------------

    glMatrixMode(GL_PROJECTION)          # Activo el stack de matrices para la proyeccion.
    glLoadIdentity()                     # Cargo una identidad para asegurarme que comience vacio.
    glViewport(0,0,cw*2,ch*2)            # Crea la matriz de escala, transforma de unidades arbitrarias a pixels.
    glFrustum(-1, 1, -1, 1, 1, 1000)     # Crea la matriz de Proyeccion. volumen de vista.

    glEnable(GL_DEPTH_TEST)              # Comparaciones de profundidad y actualizar el bufer de profundidad.

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

    # Variables de animaciones
    
    eventos = events_obj()
    eventos.setTimeEvents()

    stand = True
    attack = False

    death = False
    killed = False

    countKnight = 0
    countHueteotl = 0
    #---------------------------------------------------------------------------------------
    
    while True:

        screen.blit(background_image,[0,0])
        
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:       
                pygame.quit()
                quit()

            if event.type == eventos.knight:
                if stand:
                    knight = knight_Stand[countKnight]
                    weapon_k = weaponK_Stand[countKnight]
                    if countKnight >= (len(knight_Stand) - 1):
                        countKnight = 0
                    else:
                        countKnight += 1
            
            if event.type == eventos.hueteotl:
                if  death == False:
                    hueteotl = hueteotl_Stand[countHueteotl]
                    weapon_h = weaponH_Stand[countHueteotl]
                    if countHueteotl >= (len(hueteotl_Stand) - 1):
                        countHueteotl = 0
                    else:
                        countHueteotl += 1
            
            if attack:     
                knight = knight_Attack[countKnight]
                weapon_k = weaponK_Attack[countKnight]
                if countKnight >= (len(knight_Attack) - 1):
                    stand = not stand   
                    attack = not attack
                    death = not death
                    countKnight = 0
                    countHueteotl = 0
                else:
                    countKnight += 1
            
            if death:

                hueteotl = hueteotl_Death[countHueteotl]
                weapon_h = weaponH_Death[countHueteotl]
                if countHueteotl >= (len(hueteotl_Death) - 1):
                    countHueteotl = 4
                else:
                    countHueteotl += 1




            if event.type == pygame.KEYDOWN:    # Evento tecla presionada.

                if event.key == pygame.K_w:     # Letra w ataca el caballero
                    stand = not stand   
                    attack = not attack
                    countKnight = 0


                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_l:     # Con la letra l prendo y apago la iluminacion
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

        glTranslatef(-30,0,-70) # Traslacion (derecha, arriba, hacia adentro).


        glRotatef(-90, 1,0,0)   # Rotacion (angulo, eje x, eje y, eje z).

        glVertexPointer(3, GL_FLOAT, 0, knight.vertFaces)          
        glNormalPointer(GL_FLOAT, 0, knight.normalFaces)           
        glTexCoordPointer(2, GL_FLOAT, 0, knight.texturesFaces)    

        glBindTexture(GL_TEXTURE_2D, text)                         
        glDrawArrays(GL_TRIANGLES, 0, len(knight.vertFaces)*3)    

        glPopMatrix()

    #---------------------------------------------------------------------------------------    

        glPushMatrix()

        glTranslatef(-30,0,-70) # Traslacion. (derecha, arriba, hacia adentro).


        glRotatef(-90, 1,0,0)   # Rotacion. (angulo, eje x, eje y, eje z).

        glVertexPointer(3, GL_FLOAT, 0, weapon_k.vertFaces)          
        glNormalPointer(GL_FLOAT, 0, weapon_k.normalFaces)           
        glTexCoordPointer(2, GL_FLOAT, 0, weapon_k.texturesFaces)   

        glBindTexture(GL_TEXTURE_2D, text3)      
        glDrawArrays(GL_TRIANGLES, 0, len(weapon_k.vertFaces)*3)     

        glPopMatrix()

    #---------------------------------------------------------------------------------------

        glPushMatrix()

        glTranslatef(30,0,-70)
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

        glTranslatef(30,0,-70)
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

    surf = pygame.image.load(path)                  # Cargo imagen en memoria
    surf = pygame.transform.flip(surf, False, True) # Espejo la imagen

    image = pygame.image.tostring(surf, 'RGBA', 1)  # Obtengo la matriz de colores de la imagen.
    
    ix, iy = surf.get_rect().size       # Obentego las dimensiones de la imagen
    texid = glGenTextures(1)            # Textura vacia en memoria de video
    glBindTexture(GL_TEXTURE_2D, texid) # Activo textura

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
  
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    
    glBindTexture(GL_TEXTURE_2D, 0)
    
    return texid

main()  
