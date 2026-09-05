class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        listWithTarget = None

        while l <= r:
            mid = (l + r) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid]) -1]:
                listWithTarget = matrix[mid]
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][len(matrix[mid]) -1]:
                l = mid + 1
        
        if not listWithTarget:
            return False
        else:
            l, r = 0, len(listWithTarget) - 1

            while l <= r:
                mid = (l + r) // 2

                if target < listWithTarget[mid]:
                    r = mid - 1
                elif target > listWithTarget[mid]:
                    l = mid + 1
                else:
                    return True
            
            return False
        