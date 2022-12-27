
class Node:
    # Important for storing the values of g,h and f during the calculation of A*
    def __init__(self, position: (), parent: ()):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


class PathPlanning:

    def __init__(self):
        self.open_list = []
        self.closed_list = []
        self.Path = None


    def find_neighbors(self,current_location,no_of_blocks_in_width,no_of_blocks_in_height, grid):

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        neighbors = []
        for dir in directions:
            if no_of_blocks_in_width > dir[0] + current_location[0] >= 0 and no_of_blocks_in_height > dir[1] + current_location[1] >= 0 and \
                    grid[(dir[0] + current_location[0], dir[1] + current_location[1])]['directions'][0] != '*':
                neighbors.append([dir[0] + current_location[0], dir[1] + current_location[1]])
        return neighbors

    def add_to_open(self, neighbor):
        for node in self.open_list:
            if (neighbor == node and neighbor.f > node.f):
                return False
        return True

    def a_star(self,starting_pos, target_position, no_of_blocks_in_width,no_of_blocks_in_height, grid):
        self.open_list = []
        self.closed_list = []

        start_node = Node(starting_pos, None)
        goal_node = Node(target_position, None)

        self.open_list.append(start_node)

        while self.open_list:

            self.open_list.sort()
            current_node = self.open_list.pop(0)
            self.closed_list.append(current_node)
            if len(self.open_list) > 1000: # if there is no way
                break
            # code for checking the goal and then sending the whole path to it
            if current_node.position == goal_node.position:

                path = []
                while current_node != start_node:
                    path.append(current_node.position)
                    current_node = current_node.parent

                self.Path = path[::-1]
                break

            neighbors = self.find_neighbors(current_node.position, no_of_blocks_in_width,no_of_blocks_in_height,grid)

            for next in neighbors:

                neighbor = Node(next, current_node)

                if neighbor in self.closed_list:
                    continue

                neighbor.g = ((neighbor.position[0] - start_node.position[0]) ** 2 + (
                            neighbor.position[1] - start_node.position[1]) ** 2) ** 0.5
                neighbor.h = ((neighbor.position[0] - goal_node.position[0]) ** 2 + (
                            neighbor.position[1] - goal_node.position[1]) ** 2) ** 0.5
                neighbor.f = neighbor.g + neighbor.h

                if (self.add_to_open(neighbor) == True):
                    # Everything is green, add neighbor to open list
                    self.open_list.append(neighbor)


        # Return None, no path is found


