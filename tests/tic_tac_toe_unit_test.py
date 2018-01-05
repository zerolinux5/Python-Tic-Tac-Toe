import unittest
import sys
import os
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/src")
import tic_tac_toe

EDGE = "-------"
SPACE = " "

class Test_Get_Board_String(unittest.TestCase):

    def setUp(self):
        pass

    # Test no values
    def test_empty_set(self):
        test_board = [SPACE] * 9
        target_board = EDGE + "| | | |"*3 + EDGE
        return_board = tic_tac_toe.get_board_string(test_board)
        self.assertEqual(return_board, target_board)

    # Test all Xs
    def test_xs(self):
        test_board = ["X"] * 9
        target_board = EDGE + "|X|X|X|"*3 + EDGE
        return_board = tic_tac_toe.get_board_string(test_board)
        self.assertEqual(return_board, target_board)

    # Test all Os
    def test_os(self):
        test_board = ["O"] * 9
        target_board = EDGE + "|O|O|O|"*3 + EDGE
        return_board = tic_tac_toe.get_board_string(test_board)
        self.assertEqual(return_board, target_board)

    # Test a full set
    def test_full(self):
        test_board = ["O","O","X","X","O","O","O","X","X"]
        target_board = EDGE + "|O|O|X||X|O|O||O|X|X|" + EDGE
        return_board = tic_tac_toe.get_board_string(test_board)
        self.assertEqual(return_board, target_board)

    # Test a set with some empty values
    def test_mix(self):
        test_board = ["O","O"," ","X","O"," ","O"," ","X"]
        target_board = EDGE + "|O|O| ||X|O| ||O| |X|" + EDGE
        return_board = tic_tac_toe.get_board_string(test_board)
        self.assertEqual(return_board, target_board)

class Test_Check_End_Game(unittest.TestCase):

    def setUp(self):
        pass

    # Test no values
    def test_empty_set(self):
        test_moves = []
        num_turns = 0
        next_play = 1
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(True, cont)

    # Test no values
    def test_full_set(self):
        test_moves = [1,2,3,4,5,6,7,8,9]
        num_turns = 0
        next_play = 9
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)

    # Test no values
    def test_set_1(self):
        test_moves = [1,2,3]
        num_turns = 0
        next_play = 3
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)

    # Test no values
    def test_set_2(self):
        test_moves = [4,5,6]
        num_turns = 0
        next_play = 6
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)

    # Test no values
    def test_set_3(self):
        test_moves = [7,8,9]
        num_turns = 0
        next_play = 9
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)

    # Test no values
    def test_set_4(self):
        test_moves = [1,4,7]
        num_turns = 0
        next_play = 7
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)

    # Test no values
    def test_set_5(self):
        test_moves = [2,5,8]
        num_turns = 0
        next_play = 8
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)

    # Test no values
    def test_set_6(self):
        test_moves = [3,6,9]
        num_turns = 0
        next_play = 9
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)

    # Test no values
    def test_set_7(self):
        test_moves = [1,5,9]
        num_turns = 0
        next_play = 9
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)

    # Test no values
    def test_set_8(self):
        test_moves = [3,5,7]
        num_turns = 0
        next_play = 7
        cont = tic_tac_toe.check_end_game(next_play, num_turns, test_moves)
        self.assertEqual(False, cont)
if __name__ == '__main__':
    unittest.main()
