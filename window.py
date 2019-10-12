import pygame
import ui
from navbar import NavBar

class Window:

    widthMarginSize = 30
    heightMarginSize = 20
    fontSize = 10
    active = False

    windowNavBar = None

    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.windowNavBar = NavBar(start, size)

    def draw(self, screen, start, size):
        GREEN = pygame.Color(116, 191, 186)
        CYAN = pygame.Color(184, 222, 252)
        color = GREEN
        #Background color
        pygame.draw.rect(screen, CYAN, pygame.Rect((start[0], start[1]), (size[0], size[1])))
        self.windowNavBar.draw(screen, color)
        #Left Border
        ui.drawLine(screen, color, (start[0], start[1]), (start[0], start[1] + size[1]))
        #Right Border
        ui.drawLine(screen, color, (start[0] + size[0], start[1]), (start[0] + size[0], start[1] + size[1]))
        #Bottom Border
        ui.drawLine(screen, color, (start[0], start[1] + size[1]), (start[0] + size[0], start[1] + size[1]))

    def shouldRemoveItem(self, mouseX, mouseY):
        return self.windowNavBar.shouldRemoveItem(mouseX, mouseY)

    def shouldDragItem(self, mouseX, mouseY):
        return (not self.windowNavBar.shouldRemoveItem(mouseX, mouseY)
        and (mouseX > 0 or mouseY > 0))

    def move(self, mouseX, mouseY):
        self.start = (mouseX, mouseY)
        self.windowNavBar.move(mouseX, mouseY)

    def activate(self, boolean):
        self.active = boolean
        self.windowNavBar.activate(boolean)