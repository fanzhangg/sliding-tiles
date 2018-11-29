import unittest
from Board import Board


class testBoard(unittest.TestCase):
    board = Board(3, 3)

    def test_0_initialize_board(self):
        print("Start initialize board test")
        tiles_1 = (1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(self.board.initialize_board(tiles_1), None)
        tiles_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertRaises(IndexError("The size of tiles exceeds the expected size",
                                     self.board.initialize_board, tiles_2))
        tiles_3 = (1, 2, 3, 4)
        self.assertRaises(IndexError("The size of tiles less than the expected size",
                                     self.board.initialize_board, tiles_3))


if __name__ == '__main__':
    unittest.main(exit=False)
