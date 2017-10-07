from tkinter import *

window = 0
graphicFrame = 0
points = []


def initWindow():
    global window, graphicFrame

    window = Tk()
    window.title(u'Работа 3')
    window.geometry('700x800')
    window.resizable(FALSE, FALSE)

    graphicFrame = Frame(window)
    buttonFrame = Frame(window, bg="grey")

    graphicFrame.place(x=0, y=0, width=600, height=800)
    buttonFrame.place(x=600, y=0, width=100, height=800)

    confimButton = Button(buttonFrame, text="Confim")
    pointsLabel = Label(buttonFrame, text="Points")
    pointOneTextField = Text(buttonFrame)
    pointTwoTextField = Text(buttonFrame)
    pointThreeTextField = Text(buttonFrame)
    pointFourTextField = Text(buttonFrame)
    anglesLabel = Label(buttonFrame, text="Angles")
    angleXTextField = Text(buttonFrame)
    angleYTextField = Text(buttonFrame)

    pointsLabel.place(x=10, y=10, width=80, height=80)
    pointOneTextField.place(x=10, y=110, width=80, height=80)
    pointTwoTextField.place(x=10, y=210, width=80, height=80)
    pointThreeTextField.place(x=10, y=310, width=80, height=80)
    pointFourTextField.place(x=10, y=410, width=80, height=80)
    anglesLabel.place(x=10, y=510, width=80, height=80)
    angleXTextField.place(x=10, y=610, width=35, height=80)
    angleYTextField.place(x=55, y=610, width=35, height=80)
    confimButton.place(x=10, y=710, width=80, height=80)

    def getValues(event):
        points.append(list(map(int, element) for element in list(pointOneTextField.get("1.0", "end-1c").split(',')))) #Надо норм преобразование сделать из char в int
        points.append(map(int, element) for element in list(pointTwoTextField.get("1.0", "end-1c").split(',')))
        points.append(map(int, element) for element in list(pointThreeTextField.get("1.0", "end-1c").split(',')))
        points.append(map(int, element) for element in list(pointFourTextField.get("1.0", "end-1c").split(',')))

        print(points)


    confimButton.bind("<Button-1>", getValues)


initWindow()
window.mainloop()
