from Board import Board

# initialize a 3*3 board
board = Board(3, 3)


def get_out_of_order_pair_num(puzzle):
    """
    If a number is larger than another number after it, the two numbers are a out of order pair.
    Count the number of out of order pair case in a sliding tile case
    :param puzzle: a sliding tile case
    :type puzzle: list or tuple
    :return: the number of out of order pair
    :rtype: int
    """
    count = 0
    for i in range(1, 8):
        for j in range(i, 8):
            if puzzle[i] > puzzle[j]:
                count += 1
    return count


def check_puzzle_in_3_3_board_possible(puzzle):
    """
    Check if a puzzle in a 3*3 board is possible to solve or not
    :param puzzle: a sliding tile puzzle
    :type puzzle: list or tuple
    :return: true if the puzzle is solvable, else false
    :rtype: bool
    """
    pairs = get_out_of_order_pair_num(puzzle)
    # Each single move makes the number of out of order pairs either decreases one or increases two. Each vertical move
    # makes one number 2 moves forward or backward and thus the out of order pairs increase or decrease two. A puzzle is
    # possible to solve when its out of order pairs can be divided by two, else it is impossible to solve.
    return pairs % 2 == 0


def check_puzzle_possible(board, puzzle):
    """
    Check if a puzzle is possible to solve or not
    :param board: The sliding tile board
    :type puzzle: str or tuple
    :param puzzle: a sliding tile puzzle
    :return: true if the puzzle is solvable, else false
    :rtype: bool
    """
    board_size = board.ROW * board.COL
    pairs = get_out_of_order_pair_num(puzzle)
    return pairs % (board_size - 1) == 0
