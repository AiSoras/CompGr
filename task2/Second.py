from random import choice
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

points = list()
window = 0


def createPoints(count, start, stop, step=0.1):
    listOfNumbers = []
    result = start
    while result < stop:
        listOfNumbers.append(round(result,1))
        result += step
    for i in range(count):
        points.append([choice(listOfNumbers), choice(listOfNumbers)])


def draw():  # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glScalef(0.1, 0.1, 1)

    glBegin(GL_LINES)

    glColor3f(1, 0, 1)
    glVertex2d(1, 0)
    glVertex2d(-1, 0)

    glColor3f(1, 0, 1)
    glVertex2d(0, -1)
    glVertex2d(0, 1)

    glColor3f(0,0,0)
    for x in range(len(points)):
        if x+1 != len(points):
            glVertex2d(points[x][0], points[x][1])
            glVertex2d(points[x+1][0], points[x+1][1])

    glEnd()




    glutSwapBuffers()  # important for double buffering


def main():
    createPoints(8,-9,9)
    print(points)

    glutInit()  # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 640)  # set window size

    glutInitWindowPosition(200, 10)  # set window position
    window = glutCreateWindow(b"2")  # create window with title
    glutDisplayFunc(draw)  # set draw function callback
    glutIdleFunc(draw)  # draw all the time
    glutMainLoop()  # start everything


main()