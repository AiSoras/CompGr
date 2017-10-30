from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

faces = (((0, 0, 0), (0, 3, 0), (3, 3, 0), (3, 0, 0)),
         ((0, 0, 0), (0, 3, 0), (0, 3, 3), (0, 0, 3)),
         ((3, 0, 3), (3, 3, 3), (3, 3, 0), (3, 0, 0)),
         ((0, 3, 3), (0, 3, 0), (3, 3, 0), (3, 3, 3)),
         ((0, 0, 0), (3, 0, 0), (3, 0, 3), (0, 0, 3)),
         ((0, 0, 3), (3, 0, 3), (3, 3, 3), (0, 3, 3)))

eye = (6, 6, 6)

point = [0, 0, 0]


def keyPressed(bkey, x, y):
    global eye
    try:
        key = bkey.decode("utf-8")
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
    glutPostRedisplay()


def getCanonicalForm(pointOne, pointTwo, pointThree):  # Просто считаю определитель для опеределения канонической формы плоскости
    x1 = pointOne[0]
    y1 = pointOne[1]
    z1 = pointOne[2]

    x2 = pointTwo[0]
    y2 = pointTwo[1]
    z2 = pointTwo[2]

    x3 = pointThree[0]
    y3 = pointThree[1]
    z3 = pointThree[2]

    result = [0, 0, 0, 0]  # ax+by+cz+d=0
    result[0] = (y2-y1)*(z3-z1)-(z2-z1)*(y3-y1)
    result[1] = -((x2-x1)*(z3-z1)-(z2-z1)*(x3-x1))
    result[2] = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    result[3] = -x1*result[0] - y1*result[1] - z1*result[2]

    return result


def getPointInside():
    global point
    count = 0
    for face in faces:
        count += len(face)
        temp = list(zip(*face))
        for i in range(3):
            point[i] += sum(temp[i])
    point = [element/count for element in point]


def getT(plane, pointOne, pointTwo):

    a = plane[0]
    b = plane[1]
    c = plane[2]
    d = plane[3]

    x1 = pointOne[0]
    y1 = pointOne[1]
    z1 = pointOne[2]

    x2 = pointTwo[0]
    y2 = pointTwo[1]
    z2 = pointTwo[2]

    t = (-d-a*x1-b*y1-c*z1)/(a*(x2-x1)+b*(y2-y1)+c*(z2-z1))

    return t


def initFigure():
    global faces, point, eye
    glLineWidth(2)
    for face in faces:
        t = getT(getCanonicalForm(face[0], face[1], face[2]), point, eye)
        if 0 <= t <= 1:
            glBegin(GL_LINE_LOOP)
            glColor3f(0, 0, 0)
            for vertex in face:
                glVertex3dv(vertex)
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


def draw3DScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    gluLookAt(eye[0], eye[1], eye[2], 0, 0, 0, 0, 1, 0)

    initFigure()

    glutSwapBuffers()


def initWindow():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(500, 100)

    window = glutCreateWindow(b"T3")

    glutDisplayFunc(draw3DScene)
    glutKeyboardFunc(keyPressed)
    initGL(800, 800)


def main():
    getPointInside()
    initWindow()
    glutMainLoop()


main()
