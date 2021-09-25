import pygame
import update_objects

pygame.init()

game_icon = pygame.image.load("Resources/Images/game_icon_tag.png")

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Tight and Decide [1920x1080] [50 FPS]")
objects_on_screen = []

def makeFont(font_name, fontSize=14, bold=False, italic=False):
    return pygame.font.SysFont(font_name, fontSize, bold, italic)

def returnCurrentObjects():
    return objects_on_screen

def returnRenderedFont(font, valueToDisplay="Failed to pass value"):
    return font.render(str(valueToDisplay), 1, (255, 0, 0))
    

def insertObject(instanceToInsert, posX, posY):
    screen.blit(instanceToInsert, (posX, posY))
    objects_on_screen.append(InstanceReference(instanceToInsert, posX, posY))

def update_ObjectList(new_object_list):
    objects_on_screen = new_object_list


def getScreen():
    try:
        return screen
    except:
        raise Exception("Error while returning screen.")

#def updateScreen(fps):
    ###pygame.display.update()
    ###pygame.time.Clock().tick(fps)

def closeGame():
    pygame.quit()



def FlipScreen():
    pygame.display.flip()

def makeInstanceReference(InstanceToPass, posX, posY):
    return InstanceReference(InstanceToPass, posX, posY)

class InstanceReference:
    def __init__(self, InstanceObject, posX, posY):
        self.InstanceObject = InstanceObject
        self.posX = posX
        self.posY = posY
