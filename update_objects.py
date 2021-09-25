import pygame
import screencontroller

pygame.init()

def insert_and_update_object(InstanceToAdd, posX, posY):
	current_objects_in_list = screencontroller.returnCurrentObjects()
	
	for every_object in current_objects_in_list:
		if every_object.posX == posX and every_object.posY == posY:
			current_objects_in_list.pop(current_objects_in_list.index(every_object))
			update_all_objects()
			classInstanceReferenceObject = screencontroller.makeInstanceReference(InstanceToAdd, posX, posY)
			current_objects_in_list.append(classInstanceReferenceObject)
			screencontroller.insertObject(classInstanceReferenceObject.InstanceObject, classInstanceReferenceObject.posX, classInstanceReferenceObject.posY)
			screencontroller.update_ObjectList(current_objects_in_list)
			screencontroller.FlipScreen()
			print(f"Done inserted object at {classInstanceReferenceObject.posX}, {classInstanceReferenceObject.posY} succeffuly.")
		else:
			classInstanceReferenceObject = screencontroller.makeInstanceReference(InstanceToAdd, posX, posY)
			current_objects_in_list.append(classInstanceReferenceObject)
			screencontroller.insertObject(classInstanceReferenceObject.InstanceObject, classInstanceReferenceObject.posX, classInstanceReferenceObject.posY)
			screencontroller.update_ObjectList(current_objects_in_list)
			screencontroller.FlipScreen()
			print(f"Done inserted object at {classInstanceReferenceObject.posX}, {classInstanceReferenceObject.posY} succeffuly.")


def update_all_objects():
	current_objects_in_list = screencontroller.returnCurrentObjects()

	for deprecated in current_objects_in_list:
		print(deprecated.posX, deprecated.posY)
		screencontroller.insertObject(deprecated.InstanceObject, deprecated.posX, deprecated.posY)
		current_objects_in_list.pop(current_objects_in_list.index(deprecated))
		screencontroller.update_ObjectList(current_objects_in_list)

