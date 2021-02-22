

import sys
import pygame
import time
import math

pygame.init()

size = width, height = 1400, 500


screen = pygame.display.set_mode(size)


class Circle:
    def __init__(self, posX, posY, omega, radius):
        self.posX = posX
        self.posY = posY
        self.omega = omega
        self.radius = int(radius)
        self.theta = 0

    def update(self):
        if self.theta <= 2*math.pi:
            self.theta += self.omega*(2*math.pi/360)
        else:
            self.theta = 0

    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0),
                           (self.posX, self.posY), self.radius, 1)

        pygame.draw.lines(screen, (0, 0, 0), False, [
            (self.posX, self.posY), (self.posX-self.radius*math.cos(self.theta), self.posY-self.radius*math.sin(self.theta))])

    def getPos(self):
        return int(self.posX-self.radius*math.cos(self.theta)), int(self.posY-self.radius*math.sin(self.theta))

    def setPos(self, posX, posY):
        self.posX = posX
        self.posY = posY


circles = []
x = 1
#  def __init__(self, posX, posY, omega, radius):
circles.append(Circle(350, 250, 1, 400/math.pi))
#circles.append(Circle(350, 250, 3, 400/(3*math.pi)))
#circles.append(Circle(350, 250, 5, 400/(5*math.pi)))
#circles.append(Circle(350, 250, 7, 400/(7*math.pi)))
#circles.append(Circle(350, 250, 0.009, 10))
graph = []
for i in range(5250):
    graph.append(250)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for i in range(len(circles)):
        if i != 0:
            circles[i].setPos(tempX, tempY)
        tempX, tempY = circles[i].getPos()
        circles[i].update()
        circles[i].draw()
    # print(circles[len(circles)-1].getPos()[0])

    pygame.draw.lines(screen, (0, 0, 0), False, [
                      circles[len(circles)-1].getPos(), (700, circles[len(circles)-1].getPos()[1])])

    curentY = circles[len(circles)-1].getPos()[1]

    for i in reversed(range(len(graph)-1)):
        graph[i] = graph[i-1]
    graph[0] = curentY

    for i in range(len(graph)-2):
        pygame.draw.lines(screen, (0, 0, 0), False, [
                          (700+(i-1)/5, graph[i]), (700+i/5, graph[i+1])], 2)
    pygame.display.flip()
    screen.fill((255, 255, 255))
