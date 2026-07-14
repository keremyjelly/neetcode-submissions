class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col in range(9):
            print(f'col={col}')
            cseen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in cseen:
                    print(f'Catch 1: col={col}, row={row}')
                    return False
                cseen.add(board[row][col])
            # pass 0-9 as row number
            if not self.validRow(sorted(board[col])):
                print(f'Catch 2: col={col}')
                return False

        for i in {1,4,7}:
            for j in{1,4,7}:
                if not self.validSq(board, i, j):
                    print(f'Catch 3: row,col={i,j}')
                    return False

        return True

    def validRow(self, row):
        for i in range(1,9):
            if row[i] == ".":
                continue
            if row[i] == row[i-1]:
                return False
        return True
    
    def validSq(self, board, ridx, cidx):
        print(f'checking {ridx, cidx}')
        seen = set()
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                if board[i + ridx][j + cidx] == ".":
                    continue
                if board[i + ridx][j + cidx] in seen:
                    print(f'failed at {board[i + ridx][j + cidx]}')
                    return False
                print(f'Did not find {board[i + ridx][j + cidx]} in {seen}')
                seen.add(board[i + ridx][j + cidx])
        return True
