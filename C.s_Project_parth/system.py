'''
system
'''

import pygame
import pickle
import sys
import random
import time

#colors
white       = (255, 255, 255)
pink        = (254, 131, 199)
shodow_blue = ( 69,  87, 217)
light_blue  = (147, 252, 252)
light_pink  = (202,  10, 244)
black       = (  0,   0,   0)
red         = (255,   0,   0)
gold        = (248, 172,   0)


with open('game_size.txt','r') as f:
    game_size = f.read().split(',')
x = int(game_size[0])    
y = int(game_size[1])    
pygame.init()
full_screen=(x,y)
screen=pygame.display.set_mode(full_screen)

#conditions
main_program_condition=True
pressed_draw_button_condition=False
pressed_artwork_button_condition=False
pressed_save_button_condition=False
sysquit=False
def add_in_file(item,mode):
    if mode == 'binary':
        with open('fileBat.bat','ab+') as f:
            pickle.dump(item,f)
    elif mode == 'text':
        with open('fileText.txt','a') as f:
            f.write('{}\n'.format(item))

def test_for_speed_best_mode(item):
    t0 = time.time()
    for i in range(100):
        add_in_file(item,'binary')
    give_arry('binary')
    t1 = time.time()
    time_binary=t1-t0
    t0 = time.time()
    for i in range(100):
        add_in_file(item,'text')
    give_arry('text')
    t1 = time.time()
    time_text=t1-t0
    if time_binary > time_text:
        return 'binary'
    return 'text'
            
def give_arry(mode):
    """
    the code below
    manipulates the data recived by the file.bat such that all mouse position are unique
    and then store it temporary in save1.dat
    """
    if mode == 'binary':
        l=[(700,700)] #the l[0] acts as a canvas size 
        with open('fileBat.bat','rb+') as f:
            try:
                while 1:
                    mos_pos=pickle.load(f)
                    
                    change_in_mouse_pos= mos_pos == l[-1]
                    
                    if change_in_mouse_pos:
                        continue
                    l.append(mos_pos)
            except Exception:
                 pass
    elif mode == 'text':
        l=[(700,700)] #the l[0] acts as a canvas size 
        with open('fileText.txt','r+') as f:
            L=f.read().split('\n')
            interval=0
            try:
                while 1:
                    mos_pos=eval(L[interval])
                    print(interval)
                    
                    change_in_mouse_pos= mos_pos == l[-1]
                    interval+=1
                    if change_in_mouse_pos:
                        continue
                    l.append(mos_pos)
            except Exception:
                 pass
    return l


def color_change(mouse_postion,color_sep,sum_sub):
            print(mouse_postion,color_sep,sum_sub)   
            if len(mouse_postion) == 1:
                pass
            elif mouse_postion[-2]!=mouse_postion[-1] :
                print(1)
                exec('color_sep{}=1'.format(sum_sub))
                print(color_sep)
                return color_sep
            else:
                mouse_postion.clear()
            print(color_sep)
            return color_sep
        
def color_rotion(color_sep):
    if color_sep == 255: 
        sum_sub='-'
    elif color_sep == 0: 
        sum_sub='+'
    return sum_sub

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

def readpyfile(file):
    with open(file,'r') as f:
        l=f.readlines()
        start=0
        end=len(l)
        
        for i in range(len(l)):
            if l[i]=='#start\n':
                #print('how')
                start=i
            elif l[i]=='#end\n':
                end=i
        #print(start,end)
        f.seek(0)
        lines_of_code=f.readlines()[start:end]
        string_form='\n'.join(lines_of_code)
        #print(string_form)
        return string_form

with open('fileBat.bat','wb') as f:
    pass
with open('fileText.txt','w') as f:
    pass

mode = test_for_speed_best_mode(((0,0),0))
        
while main_program_condition:
    #open main menu 
    exec(readpyfile('parth_projectCs.py'))
    
    if pressed_draw_button_condition:
        
        exec(readpyfile('image_recorder.py'))
        exec(readpyfile('image_drawer.py'))
        
        if pressed_save_button_condition:
            
            exec(readpyfile('artwork_storer.py'))
            
    if pressed_artwork_button_condition:
        
        exec(readpyfile('artwork_display.py'))
    
    pressed_draw_button_condition,pressed_artwork_button_condition=False,False 
    pressed_save_button_condition=False
pygame.quit()    
sys.exit()        
    
