from tkinter import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

verticesOriginal = ((0, 0, 1), (1, 1, 1), (1, 0, 0), (0, 1, 0))

eye = (2, 3, 5)

graphicFrame = 0
points = []


def initWindow():
    # global window
    #
    # window = Tk()
    # window.title(u'Работа 3')
    # window.geometry('700x800')
    # window.resizable(FALSE, FALSE)

    initGraphicFrame()
    # #graphicFrame = Frame(window)
    # buttonFrame = Frame(window, bg="grey")
    #
    # #graphicFrame.place(x=0, y=0, width=600, height=800)
    # buttonFrame.place(x=600, y=0, width=100, height=800)
    #
    # confimButton = Button(buttonFrame, text="Confim")
    # pointsLabel = Label(buttonFrame, text="Points")
    # pointOneTextField = Text(buttonFrame)
    # pointTwoTextField = Text(buttonFrame)
    # pointThreeTextField = Text(buttonFrame)
    # pointFourTextField = Text(buttonFrame)
    # anglesLabel = Label(buttonFrame, text="Angles")
    # angleXTextField = Text(buttonFrame)
    # angleYTextField = Text(buttonFrame)
    #
    # pointsLabel.place(x=10, y=10, width=80, height=80)
    # pointOneTextField.place(x=10, y=110, width=80, height=80)
    # pointTwoTextField.place(x=10, y=210, width=80, height=80)
    # pointThreeTextField.place(x=10, y=310, width=80, height=80)
    # pointFourTextField.place(x=10, y=410, width=80, height=80)
    # anglesLabel.place(x=10, y=510, width=80, height=80)
    # angleXTextField.place(x=10, y=610, width=35, height=80)
    # angleYTextField.place(x=55, y=610, width=35, height=80)
    # confimButton.place(x=10, y=710, width=80, height=80)
    #
    # def getValues(event):
    #     points.append(list(map(int, element) for element in list(pointOneTextField.get("1.0", "end-1c").split(',')))) #Надо норм преобразование сделать из char в int
    #     points.append(map(int, element) for element in list(pointTwoTextField.get("1.0", "end-1c").split(',')))
    #     points.append(map(int, element) for element in list(pointThreeTextField.get("1.0", "end-1c").split(',')))
    #     points.append(map(int, element) for element in list(pointFourTextField.get("1.0", "end-1c").split(',')))
    #
    #     print(points)
    #
    #
    # confimButton.bind("<Button-1>", getValues)


def keyPressed(bkey, x, y):
    """
    Обработчик событий клавиш в программе
    :rtype: object
    """
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
            eye = (eye[0] + 1, eye[1], eye[2])
        if key == 's':
            eye = (eye[0] - 1, eye[1], eye[2])
    except:
        pass


def initPlane(vertices):
    a = 20
    k = [i / a for i in range(0, a + 1)]
    point = [0, 0, 0]

    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 1)
    for u in k:
        for w in k:
            for i in range(3):
                point[i] = (1 - u) * (1 - w) * vertices[0][i] + u * (1 - w) * vertices[1][i] + (1 - u) * w * vertices[2][i] + u * w * vertices[3][i]
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
    """
    Отрисовывает оси координат
    """
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
    initPlane(verticesOriginal)

    glutSwapBuffers()


def initGraphicFrame():
    global graphicFrame, window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow(b"T3")
    #graphicFrame = glutCreateSubWindow(window, 0, 0, 600, 800)

    glutSetWindow(graphicFrame)
    glutDisplayFunc(draw3DScene)
    glutIdleFunc(draw3DScene)
    glutKeyboardFunc(keyPressed)
    initGL(640, 480)
    glutMainLoop()


initWindow()
window.mainloop()


# def matrixMultiplication(matrixOne, matrixTwo):
#     """
#     Эта функция используется для умножения двух матриц
#     :param matrixOne:
#     :param matrixTwo:
#     :return: результат умножения матриц, вложенный массив
#     """
#     result = []
#     for i in range(12):
#         result.append([0] * 3)
#         for j in range(3):
#             for k in range(3):
#                 result[i][j] += matrixOne[i][k] * matrixTwo[k][j]
#     return result


