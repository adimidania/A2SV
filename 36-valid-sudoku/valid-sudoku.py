class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                box_index = (i // 3) * 3 + (j // 3)
                if number != '.':
                    # Did we populate the numbers of row i? Does number exist in row i already?
                    if i not in rows:
                        rows[i] = {}
                    if number in rows[i]:
                        return False
                    rows[i][number] = 1

                    # Did we populate the numbers of col j? Does number exist in col j already?
                    if j not in cols:
                        cols[j] = {}
                    if number in cols[j]:
                        return False
                    cols[j][number] = 1

                    # Did we populate the current box? Does number exist in the current box?
                    if box_index not in boxes:
                        boxes[box_index] = {}
                    if number in boxes[box_index]:
                        return False
                    boxes[box_index][number] = 1

        return True