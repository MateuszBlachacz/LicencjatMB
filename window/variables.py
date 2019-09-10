import pygame
from .Point import Point

file_name = "saved_computer.txt"
kMYK = 200
button_create_list = {"btn1":("  INA",(0+kMYK,0),(40,30),"INA","red","button1","button4"),
"btn2":(" CMA",(50+kMYK,0),(40,30),"CMA","blue","button1","button4"),
"btn3":("  LDI",(100+kMYK,0),(40,30),"LDI","green","button1","button4"),
"btn4":("  ADI",(150+kMYK,0),(40,30),"ADI","blue","button1","button4"),
"btn5":(" LDA",(200+kMYK,0),(40,30),"LDA","blue","button1","button4"),
"btn6":("  STA",(250+kMYK,0),(40,30),"STA","blue","button1","button4"),
"btn7":("  INP",(300+kMYK,0),(40,30),"INP","blue","button1","button4"),
"btn8":(" OUT",(350+kMYK,0),(40,30),"OUT","blue","button1","button4"),
"btn_Play":(" Play",(45,60),(60,30),"Play","blue","button1","button4"),
"btn_Pause":(" Pause",(45,90),(60,30),"Pause","blue","button1","button4"),
"btn_Stop":(" Stop",(45,120),(60,30),"Stop","blue","button1","button4")}


time_point = [Point(207, 440), Point(231, 440), Point(254, 440), Point(278, 440), Point(301, 440),Point(324, 440)]
dekoder_point =[Point(347, 328), Point(324, 328), Point(301, 328), Point(277, 328), Point(254, 328), Point(231, 328), Point(207, 328), Point(184, 328)]
dekoder_out = [Point(368, 385), Point(390, 385)]


stage_C1 = [Point(348, 66), Point(369, 66), Point(387, 66), Point(407, 66), Point(424, 66)]
stage_C1_load = [Point(410, 277), Point(424, 277), Point(438, 277)]
stage_C1_MUX1 = [Point(359, 77)]
stage_C2 = [Point(146, 98), Point(161, 98), Point(177, 98), Point(194, 98), Point(212, 98)]
stage_C2_MUX2 =[Point(303, 98), Point(315, 98)] 
stage_C3 = [Point(146, 238), Point(161, 238), Point(177, 238), Point(194, 238), Point(212, 238)]
stage_C4 = [Point(429, 517), Point(445, 517), Point(465, 517), Point(485, 517), Point(505, 517), Point(520, 517)]
stage_C5 = [Point(429, 540), Point(445, 540), Point(465, 540), Point(485, 540), Point(505, 540), Point(520, 540)]
stage_C6 = [Point(428, 502), Point(444, 502), Point(456, 502)]
stage_C7 = [Point(426, 484)]
stage_C7_Load =[Point(452, 484)]
stage_C7_Select = [Point(436, 473), Point(436, 459), Point(436, 438),
Point(450, 431), Point(467, 431), Point(485, 431), Point(504, 431)]
stage_C8 = [Point(146, 175), Point(161, 175), Point(177, 175), Point(194, 175), Point(212, 175)]
stage_C9 = [Point(410, 259), Point(438, 259)]
stage_C9_Select = [Point(421, 243), Point(421, 227), Point(421, 211), Point(437, 198), Point(455, 198),
Point(475, 198), Point(497, 198), Point(516, 198), Point(533, 198)]
stage_C10_RAM = [Point(425, 84)]
stage_C10 = [Point(410, 268), Point(424, 268), Point(438, 268)]
stage_C11 = [Point(432, 136), Point(447, 136), Point(463, 136), Point(480, 136)]
stage_C12_Increment_Not = [Point(213, 541,(255,0,0),3)]
stage_C12 = [Point(133, 524)]
stage_C12_Reset = [Point(150, 524), Point(161, 524), Point(180, 524), Point(196, 524), Point(209, 524), Point(225, 524)]
stage_C12_Increment = [Point(141, 534), Point(151, 541), Point(159, 541)] 
stage_C13 = [Point(428, 446)]
stage_C13_Load = [Point(445, 459), Point(445, 473), Point(455, 491)]
stage_C13_Select = [Point(454, 446), Point(467, 446), Point(485, 446), Point(504, 446)]
stage_C14 = [Point(491, 611), Point(506, 611), Point(525, 611)]

DR_list = [Point(584, 292)]
DR_list_ADDER = [Point(584, 314)]
DR_list_MUX3ARIR = [Point(565, 300), Point(547, 300)]
DR_list_MUX3 = [Point(537, 316), Point(537, 328), Point(537, 344), Point(537, 363), Point(537, 378), Point(537, 399)]
DR_list_ARIR = [Point(521, 300), Point(498, 300), Point(473, 300),
Point(447, 300), Point(420, 300), Point(400, 300), Point(379, 300),
Point(374, 280), Point(374, 258), Point(374, 237), Point(374, 222),
Point(358, 206), Point(334, 206), Point(303, 206), Point(281, 206)]
DR_list_AR= [Point(266, 196)]
DR_list_IR= [Point(266, 217)]
DR_list_RAM = [Point(602, 299), Point(617, 299), Point(629, 299),
Point(645, 299), Point(655, 289), Point(655, 272), Point(655, 248),
Point(655, 228), Point(655, 208), Point(655, 181), Point(655, 151),
Point(655, 115), Point(655, 87), Point(655, 67), Point(643, 52),
Point(622, 52), Point(607, 52), Point(591, 52), Point(574, 52), 
Point(561, 56)]
DR_load =[Point(495, 268), Point(512, 268), Point(529, 268), Point(543, 268)]

