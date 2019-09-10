class Point:
	def __init__(self,x,y,color= (0,0,255),size=2):
		self.x=x
		self.y=y
		self.color=color
		self.size=size
		self.important = False
		self.one = False

	def set_One(self):
		self.color = (255,0,0)
		self.size = 3
		self.one = True 

	def set_Zero(self):
		self.color = (0,0,255)
		self.size = 2
		self.one = False

	def set_important(self,value=True):
		self.important = value