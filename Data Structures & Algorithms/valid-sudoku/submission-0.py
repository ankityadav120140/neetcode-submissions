class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each column
        for i in range(9):
            st = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] in st:
                    return False
                else:
                    st.add(board[j][i])

        #check each row
        for i in range(9):
            st = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in st:
                    return False
                else:
                    st.add(board[i][j])
        
        #check each block
        for i in range(3):
            for j in range(3):
                a = i * 3
                b = j * 3
                st = set()
                for x in range(3):
                    for y in range(3):
                        if board[a + x][b + y] == ".":
                            continue
                            
                        if board[a + x][b + y] in st:
                            return False
                        else:
                            st.add(board[a + x][b + y])
        return True

        

            