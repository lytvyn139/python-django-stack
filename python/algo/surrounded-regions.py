class Solution:
    _rows = 0
    _cols = 0
    
    def solve(self, board: List[List[str]]) -> None:
        if board == None or len(board) == 0: return
        self._rows = len(board)
        self._cols = len(board[0])
        
        from itertools import product
        borders = list(product(range(self._rows), [0, self._cols-1])) + list(product([0, self._rows-1], range(self._cols)))
        
        for row, col in borders:
            self.DFS(board, row, col)
        
        for r in range(self._rows):
            for c in range(self._cols):
                if board[r][c] == 'O': board[r][c] = 'X'
                elif board[r][c] == 'Resistence': board[r][c] = 'O'
                    
    def DFS(self, board, row, col):
        if board[row][col] != 'O':
            return
        board[row][col] = 'Resistence'
        if col < self._cols-1: self.DFS(board, row, col+1)
        if row < self._rows-1: self.DFS(board, row+1, col)
        if col > 0: self.DFS(board, row, col-1)
        if row > 0: self.DFS(board, row-1, col)