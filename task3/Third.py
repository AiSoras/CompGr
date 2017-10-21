from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin, radians
from random import choice

window = 0

verticesOriginal = ((0, 0, 1), (1, 1, 1), (1, 0, 0), (0, 1, 0))
points = []

eye = (2, 3, 5)


def createPoints(count, start, stop, step=0.1):
    global points
    listOfNumbers = []
    result = start
    while result < stop:
        listOfNumbers.append(round(result, 1))
        result += step
    for i in range(count):
        points.append([choice(listOfNumbers), choice(listOfNumbers), choice(listOfNumbers)])


def keyPressed(bkey, x, y):
    global eye
    # Convert bytes object to string
    try:
        key = bkey.decode("utf-8")
        # Allow to quit by pressing 'Esc' or 'q'
        if key == chr(27):
            sys.exit()
        if key == 'w':
            eye = (eye[0], eye[1] + 1, eye[2])
        if key == 's':
            eye = (eye[0], eye[1] - 1, eye[2])
        if key == 'd':
            eye = (eye[0] + 1, eye[1], eye[2])
        if key == 'a':
            eye = (eye[0] - 1, eye[1], eye[2])
        if key == 'q':
            eye = (eye[0], eye[1], eye[2] - 1)
        if key == 'e':
            eye = (eye[0], eye[1], eye[2] + 1)
    except:
        pass


def initPlane(vertices):
    a = 20
    k = [i / a for i in range(0, a + 1)]
    point = [0, 0, 0]

    glPointSize(2)
    glBegin(GL_LINE_STRIP)
    glColor3f(0, 0, 1)
    for u in k:
        for w in k:
            for i in range(3):
                point[i] = (1 - u) * (1 - w) * vertices[0][i] + u * (1 - w) * vertices[1][i] + (1 - u) * w * \
                                                                                               vertices[2][i] + u * w * \
                                                                                                                vertices[
                                                                                                                    3][
                                                                                                                    i]
            glVertex3dv(point)
    glEnd()


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
    #initPlane(verticesOriginal)
    initPlane(points)

    glutSwapBuffers()


def initGraphicFrame():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(500, 100)

    window = glutCreateWindow(b"T3")

    glutDisplayFunc(draw3DScene)
    glutIdleFunc(draw3DScene)
    glutKeyboardFunc(keyPressed)
    initGL(1000, 500)


def matrixMultiplication(matrixOne, matrixTwo):
    result = []
    for i in range(len(matrixOne)):
        result.append([0] * 3)
        for j in range(3):
            for k in range(3):
                result[i][j] += matrixOne[i][k] * matrixTwo[k][j]
    return result


def rotateOX(angle, vertices):
    angle = radians(angle)
    cosine = round(cos(angle), 5)
    sine = round(sin(angle), 5)
    rotationMatrix = [[1, 0, 0], [0, cosine, sine], [0, -sine, cosine]]
    return matrixMultiplication(vertices, rotationMatrix)


def initSubWindow():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(1000, 100)
    SubWindow = glutCreateWindow(b"Angle")
    glutSetWindow(SubWindow)
    glutDisplayFunc(draw3DScene)
    glutIdleFunc(draw3DScene)
    glutKeyboardFunc(keyPressed)
    initGL(500, 500)


def main():
    global points
    createPoints(4, -3, 3)
    angle = int(input("Angle of rotation about the OX axis:\n>>> "))
    initGraphicFrame()
    print(points)
    if (angle!=0):
        points = rotateOX(angle, points)
        print(points)
        initSubWindow()
    glutMainLoop()


main()
