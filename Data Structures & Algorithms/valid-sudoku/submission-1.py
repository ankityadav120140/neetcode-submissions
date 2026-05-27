class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                tgt = board[r][c]
                if(tgt == "."):
                    continue
                
                b = (r // 3) * 3 + (c // 3)

                if (tgt in rows[r] or tgt in columns[c] or tgt in boxes[b]):
                    return False
                
                rows[r].add(tgt)
                columns[c].add(tgt)
                boxes[b].add(tgt)
        
        return True