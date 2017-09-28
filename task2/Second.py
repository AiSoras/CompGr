from random import choice

points = list()


def createPoints(count, start, stop, step=0.1):
    listOfNumbers = []
    result = start
    while result < stop:
        listOfNumbers.append(round(result,1))
        result += step
    for i in range(count):
        points.append([choice(listOfNumbers), choice(listOfNumbers)])


def main():
    createPoints(10,-10,10)
    print(points)


main()