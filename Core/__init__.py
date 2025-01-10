from Core.Repository.PlayTable import PlayTable
from Core.Domain.Vector2 import Vector2 as v2

class MoveInvalidException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Core:
    Table = None
    direction_set = [v2(0, 1), v2(1, 1), v2(1, 0), v2(1, -1), v2(0, -1), v2(-1, -1), v2(-1, 0), v2(-1, 1)]
    valid_directions = []
    def __init__(self):
        pass

    def set_size(self, size):
        self.Table = PlayTable(size)
        height, width = size

        middle = v2(width//2-1, height//2)
        offsets = [v2(0,0), v2(1,0), v2(1,-1), v2(0,-1)]

        p1 = 1
        for offset in offsets:
            place = middle + offset
            self.Table.grid[place.y, place.x] = p1+1
            p1 = (p1+1)%2


    def get_board(self):
        return self.Table.grid

    def validate_move(self, player, location):
        board = self.Table.grid
        move_valid = False

        self.valid_directions = []
        # Iterate through all directions to check for validity
        for direction in self.direction_set:
            move_valid = (self.__validate_move(player, location, direction, board) or move_valid)

        if not move_valid:
            raise MoveInvalidException("Invalid move")

        # Update board if the move is valid
        self.Table.change_cell(location, player)
        for direction in self.valid_directions:
            _loc = location + direction
            while self.Table.grid[_loc.y, _loc.x] != player:
                self.Table.grid[_loc.y, _loc.x] = player
                _loc = _loc + direction

    def __is_on_board(self, row, col):
        board = self.Table.grid
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    def get_valid_moves(self, board, player_id):
        """
        Find all valid moves for the given player.
        :param player_id: The player for whom to find valid moves (1 or 2).
        :param board: The board in which to get valid moves.
        :return: List of tuples representing valid moves (array, col).
        """
        opponent_id = 1 if player_id == 2 else 2
        directions = [
            (-1, 0), (1, 0),  # vertical
            (0, -1), (0, 1),  # horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonal
        ]
        valid_moves = []


        for row in range(len(board)):
            for col in range(len(board[0])):
                move_valid  = False
                for direction in self.direction_set:
                    move_valid = move_valid or self.__validate_move(player_id, v2(col, row), direction, board)

                if move_valid:
                    valid_moves.append((row, col))

        return valid_moves

    def __validate_move(self, player, location, direction, board):
        # Ensure the starting cell is empty
        if board[location.y, location.x] != 0:
            return False

        # Initialize variables
        current_location = location + direction
        rows, cols = board.shape  # Extract board dimensions
        opposite_counter = 0

        # Traverse in the given direction
        while 0 <= current_location.y < rows and 0 <= current_location.x < cols:
            cell_value = board[current_location.y, current_location.x]

            if cell_value == 0:  # Empty cell: invalid move
                return False

            if cell_value == player:  # Found player's piece after opponents
                if opposite_counter > 0:
                    self.valid_directions.append(direction)
                return opposite_counter > 0

            # Count opponent's pieces
            opposite_counter += 1
            current_location += direction

        return False  # Reached the edge without finding player's piece

    def apply_move(self, temp_board, move, player_id):
        board = temp_board
        player = player_id
        location = move

        move_valid = False

        self.valid_directions = []
        # Iterate through all directions to check for validity
        for direction in self.direction_set:
            move_valid = move_valid or self.__validate_move(player, location, direction, board)

        if not move_valid:
            raise MoveInvalidException("Invalid move")

        # Update board if the move is valid
        board[location.y, location.x] = player
        for direction in self.valid_directions:
            _loc = location + direction
            while board[_loc.y, _loc.x] != player:
                board[_loc.y, _loc.x] = player
                _loc = _loc + direction

