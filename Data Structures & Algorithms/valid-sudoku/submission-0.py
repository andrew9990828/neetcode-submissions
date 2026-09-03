class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                point = board[r][c]
                if point == ".":
                    continue

                if (point in rows[r] or point in cols[c]
                    or point in boxes[(r//3, c//3)]):
                    return False
                
                rows[r].add(point)
                cols[c].add(point)
                boxes[(r//3, c//3)].add(point)
        
        return True
