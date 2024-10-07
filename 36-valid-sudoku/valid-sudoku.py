class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for row in board:
            print("rows")
            nums = []
            for num in row:
                if num != ".":
                    nums.append(int(num))
            if len(nums) != len(set(nums)):
                return False

        for i in range(n):
            print("columns")
            nums = []
            for j in range(n):
                if board[j][i] != ".":
                    nums.append(int(board[j][i]))
            if len(nums) != len(set(nums)):
                return False

        for i in range(3):
            print("boxes")
            for j in range(3):
                nums = []
                for k in range(3):
                    for m in range(3):
                        num = board[3*i + k][3*j + m]
                        if num != ".": 
                            nums.append(int(num))
                    if len(nums) != len(set(nums)):
                        return False
        return True
        