class Board:
    def __init__(self, row, col):
        self.ROW = row
        self.COL = col
        self.tiles = []

    def initialize_board(self, tiles: tuple or list) -> None:
        expected_size = self.ROW * self.COL - 1
        print('The expected size is', expected_size)
        if len(tiles) == expected_size:
            self.tiles.append(tiles)
        elif len(tiles) >= expected_size:
            raise IndexError("The size of tiles exceeds the expected size")
        else:
            raise IndexError("The size of tiles less than the expected size")
