import pygame

from .functions import text_surface,text_font

class Button:
	def __init__(self,text,pos,size,task,color,img=None,img2=None):
		self.text = text
		self.pos = pos
		self.size = size
		self.task = task
		self.color = color
		self.img = img
		self.img_l= [img,img2]
		self.img_i = 0
	
	def get_button_size(self):
		return (self.pos[0],self.pos[1],self.size[0],self.size[1])
	@property
	def task(self):
		return self._task

	@task.setter
	def task(self,task):
		self._task = task

	@task.getter
	def task(self):
		return self._task

	def Click_mouse(self):
		if not isinstance(self.task,type("")):
			self.change_image()
			try:
				self.task()
			except Exception:
				print("End game")
			finally:
				self.change_image()
		else:
			print(self.task)

		#self.change_image()

	def change_image(self):
		if self.img_i == 0:
			self.set_image(self.img_l[1])
			self.img_i = 1
		else:
			self.set_image(self.img_l[0])
			self.img_i = 0

	def set_image(self,image):
		self.img = image

	def draw(self,window,text_color):
		if self.img:
			self.img = pygame.transform.scale(self.img,(self.size[0],self.size[1]))
			self.rect = self.img.get_rect()
			self.rect.x = self.pos[0]
			self.rect.y = self.pos[1]
			window.blit(self.img,self.rect)
		else:		
			pygame.draw.rect(window,self.color,(self.pos[0],self.pos[1], self.size[0], self.size[1]))
		
		ts=text_surface(self.text,text_font(20,None),text_color)
		ts_rect = ts.get_rect()
		ts_rect.topleft = (self.pos[0]+(self.size[0]*0.05),self.pos[1]+(self.size[1]*0.3))
		window.blit(ts,ts_rect)


	def __str__(self):
		return_string = "Jesem przyciskiem \nText:" + self.text + "\n" + "Task: " + self.task 	
		return  return_string


