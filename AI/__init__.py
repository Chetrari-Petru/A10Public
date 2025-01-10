import copy
import math
from Core import Core
from Core.Domain.Vector2 import Vector2


class ReversiAI:
    def __init__(self, player_id):
        self.player_id = player_id  # 2 for Player 2 (AI)
        self.opponent_id = 1 if player_id == 2 else 2

    def __count(self, array, value):
        """
        Counts the number of elements with the value $value in the array
        :param array: The array to be counted
        :param value:  The value to be counted
        :return: (int) Count the number of elements with the value $value in the array
        """
        count = 0
        for i in range(len(array)):
            if array[i] == value:
                count += 1
        return count



    def evaluate_board(self, board):
        """
        Evaluate the board state.
        Positive scores favor AI, and negative scores favor the opponent.
        """
        ai_score = sum(self.__count(row, self.player_id) for row in board)
        opponent_score = sum(self.__count(row, self.opponent_id) for row in board)
        return ai_score - opponent_score

    def get_valid_moves(self, core, board, player_id):
        """
        Use Core's methods to retrieve valid moves for the specified player.
        """
        return core.get_valid_moves(board, player_id)

    def minimax(self, core: Core, board, depth, maximizing_player, alpha, beta):
        """
        Minimax algorithm with alpha-beta pruning.
        """
        current_player = self.player_id if maximizing_player else self.opponent_id
        valid_moves = self.get_valid_moves(core, board, current_player)

        # Base case: game over or maximum depth reached
        if depth == 0 or not valid_moves:
            return self.evaluate_board(board), None

        best_move = None
        if maximizing_player:
            max_eval = -math.inf
            for move in valid_moves:
                temp_board = copy.deepcopy(board)
                _move = Vector2(move[1], move[0])
                core.apply_move(temp_board, _move, self.player_id)
                eval_score, _ = self.minimax(core, temp_board, depth - 1, False, alpha, beta)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = _move
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in valid_moves:
                temp_board = copy.deepcopy(board)
                _move = Vector2(move[1], move[0])
                core.apply_move(temp_board, _move, self.opponent_id)
                eval_score, _ = self.minimax(core, temp_board, depth - 1, True, alpha, beta)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = _move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def get_move(self, core, board):
        """
        Decide the best move using the minimax algorithm.
        """
        _, best_move = self.minimax(core, board, depth=3, maximizing_player=True, alpha=-math.inf, beta=math.inf)
        return best_move

# Example of how to integrate the AI in the game loop
# from core import Core
# core = Core()
# ai = ReversiAI(value=2)
# board = core.initialize_board()
# while not core.is_game_over(board):
#     if core.get_current_player() == 2:
#         move = ai.get_move(core, board)
#         core.apply_move(board, move, 2)
