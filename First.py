from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ESCAPE = '\033'

window = 0

vertices = (
        (2, 0, 0), (2, 0, 2), (0, 0, 2), (0, 0, 0), (2, 1, 2), (0, 1, 2), (2, 1, 1), (0, 1, 1), (2, 2, 1), (0, 2, 1),
        (0, 2, 0), (2, 2, 0))

eye = (2,3,5)

def keyPressed(bkey, x, y):
    global eye
    # Convert bytes object to string
    try:
        key = bkey.decode("utf-8")
        # Allow to quit by pressing 'Esc' or 'q'
        if key == chr(27):
            sys.exit()
        if key == 'q':
            print("Bye!")
            sys.exit()
        if key == 'w':
            eye = (eye[0]+1, eye[1], eye[2])
        if key == 's':
            eye = (eye[0]-1, eye[1], eye[2])
    except:
        pass


def initFigure():
    edges = (
        (0, 1), (0, 3), (0, 11), (1, 2), (1, 4), (2, 5), (2, 3), (4, 5), (4, 6), (5, 7), (6, 8), (7, 9), (6, 7), (8, 9),
        (8, 11), (9, 10), (10, 3), (10, 11))

    glBegin(GL_LINES)
    glColor3f(0, 0, 0);
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def init_axes():
    glBegin(GL_LINES);
    glColor3f(1, 0, 0);
    glVertex3f(-100, 0, 0);
    glVertex3f(100, 0, 0);

    glColor3f(0, 1, 0);
    glVertex3f(0, -100, 0);
    glVertex3f(0, 100, 0);

    glColor3f(0, 0, 1);
    glVertex3f(0, 0, -100);
    glVertex3f(0, 0, 100);

    glEnd();

def initGL(Width, Height):
    glClearColor(1.0, 1.0, 1.0, 1.0)
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

    gluLookAt(eye[0], eye[1], eye[2], 0, 0, 0, 0, 1, 0)
    #glTranslatef(0.0, 0.0, -6.0)

    init_axes()
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
    print("Hit ESC key to quit.")
    main()
