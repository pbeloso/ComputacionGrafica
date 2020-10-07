# coding=utf-8

# importa la librería Pygame
import pygame

# importa el sub-módulo GL del módulo OpenGL
# Nota: se require la instalación de PyOpenGL
from OpenGL import GL

# colores
black = (0, 0, 0, 1)
green = (0, 1, 0)


def init():
    """
    Inicializa el estado de OpenGL.
    """

    # establece el color de fondo
    GL.glClearColor(*black)


def draw_square():
    """
    Dibuja un cuadrado.
    """

    # limpia el fondo
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    # establece el color del cuadrado
    GL.glColor3f(*green)

    # dibuja el cuadrado
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex3f(1, 1, 0)
    GL.glVertex3f(-1, 1, 0)
    GL.glVertex3f(-1, -1, 0)
    GL.glVertex3f(1, -1, 0)
    GL.glEnd()


def resize(width, height):
    """
    Actualiza la vista (viewport) cuando la pantalla es redimensionada.
    """

    # establece la vista (viewport)
    GL.glViewport(0, 0, width, height)

    # establece la proyección
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glOrtho(-2, 2, -2, 2, -2, 2)

    # establece la vista del modelo
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()


def main():
    # inicializa Pygame
    pygame.init()

    # establece las dimensiones de pantalla
    screen_size = (400, 400)

    # establece las opciones de la pantalla
    screen_options = pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE

    # establece el título de la ventana
    pygame.display.set_caption(u'Dibujar cuadrado')

    # establece el tamaño de la ventana, y habilita algunas opciones
    pygame.display.set_mode(screen_size, screen_options)

    # actualiza la vista (viewport)
    resize(*screen_size)

    # inicializa el estado de OpenGL
    init()

    # ¿la aplicación está ejecutándose?
    is_running = True

    # si la aplicación está ejecutándose
    while is_running:
        # obtiene los eventos de la cola de eventos
        for event in pygame.event.get():
            # si se presiona el botón 'cerrar' de la ventana
            if event.type == pygame.QUIT:
                # detiene la aplicación
                is_running = False

            # si se redimensiona la pantalla
            if event.type == pygame.VIDEORESIZE:
                # actualiza el tamaño de la pantalla y establece las mismas opciones
                screen = pygame.display.set_mode(event.size, screen_options)

                # obtiene el nuevo tamaño de pantalla
                width, height = screen.get_size()

                # actualiza la vista (viewport)
                resize(width, height)

        # dibuja un cuadrado
        draw_square()

        # actualiza la pantalla
        pygame.display.flip()

    # finaliza Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
