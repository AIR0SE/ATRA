'''
GUI
'''

import pygame
import random
import pickle

#color
shodow_blue= (69, 87, 217)
light_pink= (202, 10, 244)
black=(0,0,0)
red=(255,0,0)


with open('game_size.txt','r') as f:
    game_size = f.read().split(',')
x = int(game_size[0])    
y = int(game_size[1])    
pygame.init()
full_screen=(x,y)
screen=pygame.display.set_mode(full_screen)

#conditions
pressed_draw_button_condition,pressed_artwork_button_condition=False,False

def neaar_button_red(lst):
     for info_about_a_button in lst:
         (mx,my) = pygame.mouse.get_pos()
         location_of_button=1
         color_of_button   =0
         x_axis=0
         y_axis=1
         
         location_button=info_about_a_button[location_of_button]
         x_limit=location_button[x_axis] < mx+25 and location_button[x_axis] > mx-25
         y_limit=location_button[y_axis] < my+25 and location_button[y_axis] > my-25
         if x_limit and y_limit :
             info_about_a_button[color_of_button]=red
         else:
             info_about_a_button[color_of_button]=black

def content_data(file):
    with open(file,'rb') as f:
        L=pickle.load(f)
    return L

def name_OF_selectedfiles():
    with open('game_file_location.txt','r') as f:
        name_of_all_drawing_N=f.readlines()
    name_of_all_drawing=[]
    for i in name_of_all_drawing_N:
        drawing=i.rstrip('\n')
        name_of_all_drawing.append(drawing)
    return name_of_all_drawing

def animation_of(file_name,position) :
    name_of_all_drawing = name_OF_selectedfiles()
    if file_name == 'random':
        file_number=random.randint(0,len(name_of_all_drawing)-1)
    else:
        file_number=name_of_all_drawing.index(file_name+".bat")
    sum_sub='+'
    program=True
    interval=0
    color_sep=0

    center_point=(350,350)
    new_center_point = position
    x_addition=new_center_point[0]-center_point[0]
    y_addition=new_center_point[1]-center_point[1]
    data_file_of_recent_painting = content_data(name_of_all_drawing[file_number])
    data_file_of_recent_painting.pop(0)
    final_stop=len(data_file_of_recent_painting)-1
    screen_animation_data=[]
    while program:
        circle_cordinateX,Y = data_file_of_recent_painting[interval][0]
        circle_cordinateX += x_addition
        Y                 += y_addition
        circle_cordinate = circle_cordinateX,Y
        size_of_circle   = data_file_of_recent_painting[interval][1]
        color=(255-color_sep,0,color_sep)
        screen_animation_data.append((color,circle_cordinate,size_of_circle))
        if color_sep == 255: 
            sum_sub='-'
        elif color_sep == 0: 
            sum_sub='+'
        if sum_sub == '-':
            color_sep-=1
        else:
            color_sep+=1
        print(color_sep)
        interval+=1
        if interval == final_stop - 1 :
            return screen_animation_data
#start
clock = pygame.time.Clock()
starting_time = pygame.time.get_ticks()

current_slide=True

head_font      = pygame.font.Font('freesansbold.ttf', 128 )
options_font   = pygame.font.Font('freesansbold.ttf', 48  )

head_text      = head_font   .render('ATRA'   , True, light_pink )
option1        = options_font.render('Draw'   , True, black      )
option2        = options_font.render('Arworks', True, black      )
option3        = options_font.render('QUIT'   , True, black      )

textRect0 = head_text.get_rect()
textRect1 = option1  .get_rect()
textRect2 = option2  .get_rect()
textRect3 = option3  .get_rect()

CENTER_POSITION=x//2
textRect0.center = (CENTER_POSITION, 100 )
textRect1.center = (CENTER_POSITION, 300 )
textRect2.center = (CENTER_POSITION, 400 )
textRect3.center = (CENTER_POSITION, 500 )

color_op1,color_op2,color_op3=black,black,black
color_toggle=[
     [color_op1,(CENTER_POSITION, 300 )],
     [color_op2,(CENTER_POSITION, 400 )],
     [color_op3,(CENTER_POSITION, 500 )],
     ]
animation_Main_GUI_1 = animation_of('Tree',(x//2,y//2+50))
animation_Main_GUI_2 = animation_of('snowball1',(0,y//2+50))
animation_Main_GUI_3 = animation_of('snowball2',(x,y//2+50))
interval   =  0
time_span  = 25
final_stop_1 = len(animation_Main_GUI_1) - 1
final_stop_2 = len(animation_Main_GUI_2) - 1
final_stop_3 = len(animation_Main_GUI_3) - 1
starting_time = pygame.time.get_ticks()
screen.fill(shodow_blue)

while current_slide:
     
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            current_slide=False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_q:
                
               current_slide=False
               main_program_condition=False
               
            if event.key == pygame.K_RETURN:
                
               if  color_toggle[0][0] == red:
                   
                   pressed_draw_button_condition=True
                   current_slide=False
                   
               elif color_toggle[1][0] == red:
                   
                   pressed_artwork_button_condition=True
                   current_slide=False
                   
               elif color_toggle[2][0] == red:
                   
                   main_program_condition=False
                   current_slide=False

    neaar_button_red(color_toggle)
    option1 = options_font.render('Draw'   , True, color_toggle[0][0])
    option2 = options_font.render('Arworks', True, color_toggle[1][0])
    option3 = options_font.render('QUIT'   , True, color_toggle[2][0])
    if current_time-starting_time >= time_span :
        if interval < final_stop_1:
            screen, color, circle_cordinate, size_of_circle = (screen,) + animation_Main_GUI_1[interval]
            pygame.draw.circle(screen, color, circle_cordinate, size_of_circle)
        if interval < final_stop_2:
            screen, color, circle_cordinate, size_of_circle = (screen,) + animation_Main_GUI_2[interval]
            pygame.draw.circle(screen, color, circle_cordinate, size_of_circle)
        if interval < final_stop_3:
            screen, color, circle_cordinate, size_of_circle = (screen,) + animation_Main_GUI_3[interval]
            pygame.draw.circle(screen, color, circle_cordinate, size_of_circle)
        interval+=1
        starting_time=current_time
    
    screen.blit(head_text, textRect0  )
    screen.blit(option1  , textRect1  )
    screen.blit(option2  , textRect2  )
    screen.blit(option3  , textRect3  )
    
    pygame.display.flip()

#end
       
pygame.quit()
