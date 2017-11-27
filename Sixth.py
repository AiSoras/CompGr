from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

faces = (((0, 0, 3), (3, 0, 3), (3, 3, 3), (0, 3, 3)),  # Все точки перечислены против часовой стрелки
         ((0, 0, 3), (0, 3, 3), (0, 3, 0), (0, 0, 0)),
         ((0, 0, 0), (0, 3, 0), (3, 3, 0), (3, 0, 0)),
         ((3, 0, 0), (3, 3, 0), (3, 3, 3), (3, 0, 3)),
         ((3, 0, 0), (3, 0, 3), (0, 0, 3), (0, 0, 0)),
         ((3, 3, 3), (3, 3, 0), (0, 3, 0), (0, 3, 3)))

eye = (6, 6, 6)

lightPosition = (4.0, 5.0, 5.0, 1.0)
lightColor = (1.0, 1.0, 1.0, 1.0)

point = [0, 0, 0]

ambient = (0.5, 0.5, 0.5, 1)


def keyPressed(bkey, x, y):
    global eye, lightPosition
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
        if key == 'y':
            lightPosition = (lightPosition[0] - 1, lightPosition[1], lightPosition[2], lightPosition[3])
        if key == 'u':
            lightPosition = (lightPosition[0] + 1, lightPosition[1], lightPosition[2], lightPosition[3])
        if key == 'h':
            lightPosition = (lightPosition[0], lightPosition[1] - 1, lightPosition[2], lightPosition[3])
        if key == 'j':
            lightPosition = (lightPosition[0], lightPosition[1] + 1, lightPosition[2], lightPosition[3])
        if key == 'n':
            lightPosition = (lightPosition[0], lightPosition[1], lightPosition[2] - 1, lightPosition[3])
        if key == 'm':
            lightPosition = (lightPosition[0], lightPosition[1], lightPosition[2] + 1, lightPosition[3])
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
        cannonicalFrom = getCanonicalForm(face[0], face[1], face[2])
        t = getT(cannonicalFrom, point, eye)
        if 0 <= t <= 1:
            glBegin(GL_POLYGON)
            # glColor3f(0.5, 0.5, 0.5)
            glNormal3f(cannonicalFrom[0], cannonicalFrom[1], cannonicalFrom[2])  # Нормаль к плоскости, направлена наружу
            for vertex in face:
                glVertex3dv(vertex)
            glEnd()


def initGL(Width, Height):
    glClearColor(0.25, 0.4, 0.88, 1.0)  # Цвет фона
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_CULL_FACE)  # Отрисовывается только видимая сторона плоскости
    glEnable(GL_LIGHTING)  # Включаем расчет освещения
    glEnable(GL_LIGHT0)  # Включаем источник
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)  # Разрешаем режим освещенности для двух сторон грани
    # glEnable(GL_COLOR_MATERIAL)  # Разрешаем цвет у материала
    glEnable(GL_NORMALIZE)  # Нормализуем нормали во избежание артефактов


def draw3DScene():
    global ambient, lightPosition, lightColor
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Интенсивность освещения

    glLoadIdentity()

    gluLookAt(eye[0], eye[1], eye[2], 0, 0, 0, 0, 1, 0)

    # Настройка свойств источника света
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)  # Положение направленного источника света
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (0.0, 0.0, 1.0))  # Его направление
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 0.0, 0.0, 1.0))  # Интенсивность зеркального света
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor)  # Цвет света
    # glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 180.0)  # Угол между осью и стороной конуса, по умолчанию 180 градусов

    # Настройка свойств материала
    # Далее все идет только для внешней части (Front), т.к. только она и отрисовывается
    glMaterialfv(GL_FRONT, GL_DIFFUSE, lightColor)  # Отвечает за рассеивание материалом света с определенным цветом
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.7, 0.7, 0.7, 1.0))  # Отвечает за затемнение цвета
    # glMaterialfv(GL_FRONT, GL_EMISSION, (0.3, 0.2, 0.2, 0.0))  # Отвечает за излучение материалом
    # glMaterialfv(GL_FRONT, GL_SPECULAR, lightColor)  # Цвет отраженного света
    # glMaterialf(GL_FRONT, GL_SHININESS, 50)  # Интенсивность отражения

    initFigure()

    glutSwapBuffers()


def initWindow():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(500, 100)

    window = glutCreateWindow(b"Task6")

    glutDisplayFunc(draw3DScene)
    # glutIdleFunc(draw3DScene)
    glutKeyboardFunc(keyPressed)
    initGL(800, 800)


def main():
    getPointInside()
    initWindow()
    glutMainLoop()


main()