import pygame
pygame.init()

objects = []

screen = pygame.display.set_mode((1920, 1080))

def getScreen():
    return screen

def updateDisplay():
    pygame.display.flip()

def loadImage(filePath):
    return pygame.image.load(filePath)

def addCaption(text="Invalid Text"):
    pygame.display.set_caption(str(text))

def drawImage(imageClass):
    instance_values = getInstanceValues(imageClass)
    instance = instance_values[0]
    posX = instance_values[1]
    posY = instance_values[2]

    
    objects.append(imageClass)
    screen.blit(instance, (posX, posY))


def setIcon(iconClass):
    instance_values = getInstanceValues(iconClass)
    instance = instance_values[0]

    pygame.display.set_icon(instance)

def insertBackground(background_instance):
    instance_values = getInstanceValues(background_instance)
    instance = instance_values[0]
    posX = instance_values[1]
    posY = instance_values[2]

    screen.blit(instance, (posX, posY))

def makeInstanceReference(instanceref, posX, posY):
    return InstanceReference(instanceref, posX, posY)

def getInstanceValues(classToGet):
    values = []

    if isinstance(classToGet, InstanceReference):
        values.append(classToGet.instanceref)
        values.append(classToGet.posX)
        values.append(classToGet.posY)

        return values


class InstanceReference:
    def __init__(self, instanceref, posX, posY):
        self.instanceref = instanceref
        self.posX = posX
        self.posY = posY