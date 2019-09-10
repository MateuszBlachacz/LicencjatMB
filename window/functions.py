import pygame
from .variables import tmp_list


def text_surface(text,font,text_color):
	textSurface = font.render(text,True,text_color)
	return textSurface
def text_font(size,font=None):
	return pygame.font.Font(font,size)
	
def draw_from_dict(surface,my_dict):
	key_list=list(my_dict.keys())
	for key in key_list:
		draw_Point(surface,my_dict[key])

def draw_point(surface,list_point):
	#print(list_point)
	for point in list_point:
			pygame.draw.circle(surface,(255,0,0),point,3)
			
def draw_Point(surface,list_Points):
		for Point in list_Points:
			pygame.draw.circle(surface,Point.color,(Point.x,Point.y),Point.size)

def draw_Rec(surface,pos):
	pygame.draw.rect(surface,(255,0,0),pos,3)
