"""
Make a 2 player Tic Tac Toe game.
"""
PLAYER_ONE = 0
PLAYER_TWO = 1
EDGE = "-------"
SPACE = " "
INPUT_STRING = "|"
VICTORY = [[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]

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

# Update the board state with the users input
def update_board_state(board_state, next_play, player):
    if player == PLAYER_ONE:
        player_char = "X"
    else:
        player_char = "O"
    next_play_str = str(next_play)
    # We assume the index is valid since we filtered during input
    loc = board_state.index(next_play_str)
    board_state[loc] = player_char
    return board_state

# Check if out of turns
def check_end_game(next_play, num_turns, player_moves):
    draw = num_turns >= 9
    cont = True
    # Only check for victory if we didn't draw
    if not draw:
        # Get possible victory conditions
        new_vic_cond = [state for state in VICTORY if next_play in state]

        # For each no possible victory state
        for state in new_vic_cond:
            count = 0
            # Check if win condition is present
            for val in state:
                if val in player_moves:
                    count += 1
            # Player wins
            if count == 3:
                cont = False
                break
    else:
        cont = False
    return cont

#Main loop
def main():
    not_finished = True
    moves = [[],[]]
    player = PLAYER_ONE
    p_move = moves[player]
    board_state = range(1,10)
    board_state = [str(val) for val in board_state]
    count = 1

    # Infinite loop
    while not_finished:
        #1. Print board state
        print_board_state(board_state)
        #2. Get player input
        next_play = get_next_value(player, board_state)

        #3. Replace value with player movement
        board_state = update_board_state(board_state, next_play, player)
        moves[player].append(next_play)

        #4. Check victory condition
        not_finished = check_end_game(next_play, count, p_move)
        count += 1

        if not_finished:
            #5. Move to next player
            player = (player + 1) % 2
            p_move = moves[player]
    if count == 9:
        end_str = "Draw!"
    else:
        end_str = "Player %d: won!" %(player + 1)
    print end_str

#Call main if not imported
if __name__ == "__main__":
    main()
