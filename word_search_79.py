def exist(board, word):

    def dfs(board, word, i, j, index):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or index >= len(word): return False        
        if board[i][j] != word[index]: return False
        if index == len(word) - 1: return True

        temp = board[i][j]
        board[i][j] = '#'

        for (x, y) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            exist = dfs(board, word, i + x, j + y, index + 1)
            if exist: return True 
        
        board[i][j] = temp


    for i in range(len(board)):
        for j in range(len(board[0])):
            exist = dfs(board, word, i, j, 0)
            if exist: return True
    return False

if __name__ == "__main__":
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "FCEB"))