import pygame
import pickle
import sys

def content_data(file):
    with open(file,'rb') as f:
        L=pickle.load(f)
    return L

#color
white       = (255, 255, 255)     
red         = (238,  38,  21)       
black       = (  0,   0,   0)
pink        = (254, 131, 199) 
shodow_blue = ( 69,  87, 217)

with open('game_size.txt','r') as f:
    game_size = f.read().split(',')
x = int(game_size[0])    
y = int(game_size[1])    
pygame.init()
full_screen=(x,y)
screen=pygame.display.set_mode(full_screen)

#start

def save(data,file_name):
    
    with open('{}.bat'.format(file_name),'wb') as f:
        
        pickle.dump(data,f)
        
    with open("file_location.txt",'a') as f:
        
        f.write('{}.bat\n'.format(file_name))
        

background = shodow_blue
program = True

base_font = pygame.font.Font(None, 32) 
big_base_font = pygame.font.Font(None, 48) 
user_text = '' 
  
input_rect = pygame.Rect(200, 200, 140, 32)

x, y = screen.get_size() 
input_rect.center=(x//2,y//2)
color = white 

name_to_long_error = False
active = False
head_font = pygame.font.Font('freesansbold.ttf', 200)
save_title                 = head_font.render('save', True, red)
error_message_name_to_long = big_base_font.render('name entered is to long \n maximum name can 10 charecters long', True, red)
rec_save_title                 = save_title.get_rect()
rec_error_message_name_to_long = error_message_name_to_long.get_rect()
rec_save_title.center                 = (x//2,200)
rec_error_message_name_to_long.center = (x//2,y//2+30)
screen.fill(background) 
while program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program=False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
                name_to_long_error = False
                
            elif event.key == pygame.K_RETURN:
                if len(user_text) <=10:
                    program=False
                else:
                    name_to_long_error = True
            else: 
                user_text += event.unicode
             
   
    
    screen.fill(background) 
          
    pygame.draw.rect(screen, color, input_rect) 
  
    text_surface = base_font.render(user_text, True, pink) 
    screen.blit(save_title, rec_save_title) 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
    input_rect.w = max(100, text_surface.get_width()+10) 
    
    if name_to_long_error:
        screen.blit(error_message_name_to_long, rec_error_message_name_to_long)   
    pygame.display.flip()
L=content_data('save1.bat')
save(L,user_text)
#end

pygame.quit()