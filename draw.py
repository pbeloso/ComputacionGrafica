from OpenGL.GL import *
from OpenGL.GLU import *

def drawObject(pos, ang, obj, weapon, tex1, tex2):

    glPushMatrix()

    glTranslatef(pos,-25,-70) # Traslacion (derecha, arriba, hacia adentro).

    glRotatef(-90, 1,0,0)   # Rotacion (angulo, eje x, eje y, eje z).
    glRotatef(ang, 0,0,1)

    glVertexPointer(3, GL_FLOAT, 0, obj.vertFaces)          
    glNormalPointer(GL_FLOAT, 0, obj.normalFaces)           
    glTexCoordPointer(2, GL_FLOAT, 0, obj.texturesFaces)    

    glBindTexture(GL_TEXTURE_2D, tex1)                         
    glDrawArrays(GL_TRIANGLES, 0, len(obj.vertFaces)*3) 

    
    glVertexPointer(3, GL_FLOAT, 0, weapon.vertFaces)          
    glNormalPointer(GL_FLOAT, 0, weapon.normalFaces)           
    glTexCoordPointer(2, GL_FLOAT, 0, weapon.texturesFaces)    

    glBindTexture(GL_TEXTURE_2D, tex2)                         
    glDrawArrays(GL_TRIANGLES, 0, len(weapon.vertFaces)*3)    

    glPopMatrix()

def drawBack(obj,tex):
    
    glPushMatrix()

    glTranslatef(0, 0, -185)  # Traslacion. (derecha, arriba, profundida).
    glRotatef(-90, 0,0,0)   # Rotacion (angulo, eje x, eje y, eje z).
    escala = 187
    glScalef(escala,escala,escala)

    glVertexPointer(3, GL_FLOAT, 0, obj.vertFaces)         
    glNormalPointer(GL_FLOAT, 0, obj.normalFaces)           
    glTexCoordPointer(2, GL_FLOAT, 0, obj.texturesFaces)

    glBindTexture(GL_TEXTURE_2D, tex)
    glDrawArrays(GL_TRIANGLES, 0, len(obj.vertFaces)*3)  

    glPopMatrix()
