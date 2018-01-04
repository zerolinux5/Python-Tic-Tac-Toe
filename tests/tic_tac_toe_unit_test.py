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

if __name__ == '__main__':
    unittest.main()
