import pygame
import time
import random
import sys

WIDTH = 450
HEIGHT = 500
FPS = 30

WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)
BLACK=(0,0,0)


def build_grid(x, y, w):
    for i in range(1,21):
        x = 20                                                
        y = y + 20                                                    
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])         
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])        
            grid.append((x,y))                                          
            x = x + 20                                              

def push_up(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1, 19, 39), 0)     
    pygame.display.update()                                          

def push_down(x, y):
    pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()

def push_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()

def push_right(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 39, 19), 0)
    pygame.display.update()

def single_cell( x, y):
    pygame.draw.rect(screen, GREEN, (x +1, y +1, 18, 18), 0)      
    pygame.display.update()

def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 18, 18), 0)        
    pygame.display.update()                                      

def solution_cell(x,y):
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)         
    pygame.display.update()                                      
def carve_out_maze(x,y):
    single_cell(x, y)                                           
    stack.append((x,y))                                          
    visited.append((x,y))                                  
    while len(stack) > 0:                                          
        time.sleep(.00)                                       
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:      
            cell.append("right")                                 

        if (x - w, y) not in visited and (x - w, y) in grid:     
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:     
            cell.append("up")

        if len(cell) > 0:                           
            cell_chosen = (random.choice(cell))           

            if cell_chosen == "right":                       
                push_right(x, y)                       
                solution[(x + w, y)] = x, y                      
                x = x + w                                
                visited.append((x, y))                      
                stack.append((x, y))                          

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                            
            single_cell(x, y)                                 
            time.sleep(.05)                                      
            backtracking_cell(x, y)                             

def plot_route_back(x,y):
    solution_cell(x,y)  
                                          
    while (x, y) != (20,20):
    
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 20
                elif event.key == pygame.K_RIGHT:
                    x += 20
                elif event.key == pygame.K_UP:
                    y -= 20
                elif event.key == pygame.K_DOWN:
                    y += 20
                elif event.key == pygame.K_ESCAPE:
                        sys.exit()
        solution_cell(x, y)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()
font=pygame.font.Font(None,36)

text = font.render("Press any key to start the game", True, WHITE)
screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
pygame.display.flip()
text = font.render("TO QUIT PRESS ESC ", True, WHITE)
screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//1.2 - text.get_height()//2))
pygame.display.flip()


    ####### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
            else:
                screen.fill(BLACK)
                x = 0                    
                y = 0                    
                w = 20                 
                grid = []
                visited = []
                stack = []
                solution = {}
                done = False


                x, y = 20, 20                 
                build_grid(40, 0, 20)           
                carve_out_maze(x,y)            
                plot_route_back(400, 400)        

                screen.fill(BLACK)
        
                # Check if player has reached (0, 0)
                if x == 20 and y == 20:
                    text = font.render("TO QUIT PRESS ESC ", True, WHITE)
                    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//1.2 - text.get_height()//2))
                # pygame.display.flip()
                    text = font.render("Game Over", True, WHITE)
                    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
                pygame.display.flip()
                clock.tick(FPS)
                    


   