AR_list = [Point(266, 148), Point(266, 135), Point(277, 128), Point(290, 128), Point(309, 128)]
Ram_list = [Point(561, 157)]
Ram_read = [Point(480, 74)]
Adder_list = [Point(584, 393)]
Mux3_list = [Point(561, 467)]
Mux2_list = [ Point(584, 227), Point(584, 239)]
Mux1_list = [Point(399, 113), Point(417, 113), Point(436, 113), Point(455, 113), Point(471, 113), Point(484, 113)]
TC_list = [Point(266, 503,(255,0,0),3)]



IR_list = [Point(266, 266), Point(266, 279)]
AC_list =[Point(561, 562)]
AC_list_OUR=[Point(561, 588)]
AC_list_ADDERMUX2=[Point(585, 579), Point(605, 579), Point(625, 579), 
Point(638, 556), Point(638, 527), Point(638, 494), Point(638, 466), Point(638, 440), 
Point(638, 420), Point(638, 396), Point(638, 367), Point(638, 347), Point(638, 332)]
AC_list_ADDER = [Point(628, 316), Point(616, 316), Point(608, 325)]
AC_list_MUX2 = [Point(638, 285), Point(638, 265), Point(638, 246), Point(638, 222),
Point(638, 203), Point(638, 183), Point(632, 159), Point(617, 159), Point(608, 172)]
AC_load = [Point(511, 493)]

INR_IN = [Point(390, 663), Point(390, 645)]
INR_list=[Point(390, 579), Point(390, 558),
Point(390, 533), Point(390, 505), Point(390, 480), Point(390, 452),
Point(390, 427), Point(390, 405), Point(417, 392), Point(448, 392),
Point(477, 392), Point(498, 392), Point(513, 392), Point(531, 392),
Point(549, 392), Point(561, 399)]
OUR_list=[Point(561, 636), Point(561, 653)]

PC_rect = ((234, 82),(63,31))
AR_rect = ((235, 160),(63,31))
IR_rect = ((235, 222),(63,31))
DR_rect = ((552, 253),(63,31))
INR_rect= ((358, 594),(63,31))
OUR_rect= ((529, 595),(63,31))
TC_rect = ((234, 517),(63,31))
MUX1_rect = ((327, 90),(63,47))
MUX2_rect= ((552, 176),(63,48))
MUX3_rect= ((529, 408),(63,47))
ADDER_rect = ((552, 331),(63,47))
AC_rect = ((529, 486),(63,63))
RAM_rect = ((499, 67),(124,77)) 


Point_dict = {"time_point":time_point,"dekoder_point":dekoder_point,"dekoder_out":dekoder_out,
"stage_C1":stage_C1,"stage_C1_load":stage_C1_load,"stage_C1_MUX1":stage_C1_MUX1,
"stage_C2":stage_C2,"stage_C2_MUX2":stage_C2_MUX2,
"stage_C3":stage_C3,"stage_C4":stage_C4,"stage_C5":stage_C5,"stage_C6":stage_C6,
"stage_C7":stage_C7,"stage_C7_Load":stage_C7_Load,"stage_C7_Select":stage_C7_Select,
"stage_C8":stage_C8,"stage_C9":stage_C9,"stage_C9_Select":stage_C9_Select,"stage_C10":stage_C10,"stage_C10_RAM":stage_C10_RAM,"stage_C11":stage_C11,
"stage_C12_Increment_Not":stage_C12_Increment_Not,"stage_C12":stage_C12,"stage_C12_Reset":stage_C12_Reset,"stage_C12_Increment":stage_C12_Increment,
"stage_C13":stage_C13,"stage_C13_Load":stage_C13_Load,"stage_C13_Select":stage_C13_Select,"stage_C14":stage_C14,
"DR_list":DR_list,"DR_list_ADDER":DR_list_ADDER,
"DR_list_MUX3ARIR":DR_list_MUX3ARIR,"DR_list_MUX3":DR_list_MUX3,"DR_list_ARIR":DR_list_ARIR,
"DR_list_AR":DR_list_AR,"DR_list_IR":DR_list_IR,"DR_list_RAM":DR_list_RAM,"DR_load":DR_load,
"AR_list":AR_list,
"Ram_list":Ram_list,"Ram_read":Ram_read,"Adder_list":Adder_list,
"Mux3_list":Mux3_list,"Mux2_list":Mux2_list,"Mux1_list":Mux1_list,
"TC_list":TC_list,"AC_list":AC_list,"IR_list":IR_list,"AC_list_OUR":AC_list_OUR,"AC_list_ADDERMUX2":AC_list_ADDERMUX2,
"AC_list_ADDER":AC_list_ADDER,"AC_list_MUX2":AC_list_MUX2,"AC_load":AC_load,"INR_IN":INR_IN,"INR_list":INR_list,"OUR_list":OUR_list
}

rect_dict={"PC_rect":[PC_rect,False],"AR_rect":[AR_rect,False],"IR_rect":[IR_rect,False],"DR_rect":[DR_rect,False],
"INR_rect":[INR_rect,False],"OUR_rect":[OUR_rect,False],"TC_rect":[TC_rect,False],"MUX1_rect":[MUX1_rect,False],"MUX2_rect":[MUX2_rect,False],
"MUX3_rect":[MUX3_rect,False],"ADDER_rect":[ADDER_rect,False],"AC_rect":[AC_rect,False],"RAM_rect":[RAM_rect,False]}

tt_list = [time_point,dekoder_point,dekoder_out]

draw_list = []

#do not delate
task_list = {}

#to delate
tmp_list = []

