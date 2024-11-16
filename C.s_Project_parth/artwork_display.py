'''
artwork looker
'''
import pygame
import pickle

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

gold=(248, 172, 0)
red=(255,0,0)
light_blue= (147, 252, 252)
light_pink=(202, 10, 244)
black=(0,0,0)
white=(255,255,255)

with open('game_size.txt','r') as f:
    game_size = f.read().split(',')
x = int(game_size[0])    
y = int(game_size[1])    
pygame.init()
full_screen=(x,y)
screen=pygame.display.set_mode(full_screen)

#start

def name_OF_files():
    with open('file_location.txt','r') as f:
        name_of_all_drawing_N=f.readlines()
    name_of_all_drawing=[]
    for i in name_of_all_drawing_N:
        drawing=i.rstrip('\n')
        name_of_all_drawing.append(drawing)
    return name_of_all_drawing

name_of_all_drawing = name_OF_files()

back=False
front=False
sum_sub='+'
background_colour = light_blue
size_of_circle=10
program=True
interval=0
color_sep=0
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
right_direction       = head_font.render('press n --->', True, black)
left_direction        = head_font.render('press b <---', True, black)
speed_display         = head_font.render('<>', True, black)
painting_name_display = head_font.render('<>', True, black)

rec_right_direction       = right_direction.get_rect()
rec_left_direction        = left_direction.get_rect()
rec_speed_display         = speed_display.get_rect() 
rec_painting_name_display = painting_name_display.get_rect()

screen_size = screen.get_size()
mean_bw_distance_after_canvas  =  (screen_size[x_axis]-white_canvas_size[x_axis]-100)//2
distance_before_canvas=100
com_dis                        =  white_canvas_size[x_axis]+distance_before_canvas
text_position_from_left        =  mean_bw_distance_after_canvas+com_dis

text_position_from_top={'first':100,'second':200,'third':300,'fourth':400}
rec_right_direction.center  =  (text_position_from_left,
                                   text_position_from_top['first']
                                   )
rec_left_direction.center         =  (text_position_from_left,
                                   text_position_from_top['second']
                                   )
rec_painting_name_display.center  =  (text_position_from_left,
                                   text_position_from_top['third']
                                   )
rec_speed_display.center       =  (text_position_from_left,
                                   text_position_from_top['fourth']
                                   )
screen.fill(background_colour)
pygame.draw.rect(screen,white,canvas)

file_number=0
data_file_of_recent_painting = content_data(name_of_all_drawing[file_number])
data_file_of_recent_painting.pop(0)
final_stop=len(data_file_of_recent_painting)-1
last_indix_file=len(name_of_all_drawing)-1
while program:
    painting_name_display = head_font.render('<{}>'.format(name_of_all_drawing[file_number].rstrip('.bat')), True, black)
    speed_display = head_font.render('<{}>'.format(toggle_command['speed']), True, black)
    if back or front:
            screen.fill(background_colour)
            pygame.draw.rect(screen,white,canvas)
            if back and file_number>0 :
                file_number-=1
            if front and file_number < last_indix_file:
                file_number+=1
            interval=0
            color_sep=0
            data_file_of_recent_painting = content_data(name_of_all_drawing[file_number])
            data_file_of_recent_painting.pop(0)
            final_stop=len(data_file_of_recent_painting)-1
            back=False
            front=False
    if toggle_command['speed']=='slow':
        time_span=25
    elif toggle_command['speed']=='normal':
        time_span=15
    elif toggle_command['speed']=='fast':
        time_span=2
    current_time = pygame.time.get_ticks()
    circle_cordinate = data_file_of_recent_painting[interval][0]
    size_of_circle   = data_file_of_recent_painting[interval][1]
    color=(255-color_sep,0,color_sep)
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
            elif event.key == pygame.K_b:
                back=True
            elif event.key == pygame.K_n:
                front=True
    pygame.draw.rect(screen,background_colour,correction)
    screen.blit(left_direction, rec_left_direction)
    screen.blit(right_direction, rec_right_direction)
    screen.blit(painting_name_display, rec_painting_name_display)

    pygame.draw.circle(screen,color,circle_cordinate,size_of_circle)
    pygame.draw.rect(screen,gold,overline,50)
    pygame.draw.rect(screen,(0,0,0),canvas,2)
    screen.blit(speed_display, rec_speed_display)
    pygame.display.flip()
    if current_time-starting_time >= time_span and interval < final_stop - 1 :
        if color_sep == 255: 
            sum_sub='-'
        elif color_sep == 0: 
            sum_sub='+'
        exec('color_sep{}=1'.format(sum_sub))
        interval+=1
        starting_time=current_time
#end
pygame.quit()