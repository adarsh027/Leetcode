class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0

        total_time = 0

        for i in range(len(timeSeries) - 1):
            # Calculate the time difference between consecutive attacks
            time_diff = timeSeries[i + 1] - timeSeries[i]
            
            # Add the poisoned time based on the time difference
            if time_diff < duration:
                total_time += time_diff
            else:
                total_time += duration

        # Add the duration of the last attack
        total_time += duration

        return total_time

# Example usage
timeSeries = [1, 4, 6, 8]
duration = 2
sol = Solution()
print(sol.findPoisonedDuration(timeSeries, duration))  # Output should be 8

#ref: chatgpt, https://www.youtube.com/watch?v=EkJ2Us1DowA
### Detailed Logic:
1. Initialize `total_time` to store the total time the target is poisoned.
2. Iterate through the `timeSeries` array, and for each attack, calculate the poisoned time by comparing `timeSeries[i + 1] - timeSeries[i]` with `duration`.
3. If the difference `timeSeries[i + 1] - timeSeries[i]` is less than `duration`, add the difference to `total_time` because the next attack happens before the current poison duration ends.
4. If the difference is greater than or equal to `duration`, add the full `duration` to `total_time`.
5. Finally, add the duration of the last attack to `total_time`.

### Code:

```python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_time = 0

        for i in range(len(timeSeries) - 1):
            # Calculate the time difference between each consecutive attacks
            time_diff = timeSeries[i + 1] - timeSeries[i]
            
            # Add the poisoned time based on the time difference
            if time_diff < duration:
                total_time += time_diff
            else:
                total_time += duration

            # the above if else block can be reduced the below code since we are in essencee adding the minimum of diff and duration to total time.
            # Calculate the poisoned time for the current attack
            # total_time += min(time_diff, duration)

        # Add the duration of the last attack
        total_time += duration

        return total_time

### Explanation of the Code:
# 1. **Edge Case**: If `timeSeries` is empty, return `0` immediately.
# 2. **Loop through attacks**: Iterate through `timeSeries` from the first attack to the second last attack.
#    - **Calculate Time Difference Between Each Consecutive Atttack** as : `timeSeries[i + 1] - timeSeries[i]`
#    - **Determine Poisoned Time**: 
#      - If `time_diff` (timeSeries[i + 1] - timeSeries[i]) is less than `duration`, it means the next attack happens before the current poison duration ends, so add `time_diff` to `total_time`.
#      - If `time_diff` is greater than or equal to `duration`, add the full `duration` to `total_time`.
# 3. **Last Attack**: Add the full duration of the last attack to `total_time` as it always adds the complete duration.
# 4. **Return result**: Return `total_time`.


# Example usage
timeSeries = [1, 2, 5, 8]
duration = 3
sol = Solution()
print(sol.findPoisonedDuration(timeSeries, duration))  # Output should be 10

### Explanation with `timeSeries = [1, 2, 5, 8]` and `duration = 3`:

# 1. **First Attack** (`i = 0`):
#    - `time_diff = 1`
#    - `time_diff (1) < duration (3)`, so `total_time += 1`.
#    - `total_time = 1`

# 2. **Second Attack** (`i = 1`):
#    - `time_diff = 3`
#    - `time_diff (3) >= duration (3)`, so `total_time += 3`.
#    - `total_time = 4`

# 3. **Third Attack** (`i = 2`):
#    - `time_diff = 3`
#    - `time_diff (3) >= duration (3)`, so `total_time += 3`.
#    - `total_time = 7`

# 4. **Add the duration of the last attack**:
#    - Add `duration = 3` to `total_time`.
#    - `total_time = 10`

# The total poisoned time is `10` seconds.
