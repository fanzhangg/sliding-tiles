import unittest
import case_solvable_judge as judge
from Board import Board


class tedtCaseSolavableJudge(unittest.TestCase):
    def test_0_get_out_of_order_pair_num(self):
        print('Start get_out_of_order_pair_num test\n')
        case_1 = (1, 2, 3, 4, 5, 6, 8, 7)
        self.assertEqual(judge.get_out_of_order_pair_num(case_1), 1)
        case_2 = (1, 2, 3, 4, 5, 8, 7, 6)
        self.assertEqual(judge.get_out_of_order_pair_num(case_2), 3)
        print('\nFinish get_out_of_order_pair_num test\n')

    def test_1_check_puzzle_in_3_3_board_possible(self):
        print('Start check_puzzle_in_3_3_board_possible test\n')
        case_1 = (1, 2, 3, 4, 5, 6, 8, 7)
        print(case_1)
        print(judge.get_out_of_order_pair_num(case_1))
        self.assertFalse(judge.check_puzzle_in_3_3_board_possible(case_1))
        case_2 = (1, 2, 3, 4, 5, 6, 7, 8)
        self.assertTrue(judge.check_puzzle_in_3_3_board_possible(case_2))
        print('\nFinish check_puzzle_in_3_3_board_possible test\n')

    def tet_2_check_puzzle_board_possible(self):
        print("Start check_puzzle_board_possible test\n")
        case_1 = (1, 2, 3, 4, 5, 6, 8, 7)
        self.assertFalse(judge.check_puzzle_possible(judge.board, case_1))
        case_2 = (1, 2, 3, 4, 5, 6, 7, 8)
        self.assertTrue(judge.check_puzzle_possible(judge.board, case_2))
        judge.board = Board(4, 4)
        case_3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 12, 11)
        self.assertFalse(judge.check_puzzle_possible(judge.board, case_3))
        case_4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
        self.assertTrue(judge.check_puzzle_possible(judge.board, case_4))


if __name__ == '__main__':
    unittest.main()
