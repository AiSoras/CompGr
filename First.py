from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#from math import cos, sin, pi

window = 0

verticesOriginal = (
    (2, 0, 0), (2, 0, 2), (0, 0, 2), (0, 0, 0), (2, 1, 2), (0, 1, 2), (2, 1, 1), (0, 1, 1), (2, 2, 1), (0, 2, 1),
    (0, 2, 0), (2, 2, 0))

eye = (2,3,5)

edges = (
        (0, 1), (0, 3), (0, 11), (1, 2), (1, 4), (2, 5), (2, 3), (4, 5), (4, 6), (5, 7), (6, 8), (7, 9), (6, 7), (8, 9),
        (8, 11), (9, 10), (10, 3), (10, 11))


def matrixMultiplication(matrixOne, matrixTwo):
    result = []
    for i in range(12):
        result.append([0] * 3)
        for j in range(3):
            for k in range(3):
                result[i][j] += matrixOne[i][k] * matrixTwo[k][j]
    return result


def isometryMaxtrix():
    # return [[0.707107, 0.408248, -0.577353], [0, 0.816497, 0.577345], [0.707107, -0.408248, 0.577353]]
    return [[0.707107, 0.408248, 0], [0, 0.816497, 0], [0.707107, -0.408248, 0]]


def keyPressed(bkey, x, y):
    global eye
    # Convert bytes object to string
    try:
        key = bkey.decode("utf-8")
        # Allow to quit by pressing 'Esc' or 'q'
        if key == chr(27):
            sys.exit()
        if key == chr(51):
            initIsometricView()
        if key == 'q':
            print("Bye!")
            sys.exit()
        if key == 'w':
            eye = (eye[0] + 1, eye[1], eye[2])
        if key == 's':
            eye = (eye[0] - 1, eye[1], eye[2])
    except:
        pass


def initFigure3D(vertices):
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def initIsometry():
    vertices = matrixMultiplication(verticesOriginal,isometryMaxtrix())
    for element in vertices:
        element.pop()
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for edge in edges:
        for vertex in edge:
            glVertex2dv(vertices[vertex])
    glEnd()


def draw2DScene():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    glViewport(0, 0, 600, 800)
    initIsometry()
    glutSwapBuffers()


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


def init_axes():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(-100, 0, 0)
    glVertex3f(100, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, -100, 0)
    glVertex3f(0, 100, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, -100)
    glVertex3f(0, 0, 100)

    glEnd()


def draw3DScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    gluLookAt(eye[0], eye[1], eye[2], 0, 0, 0, 0, 1, 0)
    # glTranslatef(0.0, 0.0, -6.0)

    init_axes()
    initFigure3D(verticesOriginal)

    glutSwapBuffers()


def initMainWindow():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow(b"Task_1")

    glutDisplayFunc(draw3DScene)
    glutIdleFunc(draw3DScene)
    glutKeyboardFunc(keyPressed)
    initGL(640, 480)
    glutMainLoop()


def initIsometricView():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow(b"IsometricView")

    glutDisplayFunc(draw2DScene())
    glutIdleFunc(draw2DScene)
    initGL(640, 480)
    glutMainLoop()


def main():
    initMainWindow()


if __name__ == "__main__":
    print("Hit ESC key to quit.")
    main()
