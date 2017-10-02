from random import choice
from OpenGL.GL import *
from OpenGL.GLUT import *

points = list()
curve = list()
window = 0
countOfPoints = 10


def createPoints(count, start, stop, step=0.1):
    listOfNumbers = []
    result = start
    while result < stop:
        listOfNumbers.append(round(result, 1))
        result += step
    for i in range(count):
        points.append([choice(listOfNumbers), choice(listOfNumbers)])


def get_middle_dot(coords):
    return [0.5 * (coords[0][0] + coords[1][0]), 0.5 * (coords[0][1] + coords[1][1])]


def beizer4(my_list):
    global curve
    a = 20
    k = [i / a for i in range(0, a + 1)]
    for t in k:
        x = (1 - t) ** 3 * my_list[0][0] + 3 * (1 - t) ** 2 * t * my_list[1][0] + 3 * (1 - t) * t ** 2 * my_list[2][
            0] + t ** 3 * my_list[3][0]
        y = (1 - t) ** 3 * my_list[0][1] + 3 * (1 - t) ** 2 * t * my_list[1][1] + 3 * (1 - t) * t ** 2 * my_list[
            2][1] + t ** 3 * my_list[3][1]
        curve.append([x, y])


def drawPoints():
    global points

    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 1)
    for point in points:
        glVertex2dv(point)
    glEnd()

    glPointSize(8)
    glBegin(GL_POINTS)
    glColor3f(0.155, 0, 0.211)
    for i in range(2, countOfPoints - 3, 2):
        glVertex2dv(get_middle_dot(points[i:i + 2]))
    glEnd()


def draw_polyline(coords):
    for x in range(len(coords)):
        if x + 1 != len(coords):
            glVertex2dv(coords[x])
            glVertex2dv(coords[x + 1])


def draw():  # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glScalef(0.1, 0.1, 1)

    glLineWidth(1)
    glBegin(GL_LINES)

    glColor3f(1, 0, 1)
    glVertex2d(1, 0)
    glVertex2d(-1, 0)

    glColor3f(1, 0, 1)
    glVertex2d(0, -1)
    glVertex2d(0, 1)

    glColor3f(0.5, 0.5, 0.5)
    draw_polyline(points)
    glEnd()

    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    draw_polyline(curve)
    glEnd()

    drawPoints()

    glutSwapBuffers()  # important for double buffering


def main():
    global curve, window, countOfPoints
    countOfPoints = int(input("Count of points (min 4):\n>>> "))
    createPoints(countOfPoints, -9, 9)

    # Дублирует последнюю точку, если не хватает 1 точки для завершения кривой
    if countOfPoints % 2 == 1:
        countOfPoints += 1
        points.append(points[-1])

    super_arr = points[:3] + [get_middle_dot(points[2:4])]
    beizer4(super_arr)

    if countOfPoints > 4:
        for i in range(2, countOfPoints - 3, 2):
            super_arr = [get_middle_dot(points[i - 2:i])] + points[i - 1:i + 1] + [get_middle_dot(points[i:i + 2])]
            beizer4(super_arr)
        super_arr = [get_middle_dot(points[countOfPoints - 4:countOfPoints - 2])] + points[countOfPoints - 3:countOfPoints]
        beizer4(super_arr)

    glutInit()  # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 640)  # set window size

    glutInitWindowPosition(200, 10)  # set window position
    window = glutCreateWindow(b"2")  # create window with title
    glutDisplayFunc(draw)  # set draw function callback
    glutIdleFunc(draw)  # draw all the time
    glutMainLoop()  # start everything


main()
