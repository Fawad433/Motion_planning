import random


class Robot:

    def __init__(self):
        self.destination = []
        self.robot_coordinates = []

    def find_click_location(self,pos,top_left_x,top_left_y,block_size):
        '''
        To use the final destination for path finding
        '''

        block_x = (pos[0] - top_left_x) // block_size
        block_y = (pos[1] - top_left_y) // block_size
        self.destination = [block_x, block_y]

    def spawn_robot(self, hurdles, no_of_blocks_in_width, no_of_blocks_in_height):
        '''
        This is to generate the random robot location
        '''
        block_x = random.randint(0, no_of_blocks_in_width - 1)
        block_y = random.randint(0, no_of_blocks_in_height - 1)
        # I will need to come back to hurdles
        if (block_x, block_y) in hurdles:
            self.spawn_robot(hurdles, no_of_blocks_in_width, no_of_blocks_in_height)
        self.robot_coordinates = [block_x, block_y]

