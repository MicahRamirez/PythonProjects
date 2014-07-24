
"""
Clone of 2048 game.
"""
import random
#import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code
    result = []
    for index in range(len(line)):
        result.append(0)
    result = shift_down(line, result)
    for index in range(len(result) - 1):
        if result[index] == result[index + 1]:
            result[index] *= 2
            result[index + 1] = 0
            result = shift_down(result, result)
    return result


def shift_down(line, result):
    """
    shifts all the values down in a list
    so that there are no zeroes in between
    """
    
    for index in range(len(line)):
        current = index
        next_greater_zero = -1
        if line[index] == 0:
            #while the next value is still zero move right
            while current + 1 < len(line) and line[current] == 0:
                current +=1
                #if value is not equal to zero save index
                #of the next >0 value to assign current index that value
                if line[current] != 0:
                    next_greater_zero = current
                    break
            #assign result[next_greater_zero] to line[next_greater_zero]
            #change line[next_greater_zero] to zero
            next_value = line[next_greater_zero]
            line[next_greater_zero] = 0
            result[index] = next_value
        else:
            result[index] = line[index]
    return result

class TwentyFortyEight():
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        self.direction_indices = self.create_dictionary_indexes()


    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        self.board = [[0 for dummy_index in range(self.grid_width)] for dummy_inner_index in range(self.grid_height)]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        board = ""
        for index in range(self.grid_height):
            board += "["
            for inner_index in range(self.grid_width):
                board += str(self.board[index][inner_index]) + " "
            else:
                board += "]\n"
        return board

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code

        indices = self.direction_indices[direction]
        for coordinate in indices:
            merged_coordinate_list = self.get_list(direction, coordinate)
            self.change_board(merged_coordinate_list, coordinate, direction)
        print(self.__str__())
        if self.board_is_not_full():
            self.new_tile()
    
    def board_is_not_full(self):
        board_is_full = False
        for dummy_index in range(self.grid_height):
            for dummy_in_index in range(self.grid_width):
                if self.board[dummy_index][dummy_in_index] == 0:
                    return not board_is_full
        return board_is_full
                
    def change_board(self, merged_list, coordinate, direction):
        """
        After a merged_list has been calculated, assigns these values
        to the proper coordinates on the board
        """
        initial_y = coordinate[0]
        initial_x = coordinate[1]
        if direction == UP or direction == DOWN:

            #THE ISSUE IS HERE???
            for index in range(self.grid_width):
                self.board[initial_y][coordinate[1]] = merged_list[index]
                initial_y += OFFSETS[direction][0]
        else:
            for index in range(self.grid_height):
                self.board[coordinate[0]][initial_x] = merged_list[index]
                initial_x += OFFSETS[direction][1]

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        # creating a random float variable that will roll a random value
        # if randomvalue > .90
        #

        tile_added = False
        while not tile_added:
            row = random.randint(0,self.grid_height - 1)
            col = random.randint(0,self.grid_width - 1)
            if self.board[row][col] == 0:
                tile_added = True
                random_tile = random.random()
                if random_tile < .90:
                    self.board[row][col] = 2
                else:
                    self.board[row][col] = 4

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        if col < self.grid_height and row < self.grid_width:
            self.board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.board[row][col]

    def get_list(self, direction, coordinate):
        """
        gets the list in the direction from the specified coordinate
        """
        to_be_merged = []
        row = coordinate[0]
        col = coordinate[1]
        if direction == UP or direction == DOWN:
            for dummy_index in range(self.grid_height):
                to_be_merged.append(self.board[row][col])
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
            merged = merge(to_be_merged)
        else:
            for dummy_index in range(self.grid_width):
                to_be_merged.append(self.board[row][col])
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
            merged = merge(to_be_merged)
        return merged

    def create_dictionary_indexes(self):
        """
        Creates a dictionary of the border coordinates for each direction
        """
        direction_dictionary = {}
        direction_dictionary[UP] = self.direction_list(UP)
        direction_dictionary[DOWN] = self.direction_list(DOWN)
        direction_dictionary[LEFT] = self.direction_list(LEFT)
        direction_dictionary[RIGHT] = self.direction_list(RIGHT)
        return direction_dictionary

    def direction_list(self, direction):
        """
        Creates the list of border indexes for a direction
        """
        direction_indexes = []
        
        if direction == UP:
            for index in range(self.grid_width):
                direction_indexes.append((0, index))
        elif direction == DOWN:
            for index in range(self.grid_width):
                direction_indexes.append((self.grid_height - 1, index))
        elif direction == LEFT:
            for index in range(self.grid_height):
                direction_indexes.append((index , 0))
        elif direction == RIGHT:
            for index in range(self.grid_height):
                direction_indexes.append(((index), self.grid_width - 1))

        return direction_indexes



#     line = [2, 0 , 2, 4]
#     print(merge(line))
#     line = [0,0,2,2]
#     print(merge(line))
#     line = [2,2,0,0]
#     print(merge(line))
#     line = [2,2,2,2]
#     print(merge(line))
#     line = [8,16,16,8]
#     print(merge(line))
#
# game = TwentyFortyEight(4,4)
# print(game.__str__())
# game.set_tile(2,2, 2048)
# print(game.__str__())
# print(game.reset())
# print(game.__str__())
# game.new_tile()
# game.new_tile()
# game.new_tile()
# game.new_tile()
# print(game.__str__())
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))