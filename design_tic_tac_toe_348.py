class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[' ' for j in range(n)] for i in range(n)]
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = 'X' if player == 1 else 'O'
        return self._check_state(row, col, player)
    

    
    def _check_state(self, i, j, player):
        row = self.board[i]
        unique_row = set(row)
        if len(unique_row) == 1: return player

        col = [self.board[i][j] for i in range(0, self.size)]
        unique_row = set(col)
        if len(unique_row) == 1: return player

        if i == j: 
            diagonal = [self.board[i][i] for i in range(0, self.size)]  
            unique_diag = set(diagonal)
            if len(unique_diag) == 1: return player

        if i + j == self.size - 1:
            diagonal = [self.board[i][self.size - i - 1] for i in range(0, self.size)]  
            unique_diag = set(diagonal)
            if len(unique_diag) == 1: return player
        
        return 0

    def __str__(self):
        output = ''
        for row in self.board:
            output += '|'.join(row) + '\n'
        return output


toe = TicTacToe(3)

print(toe.move(0, 0, 1))
print(toe.move(0, 2, 2))
print(toe.move(2, 2, 1))
print(toe.move(1, 1, 2))
print(toe.move(2, 0, 1))
print(toe.move(1, 0, 2))
print(toe.move(2, 1, 1))
print(toe)