import pygame
from pygame.locals import *

from OpenGL.GL import *
import numpy

def main():
    pygame.init()
    cw = 800
    ch = 600
    display = (cw,ch)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #---------------------------------------------------------------------------------------

    vertFaces = []
    normalFaces = []
    texturesFaces = []

    vertFacesW = []
    normalFacesW = []
    texturesFacesW = []
         
    objParser("./Animaciones/knight_animado/knight_stand_0.obj", vertFaces, normalFaces, texturesFaces)       # Llamo al parser.
    objParser("./Animaciones/weapon_knight_animada/weapon_k_stand_0.obj", vertFacesW, normalFacesW, texturesFacesW)    # Llamo al parser.

    #---------------------------------------------------------------------------------------

    glEnable(GL_TEXTURE_2D)                         # Activo el manejo de texturas
    glActiveTexture(GL_TEXTURE0)                    # Activo la textura 0 (hay 8 disponibles)
    text = loadTexture("./knight_good.png")         # Llamo a la funcion que levanta la textura a memoria de video

    text2 = loadTexture("./knight.png")         

    text3 = loadTexture("./Animaciones/weapon_knight_animada/weapon_k.png")

    #---------------------------------------------------------------------------------------
    
    glShadeModel(GL_SMOOTH) # El pipeline estatico use Gouraud Shading (sombreado suave).

    #Empiezo por setear los parametros del material del objeto a dibujar.

    glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.4, 0.4, 0.4,1]) # Color difuso.
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1,0.1,0.1,1])   # Color ambiente (iluminacion indirecta).
    glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1,1,1,1])        # Color especular, para la parte de Lambert extendida por Phong.
    glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 32)              # Coeficiente especular.

    glEnable(GL_LIGHT0)   
    glLight(GL_LIGHT0, GL_DIFFUSE, [1,1,1,1])       # Color difuso de la luz (intensidad y color).
    glLight(GL_LIGHT0, GL_POSITION, [0,0,0,1])      # En que parte de la escena se encuentra el foco, con luz puntual.
    #glLight(GL_LIGHT0, GL_POSITION, [0,0,0,0])     # En que parte de la escena se encuentra el foco, con luz direccional.
    glLight(GL_LIGHT0, GL_AMBIENT, [0.1,0.1,0.1,1]) # Cuanto aporta esta luz a la intensidad ambiente (iluminacion indirecta).
    glLight(GL_LIGHT0, GL_SPECULAR, [1,1,1,1])      # El color especular de la luz.

    glEnable(GL_DEPTH_TEST)
    
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

    light = False
    wire = False

    #---------------------------------------------------------------------------------------
    
    while True:
        
        for event in pygame.event.get():        # Chequeo todos los eventos del cuadro anterior, utilizando la libreria de pygame.
            if event.type == pygame.QUIT:       # Quiere cerrar la ventana, y la aplicacion debe finalizar.
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_l:
                    #Con la letra L prendo y apago la iluminacion
                    light = not light
                    if(light):
                        glEnable(GL_LIGHTING)
                    else:
                        glDisable(GL_LIGHTING)
                if event.key == pygame.K_m:   # Si el evento apreta letra m, lo deja en formato malla o no (con o sin fondo).
                    if not wire:
                        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                    else:
                        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
                    wire = not wire
            if event.type == pygame.KEYDOWN:    #Si el evento es una tecla presionada.
                if event.key == pygame.K_LEFT:
                    vel = 1
                elif event.key == pygame.K_RIGHT:
                    vel = -1
    
    
        
        glMatrixMode(GL_MODELVIEW)                          # Activo el stack de matrices MODELVIEW.           
        glLoadIdentity()                                    # Limpio todas la transformaciones previas.
        
        glEnableClientState(GL_VERTEX_ARRAY)                # Habilito el array de vertices.
        glEnableClientState(GL_NORMAL_ARRAY)                # Habilito el array de normales.
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)         # Habilito el array de coordenadas de textura

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)    # Limpio el buffer de colores donde voy a dibujar. 

    #---------------------------------------------------------------------------------------    

        glPushMatrix()

        glTranslatef(-30,0,-60)                               # Traslacion. (derecha, arriba, hacia adentro).
        #glTranslatef(0,0,-3)

        glRotatef(-90, 1,0,0)                               # Rotacion. (angulo, eje x, eje y, eje z).
        #glRotatef(ang, 0,0,1)
        #ang += 0.5

        glVertexPointer(3, GL_FLOAT, 0, vertFaces)          # Paso el array de vertices, de 3 coords en cada elemento, que son de tipo float.
        glNormalPointer(GL_FLOAT, 0, normalFaces)           # Paso el array de normales.
        glTexCoordPointer(2, GL_FLOAT, 0, texturesFaces)    # Paso la lista de coordenadas de textura para cada vertice

        glBindTexture(GL_TEXTURE_2D, text)                  # Cargo la textura "text" en la posicion activa (que es la 0 en este ejemplo)
        glDrawArrays(GL_TRIANGLES, 0, len(vertFaces)*3)     # Indico que voy a dibujar triangulos, usando el array de vertices.

        glPopMatrix()

    #---------------------------------------------------------------------------------------    

        glPushMatrix()

        glTranslatef(-30,0,-60)                               # Traslacion. (derecha, arriba, hacia adentro).
        #glTranslatef(0,0,-3)

        glRotatef(-90, 1,0,0)                               # Rotacion. (angulo, eje x, eje y, eje z).
        #glRotatef(ang, 0,0,1)
        #ang += 0.5

        glVertexPointer(3, GL_FLOAT, 0, vertFacesW)          # Paso el array de vertices, de 3 coords en cada elemento, que son de tipo float.
        glNormalPointer(GL_FLOAT, 0, normalFacesW)           # Paso el array de normales.
        glTexCoordPointer(2, GL_FLOAT, 0, texturesFacesW)    # Paso la lista de coordenadas de textura para cada vertice

        glBindTexture(GL_TEXTURE_2D, text3)                  # Cargo la textura "text" en la posicion activa (que es la 0 en este ejemplo)
        glDrawArrays(GL_TRIANGLES, 0, len(vertFacesW)*3)     # Indico que voy a dibujar triangulos, usando el array de vertices.

        glPopMatrix()

    #---------------------------------------------------------------------------------------

        glPushMatrix()

        glTranslatef(30,0,-60)
        glRotatef(-90, 1,0,0)                               # Rotacion. (angulo, eje x, eje y, eje z).
        glRotatef(243, 0,0,1)
        

        glVertexPointer(3, GL_FLOAT, 0, vertFaces)          # Paso el array de vertices, de 3 coords en cada elemento, que son de tipo float.
        glNormalPointer(GL_FLOAT, 0, normalFaces)           # Paso el array de normales.
        glTexCoordPointer(2, GL_FLOAT, 0, texturesFaces)    # Paso la lista de coordenadas de textura para cada vertice

        glBindTexture(GL_TEXTURE_2D, text2)                  # Cargo la textura "text" en la posicion activa (que es la 0 en este ejemplo)
        glDrawArrays(GL_TRIANGLES, 0, len(vertFaces)*3)     # Indico que voy a dibujar triangulos, usando el array de vertices.

        glPopMatrix()

    #---------------------------------------------------------------------------------------

        glPushMatrix()

        glTranslatef(30,0,-60)
        glRotatef(-90, 1,0,0)                               # Rotacion. (angulo, eje x, eje y, eje z).
        glRotatef(243, 0,0,1)
        

        glVertexPointer(3, GL_FLOAT, 0, vertFacesW)          # Paso el array de vertices, de 3 coords en cada elemento, que son de tipo float.
        glNormalPointer(GL_FLOAT, 0, normalFacesW)           # Paso el array de normales.
        glTexCoordPointer(2, GL_FLOAT, 0, texturesFacesW)    # Paso la lista de coordenadas de textura para cada vertice

        glBindTexture(GL_TEXTURE_2D, text3)                  # Cargo la textura "text" en la posicion activa (que es la 0 en este ejemplo)
        glDrawArrays(GL_TRIANGLES, 0, len(vertFacesW)*3)     # Indico que voy a dibujar triangulos, usando el array de vertices.

        glPopMatrix()

    #---------------------------------------------------------------------------------------
    
        glBindTexture(GL_TEXTURE_2D, 0)                     # Luego de dibujar, desactivo la textura

        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_NORMAL_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        
        pygame.display.flip()                               # Hago flip de los buffers, para que se refresque la imagen en pantalla

    glDeleteTextures([text])
    pygame.quit()
    quit()

