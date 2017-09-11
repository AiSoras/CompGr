from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ESCAPE = '\033'

window = 0

vertices = (
        (2, 0, 0), (2, 0, 2), (0, 0, 2), (0, 0, 0), (2, 1, 2), (0, 1, 2), (2, 1, 1), (0, 1, 1), (2, 2, 1), (0, 2, 1),
        (0, 2, 0), (2, 2, 0))

def keyPressed(*args):
    if args[0] == ESCAPE:
        sys.exit()


def initFigure():
    edges = (
        (0, 1), (0, 3), (0, 11), (1, 2), (1, 4), (2, 5), (2, 3), (4, 5), (4, 6), (5, 7), (6, 8), (7, 9), (6, 7), (8, 9),
        (8, 11), (9, 10), (10, 3), (10, 11))

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def initGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def drawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)

    initFigure()

    glutSwapBuffers()


def main():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow(b"Task_1")

    glutDisplayFunc(drawGLScene)
    glutIdleFunc(drawGLScene)
    glutKeyboardFunc(keyPressed)
    initGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()
