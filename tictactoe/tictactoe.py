"""
Tic Tac Toe Player
"""

import math

# moves of the board
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if the board is empty, X goes first
    if board == initial_state():
        return X
    # if the game is over, return None
    elif terminal(board):
        return None
    else:
        # count the number of X and O on the board
        x = 0
        o = 0
        for row in board:
            x += row.count(X)
            o += row.count(O)
        # if X has more moves than O, it's O's turn
        if x > o:
            return O
        else:
            return X




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibilities.add((i, j))
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Raises an exception if action is not valid.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    else:
        new_board = [row.copy() for row in board]
        new_board[i][j] = player(board)
        return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    # check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    # if no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all([cell != EMPTY for row in board for cell in row]):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    If the board is terminal, the function returns None.
    """

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v
    
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
    

    
    if terminal(board):
        return None
    if player(board) == X:
        v = -math.inf
        best_move = None
        for action in actions(board):
            new_v = min_value(result(board, action))
            if new_v > v:
                v = new_v
                best_move = action
        return best_move
    else:
        v = math.inf
        best_move = None
        for action in actions(board):
            new_v = max_value(result(board, action))
            if new_v < v:
                v = new_v
                best_move = action
        return best_move