def objParser(path, vertFaces, normalFaces, texturesFaces):
    objFile = open(path, 'r')
    #objFile = open('box.obj', 'r')

    vertexList = []
    normalList = []
    textList = []

    for line in objFile:
        split = line.split()
        if not len(split) or split[0] == "o" or split[0] == "#":	# Si es un espacio en blanco, #, o;  continuo
            continue

        if split[0] == "v":			 	# Si empieza con v, lo agrego a la lista de vertices				
            vertex = [ float(split[1]), float(split[2]), float(split[3]) ]
            vertexList.append(vertex)
        
        if split[0] == "vn":			# Si empieza con vn, lo agrego a la lista de normales	
            normal = [ float(split[1]), float(split[2]), float(split[3]) ]
            normalList.append(normal)

        if split[0] == "vt":            # Si empieza con vn, lo agrego a la lista de normales				
            texture = [ float(split[1]), float(split[2]) ]
            textList.append(texture)


        elif split[0] == "f":			# Si empieza con f, lo agrego a la lista de faces
            vert = []
            norm = []
            text = []

            for i in range(1,4):
                splitFace = split[i].split("/")
                vert.append(splitFace[0])
                norm.append(splitFace[1])
                text.append(splitFace[2])

            vertexface = [ vertexList[int(vert[0])-1], vertexList[int(vert[1])-1], vertexList[int(vert[2])-1] ]
            vertFaces.append(vertexface)

            normalFace = [ normalList[int(norm[0])-1], normalList[int(norm[1])-1], normalList[int(norm[2])-1] ]
            normalFaces.append(normalFace)

            textFace = [ textList[int(text[0])-1], textList[int(text[1])-1], textList[int(text[2])-1] ]
            texturesFaces.append(textFace)

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
