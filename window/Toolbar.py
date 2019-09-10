import pygame
from .colors import color
from .Button import Button
from .variables import task_list 
from .img.img_load import img_dict

class Toolbar:
	def __init__(self,window,btn_list):
		self.window = window 
		self.list_button = []
		self.make_Button(btn_list)
		self.draw()

	def draw(self):
		self.toolbar_width= self.window.get_width()
		pygame.draw.rect(self.window,color["lightgrey"], (0, 0, self.toolbar_width, 30))
		self._draw_Button()
		

	def update(self):
		self.draw()

	def make_Button(self,lis_btn):
		for btn in lis_btn:
			if len(btn) >=5:
				if btn[3] in task_list:
					if btn[6] in img_dict:
						self.list_button.append(Button(btn[0],btn[1],btn[2],task_list[btn[3]],color[btn[4]],img_dict[btn[5]],img_dict[btn[6]]))
					else:
						self.list_button.append(Button(btn[0],btn[1],btn[2],task_list[btn[3]],color[btn[4]]))	
				else:
					if btn[6] in img_dict:
						self.list_button.append(Button(btn[0],btn[1],btn[2],btn[3],color[btn[4]],img_dict[btn[5]],img_dict[btn[6]]))
					else:
						self.list_button.append(Button(btn[0],btn[1],btn[2],btn[3],color[btn[4]]))
			else:
				self.list_button.append(Button("New Button",(10,0),(80,30),"No Task",color["red"],img_dict["button1"],img_dict["button4"]))

	def _draw_Button(self):
		for button in self.list_button:
			button.draw(self.window,color["black"])
	
	def get_button_list(self):
		return self.list_button