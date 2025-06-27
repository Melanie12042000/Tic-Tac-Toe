import pygame
from pygame.locals import *
pygame.init()
window=pygame.display.set_mode((300,300))
window_color=(255,255,255)
line_color=(0,0,0)
BUTTON_LENGTH=30
BUTTON_HIGHT=34

state=0
running=True
clicked=False
clicked_circles=[]
clicked_cross=[]
button_states=[]

cross=pygame.image.load('cross.png').convert_alpha()
cross=pygame.transform.scale(cross,(BUTTON_LENGTH,BUTTON_HIGHT))

circle=pygame.image.load('circle.png').convert_alpha()
circle=pygame.transform.scale(circle,(BUTTON_LENGTH,BUTTON_HIGHT))

while running:

    pos=pygame.mouse.get_pos()

    window.fill(window_color)




    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()

    #creating Grid
    pygame.draw.line(window,line_color,[100,100],[100,246],3)
    pygame.draw.line(window,line_color,[135,100],[135,246],3)
    pygame.draw.line(window,line_color,[170,100],[170,246],3)

    pygame.draw.line(window,line_color,[69,135],[201,135],3)
    pygame.draw.line(window,line_color,[69,173],[201,173],3)
    pygame.draw.line(window,line_color,[69,211],[201,211],3)

#creating buttons
    

    
            
    
    button1_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button1_surface.fill((255,0,0))
    button1=pygame.Rect(69,100,BUTTON_LENGTH,BUTTON_HIGHT)
    button1=window.blit(button1_surface,(button1.x,button1.y))
    

    button2_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button2_surface.fill((255,0,0))
    button2=pygame.Rect(103,100,BUTTON_LENGTH,BUTTON_HIGHT)
    button2=window.blit(button2_surface,(button2.x,button2.y)) 

    
    button3_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button3_surface.fill((255,0,0))
    button3=pygame.Rect(138,100,BUTTON_LENGTH,BUTTON_HIGHT)
    button3=window.blit(button3_surface,(button3.x,button3.y))

    
    button4_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button4_surface.fill((255,0,0))
    button4=pygame.Rect(173,100,BUTTON_LENGTH,BUTTON_HIGHT)
    button4=window.blit(button4_surface,(button4.x,button4.y)) 
    
    button5_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button5_surface.fill((255,0,0))
    button5=pygame.Rect(69,138,BUTTON_LENGTH,BUTTON_HIGHT)
    button5=window.blit(button5_surface,(button5.x,button5.y))
    

    button6_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button6_surface.fill((255,0,0))
    button6=pygame.Rect(103,138,BUTTON_LENGTH,BUTTON_HIGHT)
    button6=window.blit(button6_surface,(button6.x,button6.y)) 

    
    button7_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button7_surface.fill((255,0,0))
    button7=pygame.Rect(138,138,BUTTON_LENGTH,BUTTON_HIGHT)
    button7=window.blit(button7_surface,(button7.x,button7.y))

    
    button8_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button8_surface.fill((255,0,0))
    button8=pygame.Rect(173,138,BUTTON_LENGTH,BUTTON_HIGHT)
    button8=window.blit(button8_surface,(button8.x,button8.y)) 

    button9_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button9_surface.fill((255,0,0))
    button9=pygame.Rect(69,176,BUTTON_LENGTH,BUTTON_HIGHT)
    button9=window.blit(button9_surface,(button9.x,button9.y))
    

    button10_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button10_surface.fill((255,0,0))
    button10=pygame.Rect(103,176,BUTTON_LENGTH,BUTTON_HIGHT)
    button10=window.blit(button10_surface,(button10.x,button10.y)) 

    
    button11_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button11_surface.fill((255,0,0))
    button11=pygame.Rect(138,176,BUTTON_LENGTH,BUTTON_HIGHT)
    button11=window.blit(button11_surface,(button11.x,button11.y))

    
    button12_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button12_surface.fill((255,0,0))
    button12=pygame.Rect(173,176,BUTTON_LENGTH,BUTTON_HIGHT)
    button12=window.blit(button12_surface,(button12.x,button12.y)) 

    button13_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button13_surface.fill((255,0,0))
    button13=pygame.Rect(69,214,BUTTON_LENGTH,BUTTON_HIGHT)
    button13=window.blit(button13_surface,(button13.x,button13.y))
    

    button14_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button14_surface.fill((255,0,0))
    button14=pygame.Rect(103,214,BUTTON_LENGTH,BUTTON_HIGHT)
    button14=window.blit(button14_surface,(button14.x,button14.y)) 

    
    button15_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button15_surface.fill((255,0,0))
    button15=pygame.Rect(138,214,BUTTON_LENGTH,BUTTON_HIGHT)
    button15=window.blit(button15_surface,(button15.x,button15.y))

    
    button16_surface=pygame.Surface((BUTTON_LENGTH,BUTTON_HIGHT))
    button16_surface.fill((255,0,0))
    button16=pygame.Rect(173,214,BUTTON_LENGTH,BUTTON_HIGHT)
    button16=window.blit(button16_surface,(button16.x,button16.y)) 


    #creating lists with the buttons

    buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16]
    
    #print(circles[0])
   # running=False

    #clicked condition
    
   
    for i in range(16):
             if buttons[i].collidepoint(pos): 
                if pygame.mouse.get_pressed()[0]==1 and clicked==False:
                    clicked=True
                    if state%2==0:
                     clicked_circles.append(buttons[i])
                    elif state%2==1:
                     clicked_cross.append(buttons[i])

                   # button_states.append(str(buttons[i].x) + "," + str(buttons[i].y) + " state: ")
                   # x=buttons[i].x
                  #  y=buttons[i].y
                    print(clicked_circles)
                    print(clicked_cross)
                   # print(button_states)
                

             if clicked and state%2==0:
                 for circles in clicked_circles:
                    window.blit(circle,(circles))
                    state=state+1
             if clicked and state%2==1:
                 for crosses in clicked_cross:
                    window.blit(cross,(crosses))
                    state=state+1
                 
    if pygame.mouse.get_pressed()[0]==0:
        clicked=False
             
    pygame.display.update()