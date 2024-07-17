#Ref:
#https://www.youtube.com/watch?v=wjYnzkAhcNk
# https://www.youtube.com/watch?v=PvrxZaH_eZ4&list=PL3edoBgC7ScV9WPytQ2dtso21YrTuUSBd&index=6
class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break

        return slow
        
Solution().findDuplicate([1,3,4,2,2])
