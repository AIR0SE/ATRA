import pygame
import pickle
import sys
import time
#color
light_blue = (147, 252, 252)
light_pink = (202,  10, 244)
black      = (  0,   0,   0)
white      = (255, 255, 255)
    
with open('game_size.txt','r') as f:
    game_size = f.read().split(',')
x = int(game_size[0])    
y = int(game_size[1])    
pygame.init()
full_screen=(x,y)
screen=pygame.display.set_mode(full_screen)



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

with open('fileBat.bat','wb') as f:
    pass
with open('fileText.txt','w') as f:
    pass

mode = test_for_speed_best_mode(((0,0),0))

#start

with open('fileBat.bat','wb') as f:
    pass
with open('fileText.txt','w') as f:
    pass

color_sep=0
clock = pygame.time.Clock()
starting_time = pygame.time.get_ticks()
background_colour = light_blue
white_canvas=(600,600)
size_of_circle=5
program=True


toggle_command={
    'pause':False  
    }

rec_size              = pygame.Rect(100,100,600,600)
head_font             = pygame.font.Font('freesansbold.ttf', 48)
pause_sign            = head_font.render('Pause', True, (0,0,0))
rec_pause_sign        = pause_sign.get_rect()
rec_pause_sign.center = (x-200,100)
color_display_cords   = (x-400,y-500)
mouse_postion=[]

while program:
    
    current_time = pygame.time.get_ticks()
    
    color_of_display=(255-color_sep,0,color_sep)
    screen.fill(background_colour)
    pygame.draw.rect(screen, white, rec_size,   )
    pygame.draw.rect(screen, black, rec_size, 2 )
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            program=False
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_q:
                
                program=False
            
            elif event.key == pygame.K_z:
                
                if toggle_command['pause'] == False:
                    
                    toggle_command['pause'] = True
                    
                else:
                    
                    toggle_command['pause'] = False
            
            elif event.key == pygame.K_x:
                
                size_of_circle+=10
                
            elif event.key == pygame.K_c:
                
                if size_of_circle <=10:
                    continue
                
                size_of_circle-=10
    
    sum_sub=color_rotion(color_sep)        #each time it hits 255 or 0 the color_sep
                                           #decreases negitively or increases positively
    if toggle_command['pause']:
        # code when program is pause
        screen.blit(pause_sign, rec_pause_sign) 
        continue
    
    mx,my = pygame.mouse.get_pos()
    
    mouse_not_in_canvas= mx > 700 or mx < 100 or my > 700 or my < 100
    
    if mouse_not_in_canvas:
        continue
    
    add_in_file(((mx,my),size_of_circle),mode)

    mouse_postion.append((mx,my))
    color_sep=color_change(mouse_postion,color_sep,sum_sub) # the function should give +1 increase color_step
                                                            # if mouse_pos is changed    
    circle_cordinate=(mx,my)
    pygame.draw.circle(screen, color_of_display, color_display_cords,             50, )
    pygame.draw.circle(screen, color_of_display, circle_cordinate   , size_of_circle, )
    pygame.draw.circle(screen, black           , circle_cordinate   , size_of_circle,6)
    pygame.display.flip()

l=give_arry(mode)
with open('save1.bat','wb') as f:
    pickle.dump(l,f)
#end

pygame.quit()