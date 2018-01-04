"""
Make a 2 player Tic Tac Toe game.
"""
PLAYER_ONE = 0
PLAYER_TWO = 1
EDGE = "-------"
SPACE = " "
INPUT_STRING = "|"

#Return Board State as a string
def get_board_string(board_state):
    #Print Top
    return_string = EDGE
    # Print board list
    return_string += "|" + "|".join(board_state[:3]) + "|"
    return_string += "|" + "|".join(board_state[3:6]) + "|"
    return_string += "|" + "|".join(board_state[6:]) + "|"
    #Print Bottom
    return_string += EDGE
    return return_string

#Print Board State
def print_board_state(board_state):
    board_string = get_board_string(board_state)
    start = 0
    step = len(EDGE)
    while start < len(board_string):
        print board_string[start:start + step]
        start += step

# Get valid player value
def get_next_value(player, board_state):
    value = -1
    input_string = "Player:%d enter a value:" %(player + 1)
    is_not_in_board = value not in board_state
    invalid_value = value < 1 or value > 9
    while is_not_in_board or invalid_value:
        value = input(input_string)
        is_not_in_board = str(value) not in board_state
        invalid_value = value < 1 or value > 9
    return value

#Main loop
def main():
    not_finished = True
    player = PLAYER_ONE
    board_state = range(1,10)
    board_state = [str(val) for val in board_state]
    # Infinite loop
    while not_finished:
        #1. Print board state
        print_board_state(board_state)
        #2. Get player input
        next_play = get_next_value(player, board_state)
        #3. Move to next player
        player = (player + 1) % 2

#Call main if not imported
if __name__ == "__main__":
    main()
