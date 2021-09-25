import pygame
pygame.init()

objects = []

class InstanceReference:
    def __init__(self, instanceref, posX, posY, name=None):
        self.instanceref = instanceref
        self.posX = posX
        self.posY = posY
        self.name = name

screen = pygame.display.set_mode((1280, 780))
clock = pygame.time.Clock()
last_edit = InstanceReference("NLE", 0, 0)



def getScreen():
    return screen

def returnSurface(sizeX, sizeY):
    return pygame.Surface((sizeX, sizeY))


def fixedInfoDisplay():
    for m in objects:
        if isinstance(m, InstanceReference):
            if m.name != None:
                print(f"Object Name: '{m.name}' Position: {m.posX}, {m.posY}")

def updateDisplay():
    pygame.display.flip()

def makeFont(font_name="Verdana", font_size=14, text="Failed to pass text", bold=False, italic=False, color=(255, 255, 255), posX=0, posY=0, actual_bg=None, last_edit=last_edit):
    temp_font = pygame.font.SysFont(font_name, font_size, bold, italic)
    render_font = temp_font.render(str(text), 1, color)
    fontClass = InstanceReference(render_font, posX, posY, f"Rendered Font: {text}")

    if last_edit == fontClass:
        objects.pop(objects.index(last_edit))
        objects.append(fontClass)
        last_edit = fontClass
        if isinstance(actual_bg, InstanceReference): insertBackground(actual_bg)
        drawImage(fontClass)
    else:      
        objects.append(fontClass)
        last_edit = fontClass
        if isinstance(actual_bg, InstanceReference): insertBackground(actual_bg)
        drawImage(fontClass)

def loadImage(filePath):
    return pygame.image.load(filePath)

def getObjectList():
    return objects

def addCaption(text="Invalid Text"):
    pygame.display.set_caption(str(text))

def drawImage(imageClass, last_edit=last_edit):
    if imageClass.name != None:
        print(imageClass.name)

    if last_edit == imageClass:
        objects.pop(objects.index(last_edit))
        instance_values = getInstanceValues(imageClass)
        instance = instance_values[0]
        posX = instance_values[1]
        posY = instance_values[2]
        
        last_edit = imageClass
        objects.append(imageClass)
        screen.blit(instance, (posX, posY))
        return imageClass
    else:
        instance_values = getInstanceValues(imageClass)
        instance = instance_values[0]
        posX = instance_values[1]
        posY = instance_values[2]
        
        last_edit = imageClass

        objects.append(imageClass)
        screen.blit(instance, (posX, posY))
        return last_edit

def removeObject(index):
    object_idx = objects[index]
    objects.pop(object_idx)
    updateDisplay()


def appendObject(classObject):
    if isinstance(classObject, InstanceReference):
        objects.append(classObject)

def setIcon(iconClass):
    instance_values = getInstanceValues(iconClass)
    instance = instance_values[0]

    pygame.display.set_icon(instance)

def insertBackground(background_instance):
    instance_values = getInstanceValues(background_instance)
    instance = instance_values[0]
    posX = instance_values[1]
    posY = instance_values[2]

    #objects.append(background_instance)
     

    screen.blit(instance, (posX, posY))

def makeInstanceReference(instanceref, posX, posY, name=None):
    return InstanceReference(instanceref, posX, posY, name)

def getInstanceValues(classToGet):
    values = []

    if isinstance(classToGet, InstanceReference):
        values.append(classToGet.instanceref)
        values.append(classToGet.posX)
        values.append(classToGet.posY)

        return values


