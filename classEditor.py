
def changeName(classReference, new_name):
    import screencontroller

    ob_list = screencontroller.getObjectList()

    #try:
    new_instance = screencontroller.makeInstanceReference(classReference.instanceref, classReference.posX, classReference.posY, new_name)
    screencontroller.appendObject(new_instance)
    #except:
        #import main 
        #main.running = False