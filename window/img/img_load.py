import pygame
import os

img_dict = {}
path = "window/"
for i in range(1,8):
	img_dict["button"+str(i)] = pygame.image.load(os.path.join(path,"img","batton"+str(i)+".png"))	

for i in range(1,9):
	img_dict["component"+str(i)]= pygame.image.load(os.path.join(path,"img","component"+str(i)+".png"))
	
for i in range(1,5):
	img_dict["component_input"+str(i)] = pygame.image.load(os.path.join(path,"img","component_input"+str(i)+".png"))

img_dict["background"] = pygame.image.load(os.path.join(path,"img","background_alfa.png"))
	