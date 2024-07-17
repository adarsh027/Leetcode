# Solution 1 (preferred solution for its simplicity)
# source: https://www.youtube.com/watch?v=-PFCgiLjEaw  (Sai Anish Malla)
class Solution:
    def canFormArray(self, arr, pieces):
        # Create a mapping from the first element of each piece to the piece itself
        mapping = {piece[0]: piece  for piece in pieces}
        res = []
        for num in arr:
            if num in mapping:
                res += mapping[num]# alternativvely, you can res.extend(mapping[num])
        return res == arr
print(Solution().canFormArray([91,4,64,78], [[78],[4,64],[91]]))


# solution 2:
# source : chatgpt
class Solution:
    def canFormArray(self, arr, pieces):
        # Create a mapping from the first element of each piece to the piece itself
        piece_map = {piece[0]: piece for piece in pieces}
        
        i = 0
        while i < len(arr):
            # If the current element in arr does not start any piece, return False
            if arr[i] not in piece_map:
                return False
            
            # Retrieve the piece that starts with the current element of arr
            piece = piece_map[arr[i]]

            # Verify that each element in the current piece matches the corresponding elements in arr
            for num in piece:
                if arr[i] != num: # If any element in the piece does not match the current element in arr, return False
                    return False
                i += 1
        
        return True

# Example usage:
arr = [15, 88]
pieces = [[88], [15]]
sol = Solution()
print(sol.canFormArray(arr, pieces))  # Output: True
