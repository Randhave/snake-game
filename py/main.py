import pygame
from pygame.locals import *  # this code import all tools of pygame
import time
import random
size = 20

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = 100
        self.y = 100

    def draw_apple(self):
        block = pygame.image.load("../images/apple.png").convert()
        self.parent_screen.blit(block, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * size
        self.y = random.randint(1, 25) * size


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.x = 200
        self.y = 200
        self.direction = 'right'
        self.length = length
        self.x = [size] * length
        self.y = [size] * length

    def draw(self):
        self.parent_screen.fill((69, 230, 112))
        block = pygame.image.load("../images/arrow2.png").convert()
        for i in range(self.length):
            self.parent_screen.blit(block, (self.x[i], self.y[i]))
        pygame.display.flip()  # this flip() method  show window screen created by display method

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def increase_snake_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score : {self.length}", True, (255, 255, 255,))
        self.parent_screen.blit(score, (850, 10))
        pygame.display.flip()

    # def high_score(self):
    #     if self.length < 4:
    #         time.sleep(0.3)
    #     if self.length >= 4:
    #         time.sleep(0.2)
    #     if self.length >= 5 and self.length <= 14:
    #         time.sleep(0.1)
    #     if self.length >= 15 and self.length <= 20:
    #         time.sleep(0.045)
    #     if self.length >= 21 and self.length < 30:
    #         time.sleep(0.040)
    #     if self.length >= 30:
    #         time.sleep(0.035)

    def game_over(self):
        font = pygame.font.SysFont('arial', 25)
        line2 = font.render(f"To play again press Enter , To exit press Escape", True, (255, 255, 255,))
        self.parent_screen.blit(line2, (210, 300))
        pygame.display.flip()    # flip() it is important method , it update the value for showing on screen

    def walk(self):
        for i in range(self.length - 1, 0, -1):  # self.length-1 means last block of snake chain
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        self.draw()


class Game:
    def __init__(self):
        pygame.init()  # initilize pygame module
        self.surface = pygame.display.set_mode((1000, 600))  # this code create window screen given width and height value
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw_apple()

    def play(self):
        self.snake.walk()
        self.apple.draw_apple()
        self.snake.score()

        pygame.display.flip()

        # collision of block with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):  # this parameter pass in _collision function
            self.snake.increase_snake_length()
            self.apple.move()

        # collision of block with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):  # this parameter pass in _collision function
                  raise("Game over")

    def is_collision(self, x1, y1, x2, y2):  # x1 = self.snake.x[0] , y1 = self.snake.y[0] , x2 = self.apple.x , y2 = self.apple.y
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False

        while running:
            # events = pygame.event.get()  # event.get() this method is getting user input
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.snake.game_over()
                pause = True
                self.reset()

            # self.snake.high_score()
            time.sleep(0.1)   # for speed of snake

if __name__ == '__main__':
    game = Game()
    game.run()

        # / **
        # *
        #     * @ author
        #     Aniket_Randhave
        # * /