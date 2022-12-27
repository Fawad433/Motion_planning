from Arena import *  # very important to get the pygame module too
from Robot import Robot
from Path_planning import *
import pygame
import copy

arena = Arena()
robot = Robot()
planning = PathPlanning()


def main():
    arena.create_arena()
    run = True
    arena.create_hurdles()
    robot.spawn_robot(arena.hurdle, arena.no_of_blocks_in_width, arena.no_of_blocks_in_height)
    find_path = 0
    planning.Path = None

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                robot.find_click_location(pos, arena.top_left_x, arena.top_left_y, arena.block_size)
                find_path = 1
                arena.draw_window(win, robot.destination, robot.robot_coordinates,planning.Path)

            if find_path == 1:
                planning.a_star(robot.robot_coordinates, robot.destination, arena.no_of_blocks_in_width,
                                arena.no_of_blocks_in_height, arena.grid)
                find_path = 0

        if planning.Path is not None:
            path = copy.copy(planning.Path)
            for place in path:
                print(path)
                print(planning.Path)
                robot.robot_coordinates = place
                planning.Path.remove(place)
                arena.draw_window(win, robot.destination, robot.robot_coordinates, planning.Path)
                pygame.time.delay(100)
            planning.Path = None

        else:
            arena.draw_window(win, robot.destination, robot.robot_coordinates, planning.Path)


win = pygame.display.set_mode((arena.s_width, arena.s_height))
pygame.display.set_caption('Robot Planning')
main()  # start game1
