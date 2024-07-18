# O(n) space approach
class Solution:
    def shuffle(self, nums, n):
        # Create an empty list to store the shuffled elements
        shuffled = []
        
        # Loop through the indices of the first half of the array
        for i in range(n):
            # Append the i-th element from the first half (x_i)
            shuffled.append(nums[i])
            # Append the i-th element from the second half (y_i)
            shuffled.append(nums[i + n])
        
        return shuffled
    

# Bit Manipulation Approach:  O(1) space approach (source : chatgpt)
# https://www.youtube.com/watch?v=IvIKD_EU8BY(neetcode)
class Solution:
    def shuffle(self, nums, n):
        # Encode with bitwise operations
        for i in range(n):
            y_i_shifted = nums[i + n] << 10  # Shift y_i left by 10 bits
            nums[i] =  y_i_shifted | nums[i]  # Combine Shifted y_i with x_i

        # After the first pass (encoding phase), each element in the first half of the 
        # array contains the combined result of the original xi and yi values. Remeber that the array size = 2n
        
        # Decode and rearrange
        for i in range(n-1, -1, -1):
            x_i = nums[i] & 1023  # Obtain x_i by bit masking with 1023
            y_i = nums[i] >> 10   # Obtain y_i by shifting right by 10 bits
            # We need to place xi values at even indices and yi values at odd indices to achieve the desired interleaving format.
            nums[2 * i] = x_i    
            nums[2 * i + 1] = y_i   
        
        return nums
# Note:
# In the above code, while decoding and rearranging,  we are using temperory variables x_ and y_i 
# because if we dont use them it could lead to incorrect results. Let's understand how things could wrong when we dont use
# the temperory variables by considering the below two statements where we use direct assignments instead:
# nums[2 * i] = nums[i] & 1023  
# nums[2 * i + 1] = nums[i] >> 10

# Consider the case when i = 0
# 1st assignment ends up modifying nums[0].
# 2nd assignment on its RHS uses nums[i], ie,  nums[0], which is already modified by the 1st assignment. Thus, we end up right shifting the 
# above mmodifed nums[0], and not the actual combined result which was earlier present at nums[0]. This leads to incorrect results.

# Read the below to understannd the Bit Manipulation approach:
# Binary Representation of decimal numbers: In binary, each bit represents an exponential increase in decimal number value by a power of two. Specifically, 
# 2^10 = 1024, which means 10 bits can represent any decimal number value from 0 to 1023. This range is sufficient to handle any 
# number up to 1000 comfortably. (The given problems states that the maximum value posssible for an element in the array is 1000.)

# 10-bit Shift Explanation: When you shift a number left by 10 bits (<< 10), you're effectively multiplying it by 
# 2^10 or 1024. By shifting the number left by 10 bits, we guarantee that there is enough space (10 binary positions) 
# to safely store another number up to 10 bits long without any risk of the two numbers interfering with each other.

# Step-by-Step Illustration with xi = 3 and yi = 6

# 1. Binary Representation of xi and yi:

# xi = 3, which in binary is 0000000011 (using at least 10 bits).
# yi = 6, which in binary is 0000000110 (using at least 10 bits).

# 2. Bit Shifting yi= 6 to the left by 10 bits:

#  6 << 10 in binary moves 6 (or 110) ten places to the left and gives the result as: 1100000000000.

# (yi << 10)  = 6 << 10 = 1100000000000

# Note:
# 10-bit Shift: The 10-bit shift moves 6 into the high bits of an integer, creating a large enough gap (ten zeros) between the 
# most significant bit of 6 and the least significant bit of 3. This ensures no overlap or interference between the two values.


# 3. Encoding/Combining xi and shifted yi into a single integer without losing information by using bitwise OR operation.

# xi | (yi << 10) =  0000000011 | 1100000000000 = 110000000011

# The result 110000000011 effectively contains both numbers.

# Breakdown of Bit Positions in the resultan binary 1100000000011(13 bits)
# (1)Lower 10 Bits (for xi): These bits include the final portion of the binary where xi = 3 is directly represented as 0000000011.
# (2)Remaining Bits (for yi): The remainng bits in the result, which are 3 in this case, represent yi.That is, yi is represented by 110 (ie, bits from 11th bit position to 13th bit position in the resultant binary).


# 4. Decoding the original xi and yi from the result 

# (A) The original  xi can be retrived by applying a mask that isolates the lower 10 bits of the result. As 1023 is 1111111111 in 
# binary, which masks exactly 10 bits, it is choosen as bitmask.

# Applying the bitmask(also called mask) to the result via AND operation: 1100000000011 & 0000001111111111 = 0000000011

# Here, the bitmask 1111111111 (which is 1023 in decimal) when applied using the AND operation, clears any bits that are beyond the 10th bit, ensuring that only the first/lower 10 bits, representing xi, are retained.



# (B) The original  yi can be retrived by right shifting the resultant binary by 10 bits.

# 1100000000011 >> 10 = 00000000110


# Note:
# What is a Bitmask?
# A bitmask is a sequence of bits that can manipulate and extract specific bits from binary numbers through bitwise operations. In
# simple words, a bitmask is a way to "select" the bits you're interested in. 

