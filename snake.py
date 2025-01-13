import pygame


pygame.init

screen = pygame.display.set_mode((400, 600))
color = (42, 12, 24)
screen.fill(color)
pygame.display.flip()

pygame.display.set_caption("Hello world")
x = 150
y = 250

move_x = 0.01
move_y = 0

car_color = (255, 80, 50)

pygame.draw.rect(screen, (car_color), [x, y, 10, 10], 10)
pygame.display.update()

visited_coords = {(0,0)}

running = True

last_key = pygame.K_RIGHT

while running:
 for event in pygame.event.get(): 
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:  
           running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_UP and last_key is not pygame.K_DOWN:
                    last_key = pygame.K_UP
                    move_y = -.05
                    move_x = 0
                    print("Up")
                    
            elif event.key == pygame.K_DOWN and last_key is not pygame.K_UP:
                    last_key = pygame.K_DOWN
                    move_y = +.05
                    move_x = 0
                    print("Down")                    
                    
            elif event.key == pygame.K_LEFT and last_key is not pygame.K_RIGHT:
                    last_key = pygame.K_LEFT
                    move_x = -.05
                    move_y = 0
                    print("Left")

            elif event.key == pygame.K_RIGHT and last_key is not pygame.K_LEFT:
                    last_key = pygame.K_RIGHT
                    move_x = +.05
                    move_y = 0
                    print("Right")                                        
 


 if x >= 400 or x <= 0 or y >= 600 or y <= 0:
        print("Explosion")
        running = False

 x += move_x
 y += move_y


 
 
 #screen.fill(color)      
 pygame.draw.rect(screen, (car_color), [x, y, 10, 10], 0)        
 pygame.display.update()
 
 if (x,y) in visited_coords:
        running = False 

 visited_coords.add((x,y))

#add surface



