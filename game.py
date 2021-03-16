import pygame
import math
import random

WIN_WIDTH, WIN_HEIGHT = 500,500
SCREEN = (WIN_WIDTH, WIN_HEIGHT)
grid_width, gird_height = 50,50


class Grid():
    def __init__(self):
        self.coords = []
        

    def make_grid(self):
        for i in range(0,WIN_WIDTH, 10):
            for j in range(10,WIN_HEIGHT, 10):
                self.coords.append((i,j))

    
    def draw_grid(self, win):
        for cor in self.coords:
            r = pygame.Rect((cor[0], cor[1]), (10, 10))
            pygame.draw.rect(win, 'green', r, 1)
    
    

class Box():
    WIDTH = 10
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_box(self,win):
         rect = pygame.Rect((self.x, self.y), (self.WIDTH-1, self.WIDTH-1))
         pygame.draw.rect(win, 'white', rect)
class Snake():
    OFFSET = 2
    WIDTH = 10
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = (-1,0)
        self.length = 2
        self.boxes = [Box(self.x+ self.WIDTH*i , self.y ) for i in range(self.length)]


    def move(self):
        old = self.boxes[0]
        new = Box(old.x + self.WIDTH*self.dir[0], old.y + self.WIDTH*self.dir[1])
        #print(self.dir)
        if new not in self.boxes[1:]:
            self.boxes.pop(self.length-1)
            self.boxes.insert(0,new) 

    def eat(self):
        head = self.boxes[0]
        new = Box(head.x + self.WIDTH*self.dir[0],  head.y + self.WIDTH*self.dir[1])
        self.length += 1
        self.boxes.append(new)

    def draw(self,win):
        for box in self.boxes :
            box.draw_box(win)




class Food():
    def __init__(self, grid):
        self.grid = grid
        self.position = self.grid[random.randint(0, len(self.grid) -1)]

    def draw(self, win):
        rect = pygame.Rect((self.position[0], self.position[1]), (10,10))
        pygame.draw.rect(win, 'red', rect)




def game():
    grid = Grid()
    grid.make_grid()
    win = pygame.display.set_mode(SCREEN)
    clock = pygame.time.Clock()
    run = True
    snake = Snake(WIN_HEIGHT//2, WIN_WIDTH//2)
    food = Food(grid.coords)
    while run:
        clock.tick(20)
        win.fill('black')
        #grid.draw_grid(win)
        head =snake.boxes[0]
        #insert game logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP :
                    snake.dir = (0,-1)
                if event.key == pygame.K_DOWN :
                    snake.dir = (0,1)
                if event.key == pygame.K_LEFT :
                    snake.dir = (-1,0)
                if event.key == pygame.K_RIGHT :
                      snake.dir = (1,0)
        
        for box in snake.boxes[1:]:
            if (head.x, head.y) == (box.x, box.y):
                run = False

        if (head.x, head.y) == food.position:
            print('lool')
            snake.eat()
            food = Food(grid.coords)


        if (head.x, head.y) not in grid.coords:
            run = False
        snake.move()

        food.draw(win)
        snake.draw(win)
        pygame.display.update()

game()