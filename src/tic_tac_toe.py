"""
Make a 2 player Tic Tac Toe game.
"""
PLAYER_ONE = 0
PLAYER_TWO = 1
EDGE = "-------"
SPACE = " "

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

#Main loop
def main():
    not_finished = True
    player = PLAYER_ONE
    board_state = [SPACE] * 9
    # Infinite loop
    while not_finished:
        print_board_state(board_state)
        player = (player + 1) % 2
        # For now iterate once
        not_finished = False

#Call main if not imported
if __name__ == "__main__":
    main()
