class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        answer: List[int] = []
        minList: List[int] = [-1] * len(matrix)

        for row in range(len(matrix)):
            tmp: int = 1e9
            for col in range(len(matrix[0])):
                if tmp > matrix[row][col]:
                    tmp = matrix[row][col]
                    minList[row] = col
        
        for i in range(len(matrix)):
            flag: bool = False
            for row in range(len(matrix)):
                if matrix[i][minList[i]] < matrix[row][minList[i]]:
                    flag = True
                    break
            if flag == False: answer.append(matrix[i][minList[i]])
        return answer