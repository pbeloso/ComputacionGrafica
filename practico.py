import numpy
import random
import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from obj import *
from event import *

import texture
import draw

def main():

    #--------------------------------------------------------------------------------------- 

    # Instrucciones para levantar ventana grafica
    
    pygame.init()
    cw = 800
    ch = 600
    display = (cw,ch)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|OPENGLBLIT)

    #---------------------------------------------------------------------------------------  
    
    # Cargar archivos .obj.

    fondoList = obj().objAnimation("./Animaciones/fondo/","fondo_", 0)
    fondo = fondoList[0]

    stand = 39
    death = 5
    deathSlow = 7
    attack = 7
    run = 5
    crouch = 18
    wave = 10

    # .obj knight

    # stand

    knight_Stand = obj().objAnimation("./Animaciones/knight_animado/","knight_stand_",stand)
    knight = knight_Stand[0]

    weaponK_Stand = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_stand_",stand)
    weapon_k = weaponK_Stand[0]

    # attack

    knight_Attack = obj().objAnimation("./Animaciones/knight_animado/","knight_attack_",attack)
    weaponK_Attack = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_attack_",attack)

    # death

    knight_Death0 = obj().objAnimation("./Animaciones/knight_animado/","knight_death_fallback_",death)
    weaponK_Death0 = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_death_fallback_",death)

    knight_Death1 = obj().objAnimation("./Animaciones/knight_animado/","knight_death_fallforward_",death)
    weaponK_Death1 = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_death_fallforward_",death)

    knight_Death2 = obj().objAnimation("./Animaciones/knight_animado/","knight_death_fallbackslow_",deathSlow)
    weaponK_Death2 = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_death_fallbackslow_",deathSlow)

    # run

    knight_Run = obj().objAnimation("./Animaciones/knight_animado/","knight_run_",run)
    weaponK_Run = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_run_",run)

    # crouch

    knight_Crouch = obj().objAnimation("./Animaciones/knight_animado/","knight_crouch_stand_",crouch)
    weaponK_Crouch = obj().objAnimation("./Animaciones/weapon_knight_animada/","weapon_k_crouch_stand_",crouch)

    #---------------------------------------------------------------------------------------

    # .obj hueteotl 

    # stand

    hueteotl_Stand = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_stand_",stand)
    hueteotl = hueteotl_Stand[0]

    weaponH_Stand = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_stand_",stand)
    weapon_h = weaponH_Stand[0]

    # attack

    hueteotl_Attack = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_attack_",attack)
    weaponH_Attack = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_attack_",attack)

    # death 

    hueteotl_Death0 = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_death_fallback_",death)
    weaponH_Death0 = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_death_fallback_",death)

    hueteotl_Death1 = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_death_fallforward_",death)
    weaponH_Death1 = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_death_fallforward_",death)

    hueteotl_Death2 = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_death_fallbackslow_",deathSlow)
    weaponH_Death2 = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_death_fallbackslow_",deathSlow)

    # run

    hueteotl_Run = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_run_",run)
    weaponH_Run = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_run_",run)

    # crouch

    hueteotl_Crouch = obj().objAnimation("./Animaciones/hueteotl_animado/","hueteotl_crouch_stand_",crouch)
    weaponH_Crouch = obj().objAnimation("./Animaciones/weapon_hueteotl_animada/","weapon_crouch_stand_",crouch)

    #---------------------------------------------------------------------------------------

    # Activo las texturas ( 8 disponibles ).

    glEnable(GL_TEXTURE_2D)                         
    glActiveTexture(GL_TEXTURE0)       

    # Funcion que levanta la textura a memoria de video         

    fondoIma = texture.loadTexture("./Animaciones/fondo/fondo2.jpg")   

    tex = texture.loadTexture("./Animaciones/knight_animado/knight_good.png") 

    tex2 = texture.loadTexture("./Animaciones/knight_animado/knight.png") 

    tex3 = texture.loadTexture("./Animaciones/weapon_knight_animada/weapon_k.png")

    tex5 = texture.loadTexture("./Animaciones/hueteotl_animado/hueteotl.png")

    tex6 = texture.loadTexture("./Animaciones/weapon_hueteotl_animada/weapon.png")

    #---------------------------------------------------------------------------------------
    
    #glShadeModel(GL_SMOOTH) # El pipeline estatico use Gouraud Shading (sombreado suave).

    # Seteao los parametros del material del objeto a dibujar.
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [1,1,1,1])
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.2,0.2,0.2,1])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1,1,1,1])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128)           


    # Activo las luces ( 0 a 7 )

    glEnable(GL_LIGHT0)   
    glLight(GL_LIGHT0, GL_DIFFUSE, [1,0,0,1])      
    glLight(GL_LIGHT0, GL_AMBIENT, [1,1,1,1])       
    glLight(GL_LIGHT0, GL_POSITION, [0,10,20,0])      # [0,0,0,1] es luz puntual, [0,0,0,0] es luz direccional
    glLight(GL_LIGHT0, GL_SPECULAR, [0,0,0,1])

    #---------------------------------------------------------------------------------------

    glMatrixMode(GL_PROJECTION)          # Activo el stack de matrices para la proyeccion.
    glLoadIdentity()                     # Cargo una identidad para asegurarme que comience vacio.
    glViewport(0,0,cw*2,ch*2)            # Crea la matriz de escala, transforma de unidades arbitrarias a pixels.
    glFrustum(-1, 1, -1, 1, 1, 1000)     # Crea la matriz de Proyeccion. volumen de vista.

    glEnable(GL_DEPTH_TEST)              # Comparaciones de profundidad y actualizar el bufer de profundidad.

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
    eludir = False

    stand_h = True
    attack_h = False 
    death_h = False
    eludir_h = False

    countKnight = 0
    countHueteotl = 0

    count_h = 0
    count_k = 0

    typeofDeath = 0

    pos_h = 25
    ang_h = 210

    pos_k = -25
    ang_k = 0
 
    #---------------------------------------------------------------------------------------
    
    while True:
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:       
                pygame.quit()
                quit()

            # Evento incial stand knight
            if event.type == eventos.knight:
                if stand:
                    knight = knight_Stand[countKnight]
                    weapon_k = weaponK_Stand[countKnight]
                    if countKnight >= (len(knight_Stand) - 1):
                        countKnight = 0
                    else:
                        countKnight += 1

            # Evento incial stand hueteotl
            if event.type == eventos.hueteotl:
                if  stand_h:
                    hueteotl = hueteotl_Stand[countHueteotl]
                    weapon_h = weaponH_Stand[countHueteotl]
                    if countHueteotl >= (len(hueteotl_Stand) - 1):
                        countHueteotl = 0
                    else:
                        countHueteotl += 1
            
            # Evento ataque de knight
            if attack and death == False:     
                knight = knight_Attack[countKnight]
                weapon_k = weaponK_Attack[countKnight]
                if countKnight >= (len(knight_Attack) - 1):
                    stand = True   
                    attack = False
                    if eludir_h == False:
                        death_h = True
                    stand_h = False
                    typeofDeath = random.randint(0, 2)
                    countKnight = 0
                    countHueteotl = 0
                else:
                    countKnight += 1

            # Evento ataque de hueteotl
            if attack_h and death_h == False:
                hueteotl = hueteotl_Attack[countHueteotl]
                weapon_h = weaponH_Attack[countHueteotl]
                if countHueteotl >= (len(hueteotl_Attack) - 1):
                    stand_h = True
                    attack_h = False
                    if eludir == False:
                        death = True
                    stand = False
                    typeofDeath = random.randint(0, 2)
                    countHueteotl = 0
                    countKnight = 0
                else:
                    countHueteotl += 1

            # Evento muerte de hueteotl, random de sus 3 muertes 
            if death_h:
                if attack_h == False and stand_h == False:
                    if typeofDeath == 0:
                        hueteotl = hueteotl_Death0[countHueteotl]
                        weapon_h = weaponH_Death0[countHueteotl]
                        if countHueteotl >= (len(hueteotl_Death0) - 1):
                            countHueteotl = len(hueteotl_Death0) - 1
                        else:
                            countHueteotl += 1
                    if typeofDeath == 1:
                        hueteotl = hueteotl_Death1[countHueteotl]
                        weapon_h = weaponH_Death1[countHueteotl]
                        if countHueteotl >= (len(hueteotl_Death1) - 1):
                            countHueteotl = len(hueteotl_Death1) - 1
                        else:
                            countHueteotl += 1
                    if typeofDeath == 2:
                        hueteotl = hueteotl_Death2[countHueteotl]
                        weapon_h = weaponH_Death2[countHueteotl]
                        if countHueteotl >= (len(hueteotl_Death2) - 1):
                            countHueteotl = len(hueteotl_Death2) - 1
                        else:
                            countHueteotl += 1
            
            # Evento muerte de knight, random de sus 3 muertes
            if death:
                if attack == False and stand == False:
                    if typeofDeath == 0:
                        knight = knight_Death0[countKnight]
                        weapon_k = weaponK_Death0[countKnight]
                        if countKnight >= (len(knight_Death0) - 1):
                            countKnight = len(knight_Death0) - 1
                        else:
                            countKnight += 1
                    if typeofDeath == 1:
                        knight = knight_Death1[countKnight]
                        weapon_k = weaponK_Death1[countKnight]
                        if countKnight >= (len(knight_Death1) - 1):
                            countKnight = len(knight_Death1) - 1
                        else:
                            countKnight += 1
                    if typeofDeath == 2:
                        knight = knight_Death2[countKnight]
                        weapon_k = weaponK_Death2[countKnight]
                        if countKnight >= (len(knight_Death2) - 1):
                            countKnight = len(knight_Death2) - 1
                        else:
                            countKnight += 1

            # Evento huir de hueteotl
            if stand_h == False and attack_h == False and death_h == False and eludir_h == False:
                ang_h = -20
                hueteotl = hueteotl_Run[countHueteotl]
                weapon_h = weaponH_Run[countHueteotl]
                if countHueteotl >= (len(hueteotl_Run) - 1):
                    count_h += 1
                    countHueteotl = 0
                    if count_h >= 7:
                        stand_h = True 
                        count_h = 0   
                else:
                    countHueteotl += 1
                    pos_h += 2

            # Evento huir de knight
            if stand == False and attack == False and death == False and eludir == False:
                ang_k = 230
                knight = knight_Run[countKnight]
                weapon_k = knight_Run[countKnight]
                if countKnight >= (len(knight_Run) - 1):
                    count_k += 1 
                    countKnight = 0
                    if count_k >= 7:
                        stand = True
                        count_k = 0
                else:
                    countKnight += 1
                    pos_k -= 2

            # Evento eludir ataque de hueteotl
            if stand_h == False and attack_h == False and death_h == False and eludir_h:
                hueteotl = hueteotl_Run[countHueteotl]
                weapon_h = weaponH_Run[countHueteotl]
                if countHueteotl >= (len(hueteotl_Run) - 1):
                    count_h += 1
                    countHueteotl = 0
                    if count_h >= 2:
                        stand_h = True 
                        eludir_h = False 
                        count_h = 0  
                else:
                    countHueteotl +=1 
                    if count_h == 0:
                        pos_h += 2
                    else:
                        pos_h = 25
                

            # Evento eludir ataque de knight
            if stand == False and attack == False and death == False and eludir:
                knight = knight_Run[countKnight]
                weapon_k = weaponK_Run[countKnight]
                if countKnight >= (len(knight_Run) - 1):
                    count_k += 1
                    countKnight = 0
                    if count_k >= 2:
                        stand = True 
                        eludir = False  
                        count_k = 0 
                else:
                    countKnight +=1 
                    if count_k == 0:
                        pos_k -= 2
                    else:
                        pos_k = -25

            if event.type == pygame.KEYDOWN:    # Evento tecla presionada.

                if event.key == pygame.K_w:     # tecla w ataca knight
                    if death == False and attack_h == False:
                        stand = False   
                        attack = True
                        countKnight = 0

                if event.key == pygame.K_o:     # tecla o ataca hueteolt
                    if death_h == False and attack == False:
                        stand_h = False
                        attack_h =  True 
                        countHueteotl = 0

                if event.key == pygame.K_p:     # tecla o corre hueteolt
                    if death_h == False:
                        stand_h = False
                        countHueteotl = 0 
                
                if event.key == pygame.K_e:     # tecla q corre knight
                    if death == False:
                        stand = False
                        countKnight = 0 

                if event.key == pygame.K_i:     # tecla i elude hueteotl
                    if death_h == False:
                        stand_h = False
                        eludir_h = True
                        countHueteotl = 0 

                if event.key == pygame.K_q:     # tecla e elude knight
                    if death == False:
                        stand = False
                        eludir = True
                        countKnight = 0 

                if event.key == pygame.K_r:     # tecla r, reinicia pelea
                    stand = True
                    attack = False
                    death = False
                    eludir = False

                    stand_h = True
                    attack_h = False 
                    death_h = False
                    eludir_h = False

                    countKnight = 0
                    countHueteotl = 0

                    count_k = 0
                    count_h = 0

                    typeofDeath = 0
                    pos_h = 25
                    ang_h = 210  

                    ang_k = 0
                    pos_k = -25 

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_l:     # Con la tecla l prendo y apago la iluminacion
                    light = not light
                    if(light):
                        glEnable(GL_LIGHTING)
                        glClearColor(0,0,0,1)
                    else:
                        glDisable(GL_LIGHTING)
                        glClearColor(0.5,0.5,0.5,1)

                if event.key == pygame.K_m:     # Con la tecla m, lo deja en formato malla o no (con o sin fondo).
                    if mode == GL_LINE:
                        mode = GL_FILL
                    else:
                        mode = GL_LINE
                    glPolygonMode( GL_FRONT_AND_BACK, mode)

                if event.key == pygame.K_z:     # Con la tecla z, activa el z-buffer
                    zBuffer = not zBuffer
                    if(zBuffer):
                        glEnable(GL_DEPTH_TEST)
                    else:
                        glDisable(GL_DEPTH_TEST)

                if event.key == pygame.K_b:     # Con la tecla b, activo cullface
                    bfc = not bfc
                    if(bfc):
                        glEnable(GL_CULL_FACE)
                    else:
                        glDisable(GL_CULL_FACE)

    #---------------------------------------------------------------------------------------
    
        glMatrixMode(GL_MODELVIEW)                          # Activo el stack de matrices MODELVIEW.           
        glLoadIdentity()                                    # Limpio todas la transformaciones previas.
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)    # Limpio el buffer de colores donde voy a dibujar.
        
        # Habilito arrays.

        glEnableClientState(GL_VERTEX_ARRAY)                
        glEnableClientState(GL_NORMAL_ARRAY)               
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)        

    #---------------------------------------------------------------------------------------  
    
        # fondo
           
        draw.drawBack(fondo,fondoIma)
        
        # knight

        draw.drawObject(pos_k, ang_k, knight, weapon_k, tex, tex3)

    #---------------------------------------------------------------------------------------

        # hueteotl
        
        draw.drawObject(pos_h, ang_h, hueteotl, weapon_h, tex5, tex6)
        
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

main()  