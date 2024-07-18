class Solution:
    def distributeCandies(self, candyType):
        # Step 1: Calculate the number of unique candies using a set.
        unique_candies = len(set(candyType))
        
        # Step 2: Calculate the maximum number of candies the sister can receive.
        max_candies_for_sister = len(candyType) // 2
        
        # Greedy Decision:
        # The sister can receive at most `max_candies_for_sister` candies.
        # We want to maximize the number of unique types of candies she receives.
        # Hence, we return the minimum of `unique_candies` and `max_candies_for_sister`.
        return min(unique_candies, max_candies_for_sister)

# Example usage:
candyType = [1, 1, 2, 2, 3, 3]
solution = Solution()
print(solution.distributeCandies(candyType))  # Output: 3

# Example usage:
candyType = [1, 1, 2, 2, 3, 3]
solution = Solution()
print(solution.distributeCandies(candyType))  # Output: 3

### Explanation

# 1. **Unique Candy Types**:
#    - Use a set to find the number of unique candy types: `unique_candies = len(set(candyType))`.

# 2. **Maximum Possible Unique Candies for the Sister**:
#    - The sister can receive at most half of the total candies: `max_candies_for_sister = len(candyType) // 2`.

# 3. **Result**:
#    - The maximum number of unique candies the sister can get is the minimum of the number of unique candy types and the maximum number of candies she can receive: `return min(unique_candies, max_candies_for_sister)`.
#    - In this problem, the greedy approach is applied when deciding how many unique types of candies the sister can get without exceeding the limit. The idea is to maximize the number of unique candy types she receives, up to the limit of half the total candies. The greedy decision here is to choose as many unique types as possible without exceeding the allowed number of candies (n // 2).
       

# This approach ensures that the solution is both optimal and efficient, with a time complexity of O(n) and a space complexity of O(n).

# Note: Why greedy approach??
# The usage of greedy algorithm(ie, greedy choice) is justified here because:
# 1. Objective: We want to maximize the variety of candies the sister receives.
# 2. Constraints: The sister can only receive half of the total candies (n / 2 candies). This is a strict limit that cannot be exceeded.
# 3. Greedy choice:
# - The greedy choice in this problem is to prioritize giving the sister the maximum number of unique candy types without exceeding the allowed number of candies.
# - This is done by taking the minimum of the number of unique types of candies (unique_candies) and the allowed number of candies (max_candies_for_sister).
# - It ensures that the solution is both feasible (does not exceed the limit) and optimal (maximizes the number of unique types).

# Note:
# Greedy algorithm terminologies(addional information; not really required):
# 1. Local Optimization(the action): By making the greedy choice, we decide on the number of unique candy types the sister can get by taking the minimum of the unique types and the allowed number of candies.
# 2. Global Optimization(the result of the action, ie, local optimization): This ensures that the sister receives the maximum variety of candies possible within her allowed limit, achieving the global optimization.

