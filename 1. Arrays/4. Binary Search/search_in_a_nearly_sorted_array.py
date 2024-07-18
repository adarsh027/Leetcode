#ref: https://www.techiedelight.com/search-nearly-sorted-array-ologn-time/
def searchElement(nums, target):
 
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find middle index `mid` and compare nums[mid-1], nums[mid], and
        # nums[mid+1] with the target number
        mid = (left + right) // 2
 
        # return `mid` if the middle element is equal to the target number
        if nums[mid] == target:
            return mid
        # return `mid-1` if nums[mid-1] is equal to target number
        elif mid - 1 >= left and nums[mid - 1] == target:
            return mid - 1
        # return `mid+1` if nums[mid+1] is equal to target number
        elif mid + 1 <= right and nums[mid + 1] == target:
            return mid + 1
 
        # if the middle element is less than the target number,
        # reduce search space to the right sublist nums[mid+2…right]
        elif target > nums[mid]:
            left = mid + 2
 
        # if the middle element is greater than the target number,
        # reduce search space to the right sublist nums[left…mid-2]
        else:
            right = mid - 2
 
    # invalid input or number present is not on the list
    return -1

searchElement([2, 1, 3, 5, 4, 7, 6, 8, 9], 5)