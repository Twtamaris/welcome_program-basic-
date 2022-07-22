from cgitb import text
import pygame
from pygame import mixer

pygame.init()
pygame.font.init()
width = 1250
height = 650
timer = pygame.time.Clock()
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Welcome Program 2078 by 2077")
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (50, 50, 50)
light_gray = (170, 170, 170)
blue = (0, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
gold = (212, 175, 55)
label_font = pygame.font.SysFont('arial.ttf', 32)
medium_font = pygame.font.SysFont('arial.ttf', 24)
x = 0
apple1 = ''
apple2 = ''
apple3 = ''
apple4 = ''
apple5= ''
text_file = open('hello.txt', 'r')
a = 0
b = 0

list1 = []
for i in text_file:
    list1.append(i)


run = True
while run:
    timer.tick(60)
    screen.fill(black)
    keys_pressed = pygame.key.get_pressed()
    
            
    name = pygame.draw.rect(screen, light_gray, [width//4, height//4 - 50, 200, 40], 4, 5)
    menu_text = label_font.render('Name:', 1, white)
    screen.blit(menu_text, (width//4, height//4 - 70))
    
    roll = pygame.draw.rect(screen, light_gray, [width//4, height//4 + 50, 200, 40], 4, 5)
    menu_text = label_font.render('Roll No:', 1, white)
    screen.blit(menu_text, (width//4, height//4 - 70 + 100))
    
    faculty = pygame.draw.rect(screen, light_gray, [width//4, height//4 + 50 + 100, 200, 40], 4, 5)
    menu_text = label_font.render('Faculty', 1, white)
    screen.blit(menu_text, (width//4, height//4 - 70+ 200))
    
    amount = pygame.draw.rect(screen, light_gray, [width//4, height//4 + 50 + 100 + 100, 200, 40], 4, 5)
    menu_text = label_font.render('Amount:', 1, white)
    screen.blit(menu_text, (width//4, height//4 - 70+ 300))
    
    screenshot = pygame.draw.rect(screen, light_gray, [width//4, height//4 - 50 + 100 + 300, 200, 40], 4, 5)
    menu_text = label_font.render('Upload Screenshot of Esewa/Khalti', 1, white)
    screen.blit(menu_text, (width//4, height//4 - 70+ 400))
    
    save = pygame.draw.rect(screen, light_gray, [width//4, height//4 - 80 + 100 + 400, 100, 40], 0, 5)
    menu_text = label_font.render('Save', 1, white)
    screen.blit(menu_text, (width//4+ 20, height//4 - 70+ 500))
    
    load = pygame.draw.rect(screen, light_gray, [width//4 + 150, height//4 - 80 + 100 + 400 , 100, 40], 0, 5)
    menu_text = label_font.render('Load', 1, white)
    screen.blit(menu_text, (width//4+ 20 + 150, height//4 - 70+ 500))
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if name.collidepoint(event.pos):
                x = 1
                
                
            if roll.collidepoint(event.pos):
                x = 2
            if faculty.collidepoint(event.pos):
                x = 3
            if amount.collidepoint(event.pos):
                x = 4
            if screenshot.collidepoint(event.pos):
                x = 5
                
                
            if save.collidepoint(event.pos):
                
                text_file = open('hello.txt', 'w')
                list1.append(f'Name: {apple1}, Roll No: {apple2},, Faculty: {apple3},,, Amount: {apple4},,,, Screenshot: {apple5}\n')
                for i in range(len(list1)):
                    text_file.write(str(list1[i]))
      
                apple1 = ''
                apple2 = ''
                apple3 = ''
                apple4 = ''
                apple5= ''
                
                
            if load.collidepoint(event.pos):
                a = 1
                
                
                
               
                
                
 
                
                
                
                
        if event.type == pygame.TEXTINPUT and x == 1:
            apple1 += event.text
        
            
        if event.type == pygame.TEXTINPUT and x == 2:
            apple2 += event.text
            
        if event.type == pygame.TEXTINPUT and x == 3:
            apple3 += event.text
        
        if event.type == pygame.TEXTINPUT and x == 4:
            apple4 += event.text
        
        if event.type == pygame.TEXTINPUT and x == 5:
            apple5 += event.text
            
        
            
        if keys_pressed[pygame.K_BACKSPACE]:
            if x == 1:
                apple1 = apple1[:-1]
                
            if x == 2:
                apple2 = apple2[:-1]
                
            if x == 3:
                apple3 = apple3[:-1]
                
            if x == 4:
                apple4 = apple4[:-1]
                
            if x == 5:
                apple5 = apple5[:-1]
                
                
    
            
    
        
            
            
            
            
    
    if x == 1:
        pygame.draw.rect(screen, light_gray, [width//4, height//4 - 50, 200, 40], 0, 5)
    menu_text = label_font.render(apple1, 1, white)
    screen.blit(menu_text, (width//4 + 20, height//4 - 40))
        
    
    if x == 2:
        pygame.draw.rect(screen, light_gray, [width//4, height//4 + 50, 200, 40], 0, 5)
    menu_text = label_font.render(apple2, 1, white)
    screen.blit(menu_text, (width//4 + 20, height//4 - 40 + 100))
        
    if x == 3:
        pygame.draw.rect(screen, light_gray, [width//4, height//4 + 50 + 100, 200, 40], 0, 5)
    menu_text = label_font.render(apple3, 1, white)
    screen.blit(menu_text, (width//4 + 20, height//4 - 40 + 200))
        
        
    if x == 4:
        pygame.draw.rect(screen, light_gray, [width//4, height//4 + 50 + 100 + 100, 200, 40], 0, 5)
    menu_text = label_font.render(apple4, 1, white)
    screen.blit(menu_text, (width//4 + 20, height//4 - 40 + 300))
        
        
    if x == 5:
        pygame.draw.rect(screen, light_gray, [width//4, height//4 - 50 + 100 + 300, 200, 40], 0, 5)
    menu_text = label_font.render(apple5, 1, white)
    screen.blit(menu_text, (width//4 + 20, height//4 - 40+ 400))
    
    if a==1:
        screen.fill(black)    
        back =pygame.draw.rect(screen, light_gray, [width//4 + 150, height//4 - 80 + 100 + 400 , 100, 40], 0, 5)
        menu_text = label_font.render('Back', 1, white)
        screen.blit(menu_text, (width//4+ 20 + 150, height//4 - 70+ 500))
        
         
        
    if keys_pressed[pygame.K_ESCAPE]:
        run = False
        
    for i in range(len(list1)):
        slice1 = list1[i].index('Name: ') + 6
        slice2 = list1[i].index(', ')
        name = (list1[i][slice1:slice2])
        
        slice3 = list1[i].index('Roll No: ') + 9
        slice4 = list1[i].index(',, ')
        
        
        roll = (list1[i][slice3:slice4])
        
        
        
 
        if a == 1:
            
        
            
            menu_text = label_font.render(name, 1, white)
            screen.blit(menu_text, (width//4+ 20 + 150, height//4 + i*50))
            menu_text = label_font.render(roll, 1, white)
            screen.blit(menu_text, (width//4+ 20 , height//4 + i*50))
            
           
            
                    
            
        
        
        
        
    

    
        
          
                
                
                
            
        
            
    
    pygame.display.update()

    