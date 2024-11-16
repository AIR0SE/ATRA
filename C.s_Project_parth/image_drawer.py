import pygame
import pickle
import time
import sys



def neaar_button_red(lst):
    
    (mx,my) = pygame.mouse.get_pos()
    
    location_of_button = 1
    color_of_button    = 0
    
    x_cordinate = 0
    y_cordinate = 1
    
    for info_about_a_button in lst:
         
         location_button = info_about_a_button [ location_of_button ]
         
         x_limit=location_button[x_cordinate] < mx+25 and location_button[x_cordinate] > mx-25
         y_limit=location_button[y_cordinate] < my+25 and location_button[y_cordinate] > my-25
         
         if x_limit and y_limit :
             info_about_a_button[color_of_button]=red
         else:
             info_about_a_button[color_of_button]=black

def content_data(file):
    with open(file,'rb') as f:
        L=pickle.load(f)
    return L


#color
gold      = ( 248,  172,  0)
red       = ( 255,   0,   0)
light_blue= ( 147, 252, 252)
light_pink= ( 202,  10, 244)
black     = (   0,   0,   0)
white     = ( 255, 255, 255)

with open('game_size.txt','r') as f:
    game_size = f.read().split(',')
x = int(game_size[0])    
y = int(game_size[1])    
pygame.init()
full_screen=(x,y)
screen=pygame.display.set_mode(full_screen)

#start
data_file_of_recent_painting = content_data('save1.bat')
data_file_of_recent_painting.pop(0) # removes the intial size of canvas

pressed_save_button_condition=False
sum_sub='+'
background_colour = light_blue
size_of_circle=10
program=True
final_stop=len(data_file_of_recent_painting)-1
interval=0

#with time color of drawer changes

color_sep=0 #color=(255-color_sep,0,color_sep)
clock = pygame.time.Clock()
starting_time = pygame.time.get_ticks()

toggle_command={
    'speed':'slow'
    }

white_canvas_cordinates=(100,100)
white_canvas_size=(600,600)
x_axis=0
y_axis=1
canvas=pygame.Rect(white_canvas_cordinates[x_axis],
                   white_canvas_cordinates[y_axis],
                   white_canvas_size[x_axis],
                   white_canvas_size[y_axis]
                   )
overline=pygame.Rect(white_canvas_cordinates[x_axis]-50,
                     white_canvas_cordinates[y_axis]-50,
                     white_canvas_size[x_axis]+100,
                     white_canvas_size[y_axis]+100      # size increase by 100 as 
                                                        # both ends of rectangle inc 50
                     )

distances_from_y_axis_start_correctionprosses=white_canvas_cordinates[x_axis]+white_canvas_size[x_axis]
screen_size = screen.get_size()

correction=pygame.Rect(700,
                       100,
                       screen_size[x_axis],
                       screen_size[y_axis]      
                     )

head_font = pygame.font.Font('freesansbold.ttf', 48)
canvas_filled_sign = head_font.render('done', True, black)
save_button        = head_font.render('save', True, black)
speed_display      = head_font.render('<>', True, black)

rec_canvas_filled_sign = canvas_filled_sign.get_rect()
rec_save_button        = save_button.get_rect()
rec_speed_display      = speed_display.get_rect() 

screen_size = screen.get_size()
mean_bw_distance_after_canvas  =  (screen_size[x_axis]-white_canvas_size[x_axis]-100)//2
distance_before_canvas=100
com_dis                        =  white_canvas_size[x_axis]+distance_before_canvas
text_position_from_left        =  mean_bw_distance_after_canvas+com_dis

text_position_from_top={'first':100,'second':200,'third':300,'fourth':400}
rec_canvas_filled_sign.center  =  (text_position_from_left,
                                   text_position_from_top['first']
                                   )
rec_save_button.center         =  (text_position_from_left,
                                   text_position_from_top['second']
                                   )
rec_speed_display.center       =  (text_position_from_left,
                                   text_position_from_top['fourth']
                                   )
repaint_background = head_font.render('                  ', True, black,background_colour)

screen.fill(background_colour)
pygame.draw.rect(screen,(255,255,255),canvas)


buttons = { 
    'save_button_color_call':[ black, 
                              (text_position_from_left, text_position_from_top['second'])
                              ]
    }



while program:
    
    speed_display = head_font.render('<{}>'.format(toggle_command['speed']), True, black)
    
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            program=False
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_q:
                
               program=False
            
            elif event.key == pygame.K_z:
                
                if toggle_command['speed'] == 'slow':
                    
                   toggle_command['speed'] = 'normal'
                    
                elif toggle_command['speed'] == 'normal':
                    
                     toggle_command['speed'] = 'fast'
                    
                elif toggle_command['speed'] == 'fast':
                    
                     toggle_command['speed'] = 'slow'
                    
            elif event.key == pygame.K_RETURN:
                
               if  buttons['save_button_color_call'][0] == red:
                   
                   pressed_save_button_condition = True
                   program=False
    
    if interval == final_stop:
        
        save_button        = head_font.render('save', True, buttons['save_button_color_call'][0])
        neaar_button_red(list(buttons.values()))
        
        screen.blit( save_button        , rec_save_button        )
        screen.blit( canvas_filled_sign , rec_canvas_filled_sign )
        screen.blit( repaint_background , rec_speed_display      )
        screen.blit( speed_display      , rec_speed_display      )
        
        pygame.display.flip()
        continue
    
    print(data_file_of_recent_painting)
    print(interval)
    print(final_stop)
    
    circle_cordinate = data_file_of_recent_painting[interval][0]
    size_of_circle   = data_file_of_recent_painting[interval][1]
    color=(255-color_sep,0,color_sep)
    
    #make it a def function input toggle_command['speed'] returns timespan
    if toggle_command['speed']=='slow':
        time_span=25
    elif toggle_command['speed']=='normal':
        time_span=15
    elif toggle_command['speed']=='fast':
        time_span=2
    
    if current_time-starting_time >= time_span:
        if color_sep == 255: 
            sum_sub='-'
        elif color_sep == 0: 
            sum_sub='+'
        exec('color_sep{}=1'.format(sum_sub))
        interval+=1
        starting_time=current_time
    
    
    pygame.draw.circle(screen, color, circle_cordinate, size_of_circle)
    
    pygame.draw.  rect(screen, background_colour,correction,   )
    pygame.draw.  rect(screen, gold             ,overline  , 50)
    pygame.draw.  rect(screen, black            ,canvas    ,  2)
    
    screen.blit( repaint_background, rec_speed_display)
    screen.blit( speed_display     , rec_speed_display)
    
    pygame.display.flip()

#end
pygame.quit()
    