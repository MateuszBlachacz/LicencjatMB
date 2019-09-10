import pygame

from .img.img_load import img_dict
from .Toolbar import Toolbar
from .variables import button_create_list as bcl
from .variables import draw_list,tt_list,rect_dict,Point_dict
from .variables import task_list
from .functions import draw_point,draw_Point,draw_Rec,draw_from_dict

class Window:

	def __init__(self,size = None,name="api",color =(0,0,0),test_mode = False):
		self.mainWindow = None
		self.toolbar = None
		self.color = color
		self.list_crt_btn = (bcl["btn1"],bcl["btn2"],bcl["btn3"],
			bcl["btn4"],bcl["btn5"],bcl["btn6"],bcl["btn7"],
			bcl["btn8"],
			bcl["btn_Play"],bcl["btn_Pause"])
		if size:
			self.create_window(size)
		else:
			self.full_screen()
		
		self.image = img_dict["background"]

		self.name_window = name
		self.fill(self.color)
		print("Say Hello!")
		if not test_mode:
			self.window_task_list()
			self.create_toolsbar(self.list_crt_btn)
		self.play = True

	def create_window(self,size):
		self.mainWindow = pygame.display.set_mode(size)

	def full_screen(self):
		self.mainWindow = pygame.display.set_mode((800,600),pygame.FULLSCREEN)

	def fill(self,color):
		if self.mainWindow != None:
			self.mainWindow.fill(color)
	def draw_computer(self):
		if self.mainWindow != None:
			self.mainWindow.blit(self.image,[100,30])
		

	def getMainWindow(self):
		return self.mainWindow
	@property
	def name_window(self):
		return self._name_window

	@name_window.setter
	def name_window(self,name):
		pygame.display.set_caption(name)

	@name_window.getter
	def name_window(self):
		return pygame.display.get_caption()
	
	def window_task_list(self):
		task_list["INA"] = self.INA
		task_list["CMA"] = self.CMA
		task_list["LDI"] = self.LDI
		task_list["ADI"] = self.ADI
		task_list["LDA"] = self.LDA
		task_list["STA"] = self.STA
		task_list["INP"] = self.INP
		task_list["OUT"] = self.OUT
		task_list["Play"] = self.animation_play
		task_list["Pause"] = self.animation_pause
		task_list["Stop"] = self.animation_stop
		
		
	def create_toolsbar(self,list_btn):
		self.toolbar = Toolbar(pygame.display.get_surface(),list_btn)

	def Check_Button_isClicked(self,pos,normal=True):
		
		if normal:
			btn_list =self._take_button_list()
		else:
			btn_list =self._take_short_button_list()

		for button in btn_list:
			btn_size=button.get_button_size()
			#print(btn_size)
			if	btn_size[0] < pos[0] and (btn_size[2]+btn_size[0]) > pos[0]:
				if btn_size[1] < pos[1] and (btn_size[3]+btn_size[1]) > pos[1]:
					button.Click_mouse()
					break

	def _take_button_list(self):
		#window_button_list=[]
		window_button_list = self.toolbar.get_button_list()

		return window_button_list

	def _take_short_button_list(self):
		#window_button_list=[]
		window_button_list = self.toolbar.get_button_list()
		short_window_button_list = []
		chcek = [" Play"," Pause"," Stop"]
		for button in window_button_list:
			#print(button.text)
			if button.text in chcek:
				short_window_button_list.append(button)

		return short_window_button_list

	def update(self):
		self.fill(self.color)
		self.draw_computer()
		draw_from_dict(self.getMainWindow(),Point_dict)
		self.draw_Rect()

		if self.toolbar:
			self.toolbar.update()
	
	def INA(self):
		self.T0()
		self.T1()
		self.D1T2()

	def CMA(self):
		self.T0()
		self.T1()
		self.D2T2()
	
	def LDI(self):
		self.T0()
		self.T1()
		self.D3T2()
		self.D3T3()

	def ADI(self):
		self.T0()
		self.T1()
		self.D4T2()
		self.D4T3()

	def LDA(self):
		self.T0()
		self.T1()
		self.D5T2()
		self.D5T3()
		self.D5T4()
		self.D5T5()

	def STA(self):
		self.T0()
		self.T1()
		self.D6T2()
		self.D6T3()
		self.D6T4()
		self.D6T5()

	def INP(self):
		self.T0()
		self.T1()
		self.D7T2()

	def OUT(self):
		self.T0()
		self.T1()
		self.D8T2()
	
	
	

		
	def T0(self,lhide=True):
		if lhide:
			self.hide_all()
			self.rect_set_False() 
			Point_dict["time_point"][0].set_One()
		sd  = 200
		self.show("dekoder_out")
		self.show("stage_C1")
		self.show("stage_C1_MUX1")
		self.update_rect("PC_rect")
		self.show("stage_C2_MUX2")
		self.show("Mux1_list")
		self.show("Ram_read")
		self.update_rect("RAM_rect")
		self.show("Ram_list")
		self.show("Mux2_list")
		self.show("stage_C1_load")
		self.show("DR_load")
		self.update_rect("DR_rect")
		self.show_DR(sd)
	
	def T1(self):
		Point_dict["time_point"][0].set_Zero()
		self.hide("dekoder_out")
		self.hide("stage_C1")
		self.hide("stage_C1_MUX1")
		self.hide("stage_C2_MUX2")
		self.hide("Mux1_list")
		self.hide("Ram_read")
		self.hide("Ram_list")
		self.hide("Mux2_list")
		self.hide("stage_C1_load")
		self.hide("DR_load")
		self.hide("DR_list_RAM")
		self.hide("DR_list_AR")
		self.hide("DR_list_ADDER")
		self.hide("DR_list_MUX3")
		self.hide("Mux3_list")	
		self.rect_set_False()
		self.update_rect("DR_rect")
		Point_dict["time_point"][1].set_One()
		self.visual(1000)
		self.show("dekoder_out")
		self.show("stage_C3")
		self.update_rect("IR_rect")
		self.show("IR_list")
		self.increment_PC()


	def T2(self):
		Point_dict["time_point"][1].set_Zero()
		self.hide("dekoder_out")
		self.hide_increment_PC()
		self.hide("stage_C3")
		self.rect_set_False()
		Point_dict["time_point"][2].set_One()
		self.update_rect("IR_rect")
		self.show("IR_list")		
		
	def T3(self):
		Point_dict["time_point"][2].set_Zero()
		self.hide("DR_list_RAM")		
		self.hide("stage_C1")
		self.hide("stage_C1_load")
		self.hide("stage_C1_MUX1")				
		self.hide("stage_C2_MUX2")
		self.hide("Mux1_list")
		self.hide("Mux2_list")
		self.hide("Ram_read")
		self.hide("Ram_list")
		self.hide("DR_load")		
		self.hide("dekoder_out")
		self.rect_set_False()
		Point_dict["time_point"][3].set_One()

	def T4(self):
		Point_dict["time_point"][3].set_Zero()
		self.hide_DR_left()
		self.hide("DR_list_AR")
		self.hide("AR_list")
		self.hide("stage_C8")
		self.hide("dekoder_out")
		self.hide_increment_PC()
		self.rect_set_False()
		Point_dict["time_point"][4].set_One()

	def T5(self):
		Point_dict["time_point"][4].set_Zero()
		self.hide_DR_left()
		self.hide("DR_list_AR")
		self.hide("DR_list_AR")
		self.hide("DR_list_ADDER")
		Point_dict["time_point"][5].set_One()


		
		
	def D1T2(self):
		self.T2()
		self.D(0)
		self.show("stage_C4")
		self.update_rect("AC_rect")
		self.reset_clock()

	def D2T2(self):
		self.T2()
		self.D(1)
		self.show("stage_C5")
		self.update_rect("AC_rect")
		self.reset_clock()

	def D3T2(self):
		self.hide_DR_left()
		self.T2()
		self.D(2)
		self.T0(False)
	
	def D3T3(self):
		self.T3()
		self.hide("DR_list_ARIR")
		self.hide("DR_list_AR")		
		self.hide("DR_list_IR")
		self.D(2)
		self.load_DR_to_AC()
		self.increment_PC()		
		self.reset_clock()

	def D4T2(self):
		self.hide_DR_left()
		self.T2()
		self.D(3)
		self.T0(False)
	
	def D4T3(self):
		self.hide("DR_list_MUX3")
		self.hide("DR_list_MUX3ARIR")
		self.hide("DR_list_ARIR")
		self.hide("DR_list_AR")		
		self.hide("DR_list_IR")
		self.T3()
		self.D(3)
		self.show("stage_C7")
		self.show("stage_C7_Select")
		self.show("stage_C7_Load")
		self.show("AC_load")
		self.update_rect("AC_rect")
		self.show("AC_list")
		self.show("AC_list_OUR")
		self.show("AC_list_ADDERMUX2")
		self.show("AC_list_MUX2",100)
		self.show("AC_list_ADDER")
		self.update_rect("ADDER_rect")
		self.show("Adder_list")
		self.show("Mux3_list")
		self.increment_PC()
		self.reset_clock()
	
	def D5T2(self):
		self.hide_DR_left()
		self.T2()
		self.D(4)
		self.T0(False)
	
	def D5T3(self):
		self.hide("DR_list_IR")
		self.hide("DR_list_MUX3")
		self.hide("DR_list_ADDER")
		self.hide("Mux3_list")
		self.T3()
		self.D(4)	
		self.load_DR_to_AR()		
		self.increment_PC()
	
	def D5T4(self):
		self.T4()
		self.D(4)
		self.show("stage_C10_RAM")
		self.show("Ram_read")
		self.update_rect("RAM_rect")
		self.show("Ram_list")
		self.show("Mux2_list")		
		self.show("stage_C10")
		self.show("DR_load")
		self.update_rect("DR_rect")
		self.show_DR()

	def D5T5(self):
		self.hide("DR_list_RAM")
		self.T5()
		self.D(4)
		self.load_AR_to_AC()
		self.reset_clock()

	def D6T2(self):
		self.hide_DR_left()
		self.T2()
		self.D(5)
		self.T0(False)

	def D6T3(self):
		self.hide("DR_list_IR")
		self.hide("IR_list")	
		self.hide("DR_list_MUX3")
		self.hide("DR_list_ADDER")
		self.hide("Mux3_list")
		self.T3()
		self.D(5)	
		self.load_DR_to_AR()		
		self.increment_PC()
	
	def D6T4(self):
		self.T4()
		self.D(5)
		self.update_rect("AC_rect")
		self.show("AC_list")
		self.show("AC_list_OUR")	
		self.show("AC_list_ADDERMUX2")
		self.show("AC_list_ADDER")	
		self.show("AC_list_MUX2")
		self.show("stage_C9")
		self.show("stage_C9_Select")
		self.show("Mux2_list")
		self.show("DR_load")
		self.update_rect("DR_rect")
		self.show_DR(100)
	
	def D6T5(self):
		self.hide("AC_list")
		self.hide("AC_list_OUR")	
		self.hide("AC_list_ADDERMUX2")
		self.hide("AC_list_ADDER")	
		self.hide("AC_list_MUX2")
		self.hide("DR_list_MUX3ARIR")
		self.hide("DR_list_MUX3")
		self.T5()
		self.D(5)
		self.show("stage_C11")
		self.update_rect("RAM_rect")
		self.reset_clock()

	def D7T2(self):
		self.T2()
		self.D(6)
		self.show("INR_IN")
		self.update_rect("INR_rect")
		self.show("INR_list")
		self.show("stage_C13")
		self.show("stage_C13_Select")
		self.show("Mux3_list")
		self.show("stage_C13_Load")
		self.show("AC_load")
		self.update_rect("AC_rect")
		self.reset_clock()
	
	def D8T2(self):
		self.T2()
		self.D(7)
		self.update_rect("AC_rect")
		self.show("AC_list")
		self.show("AC_list_OUR")
		self.show("stage_C14")	
		self.update_rect("OUR_rect")
		self.show("OUR_list")
		self.reset_clock()


	def load_DR_to_AR(self):
		self.show("stage_C8")
		self.update_rect("AR_rect")
		self.show("AR_list")
		self.show("Mux1_list")
	
	def load_DR_to_AC(self):
		self.show("stage_C6")
		self.show("AC_load")
		self.update_rect("AC_rect")
		
	def hide_DR_left(self):
		self.hide("DR_list")
		self.hide("DR_list_ARIR")
		self.hide("DR_list_MUX3ARIR")
		self.hide("DR_list_IR")
	
	def show_DR(self,sd=500):
		self.show("DR_list",sd)
		self.show("DR_list_ADDER",sd)
		self.show("DR_list_MUX3ARIR",sd)
		self.show("DR_list_MUX3",sd)
		self.show("Mux3_list")	
		self.show("DR_list_ARIR",sd)
		self.show("DR_list_IR",sd)
		self.show("DR_list_AR",sd)
		self.show("DR_list_RAM",sd)

	def increment_PC(self):
		self.show("stage_C2")
		self.update_rect("PC_rect")
		self.show("stage_C2_MUX2")

	def hide_increment_PC(self):
		self.hide("stage_C2")
		self.hide("stage_C2_MUX2")

	def D(self,number):
		Point_dict["dekoder_point"][number].set_One()
		self.visual(1000)
		self.show("dekoder_out") 
		
	def reset_clock(self):
		self.show("stage_C12")
		self.show("stage_C12_Increment")
		self.hide("stage_C12_Increment_Not")
		self.show("stage_C12_Reset")
		self.update_rect("TC_rect")
		self.hide("TC_list")
		for i in range(6):
			Point_dict["time_point"][i].set_Zero()		

	def rect_set_False(self):
		keys=list(rect_dict.keys())
		for x in keys:
			rect_dict[x][1] = False
		
	def update_rect(self,key,my_delay=1000):
		rect_dict[key][1] = True
		self.visual(my_delay)

	def draw_Rect(self):
		keys=list(rect_dict.keys())
		for x in keys:
			if rect_dict[x][1]:
				draw_Rec(self.getMainWindow(),rect_dict[x][0])

	def show(self,key,my_delay=500):
		for x in Point_dict[key]:
			x.set_One()
			self.visual(my_delay)
	
	def hide_all(self):
		keys=list(Point_dict.keys())
		for x in keys:
			for point in Point_dict[x]:
				point.set_Zero()
		Point_dict["stage_C12_Increment_Not"][0].set_One()
		Point_dict["TC_list"][0].set_One()
		self.visual(0)
			
	def hide(self,key):
		for x in Point_dict[key]:
			x.set_Zero()
		self.visual(0)
		
	def visual(self,my_delay):
		self.check_play()		
		if self.play:
			self.update()
			pygame.display.flip()
			pygame.time.delay(my_delay)
		
	def animation_play(self):
		self.play=True

	def animation_pause(self):
		self.play=False
		while not self.play:
			self.check_play()

	def animation_stop(self):
		self.hide_all()
		self.rect_set_False()
		raise Exception ("End Of Animation!")
	

	def check_play(self):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.Check_Button_isClicked(event.pos,False)
		

