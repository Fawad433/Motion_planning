import pygame
import random

pygame.font.init()


class Arena:

    def __init__(self):

        # VAR FOR GRID CREATION
        self.s_width = 3000
        self.s_height = 1700
        self.play_width = 2600
        self.play_height = 1600
        self.block_size = 50
        self.no_of_blocks_in_width = self.play_width // self.block_size  # meaning 2600//50 = 52 are the no of blocks in x-axis
        self.no_of_blocks_in_height = self.play_height // self.block_size  # meaning 1600 // 50 = 32 are the no of blocks in y-axis
        self.top_left_x = (self.s_width - self.play_width) // 2  # it's the top left of the game window in the main window
        self.top_left_y = self.s_height - self.play_height
        self.grid = {}
        self.hurdle = []

    def create_arena(self):

        self.grid = {(x, y): {'directions': ['▲', '▼', '◄', '►'], 'color': [0, 0, 0]} for y in
                     range(self.no_of_blocks_in_height) for x in range(self.no_of_blocks_in_width)}

    def draw_grid_in_arena(self, surface):
        '''
        This will draw the lines in the Arena
        '''
        sx = self.top_left_x
        sy = self.top_left_y

        for i in range(self.no_of_blocks_in_height):
            pygame.draw.line(surface, (120, 120, 120), (sx, sy + i * self.block_size),
                             (sx + self.play_width, sy + i * self.block_size))
            for j in range(self.no_of_blocks_in_width):
                pygame.draw.line(surface, (120, 120, 120), (sx + j * self.block_size, sy),
                                 (sx + j * self.block_size, sy + self.play_height))

    def create_hurdles(self):

        for i in range(100):
            h = (random.randint(0, 50), random.randint(0, 30))
            if h not in self.hurdle:
                self.hurdle.append(h)
                self.grid[h]['directions'] = ['*', '*', '*', '*']

        self.hurdle.append((0,1))
        self.grid[(0,1)]['directions'] = ['*', '*', '*', '*']
        self.hurdle.append((1,0))
        self.grid[(1,0)]['directions'] = ['*', '*', '*', '*']
        self.hurdle.append((1,1))
        self.grid[(1,1)]['directions'] = ['*', '*', '*', '*']

    def draw_window(self, surface, destination, robot_coordinates, path):
        '''
        This will kep on updating the window
        '''
        surface.fill((0, 0, 0))
        # Tetris Title
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('PATH FINDING OF ROBOT', 1, (255, 255, 255))

        surface.blit(label, (self.top_left_x + self.play_width / 2 - (label.get_width() / 2), 30))
        for i in range(self.no_of_blocks_in_height):
            for j in range(self.no_of_blocks_in_width):

                # this is to create individual block
                pygame.draw.rect(surface, self.grid[(j, i)]['color'],
                                 (self.top_left_x + j * self.block_size, self.top_left_y + i * self.block_size, self.block_size, self.block_size), 0)


                # robot position
                if [j, i] == robot_coordinates:
                    pygame.draw.rect(surface, (0, 255, 255),
                                     pygame.Rect(self.top_left_x + (j * self.block_size), self.top_left_y + (i * self.block_size),
                                                 self.block_size, self.block_size), 0)

                #robot_path
                if path != None and [j, i] in path:
                    pygame.draw.rect(surface, (0, 0, 255),
                                     pygame.Rect(self.top_left_x + (j * self.block_size), self.top_left_y + (i * self.block_size),
                                                 self.block_size, self.block_size), 0)

                # destination
                if [j, i] == destination:
                    pygame.draw.rect(surface, (255, 255, 255),
                                     pygame.Rect(self.top_left_x + (j * self.block_size), self.top_left_y + (i * self.block_size),
                                                 self.block_size, self.block_size), 0)

                if (j, i) in self.hurdle:
                    pygame.draw.rect(surface, (255, 0, 0),
                                     pygame.Rect(self.top_left_x + (j * self.block_size), self.top_left_y + (i * self.block_size),
                                                 self.block_size, self.block_size), 0)

                # For presenting the hurdles and values
                if self.grid[(j, i)]['directions'][0] == '*':
                    l = font.render('*', 5, (255, 255, 255))
                    surface.blit(l, (
                        (self.top_left_x + (j * self.block_size) + self.block_size / 2),
                        (self.top_left_y + (i * self.block_size) + self.block_size / 2)))

                # draw grid and border
                pygame.draw.rect(surface, (255, 0, 0), (self.top_left_x, self.top_left_y, self.play_width, self.play_height), 5)

        self.draw_grid_in_arena(surface)
        pygame.display.update()



