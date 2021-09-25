import pygame
import screencontroller
import update_objects


pygame.init()

background = pygame.image.load("Resources/Images/background.jpg")
background = pygame.transform.scale(background, (1280, 720))
italian_flag_image = pygame.image.load("Resources/Images/italian_flag.png")
italian_flag_image = pygame.transform.scale(italian_flag_image, (340, 230))


testFont = screencontroller.makeFont("Verdana", 14, True, True)
renderFont = screencontroller.returnRenderedFont(testFont, "Test Font")
screencontroller.insertObject(background, 0, 0)
screencontroller.insertObject(italian_flag_image, 430, 0)
count = 0 

while True:
    print(count)
    if count == 1200:
        renderFont = screencontroller.returnRenderedFont(testFont, "Another test font!")
        count += 1
        update_objects.insert_and_update_object(renderFont, 430, 100)
    count += 1
    
    screencontroller.FlipScreen()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
