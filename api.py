import pygame as py
from window import window
from window.colors import color
from window.img.img_load import img_dict


py.init()

fullscreen = 0

if fullscreen:
	window = window.Window((0,0),"api",color["white"])
else:	
	window = window.Window((800,700),"api",color["lightgrey"])
#print(colors.color["white"])

apiEnd = False
clock = py.time.Clock()
FPS = 30
while not apiEnd:
	clock.tick(FPS)
	for event in py.event.get():
		if event.type == py.MOUSEBUTTONDOWN:
			if event.button == 1:
				window.Check_Button_isClicked(event.pos)
				
							
		if event.type == py.KEYUP:
			if event.key == py.K_ESCAPE:
				apiEnd = True	
		if event.type == py.QUIT:
			apiEnd = True
		
		window.update()
		
		#Draw
		
		py.display.update()
		#FLIP

		py.display.flip()


		


py.quit()
quit()