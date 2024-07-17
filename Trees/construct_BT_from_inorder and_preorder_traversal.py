#ref: https://www.youtube.com/watch?v=aZNaLrVebKQ
#ref: https://www.youtube.com/watch?v=PoBGyrIWisE
#ref: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/34579/Python-short-recursive-solution.
class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val) # Using the index method to retrive the index is an O(n) operation. In order to make it an O(1) operation, use dictionary.
# Note: You can further optimize the above code of retrieving the index by converting preorder to a deque since doing a popleft on a deque is more efficient than doing a pop(0) on a list.
        root.left = self.buildTree(preorder, inorder[:root_idx])
        root.right = self.buildTree(preorder, inorder[root_idx+1:])
        return root


# A more intuitive solution obtained from referrring solutions by michaelniki and pramttl and uncleiroh on https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/34579/Python-short-recursive-solution.

class Solution:
    def buildTree(self, preorder, inorder):
        
        if not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val) # Using the index method to retrive the index is an O(n) operation. In order to make it an O(1) operation, use dictionary .
        # when I used dictinary in this code, the efficiency didn't increase as dictinary was getting creating in every recursive call.
        # ignoring the root in the inorder subproblems, dividing problem in two parts
        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx+1:]
        
        # ignoring the root, which is the 1st element,ie, 0th indexed element  in the preorder subproblems, dividing
        # problem in two parts by using the length of the inorder subproblems. 
        preorder_left = preorder[1:root_idx+1]# this is same as  preorder_left = preorder[1: len(inorder_left) + 1]
        preorder_right = preorder[root_idx+1:] # this is same as preorder_right = preorder[len(inorder_left)+1:]
       
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
    
# optimized solution that makes use of the following:
# 1. A helper function that allows us to process inorder using start and end parameters.
# 2. A dictionary to store inorder indexes since retrieving index from a dictionary is an O(1) operation.

# Refer solution by charleszhou327 on https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/34579/Python-short-recursive-solution.
class Solution(object):
    def buildTree(self, preorder, inorder):
        inorder_dict = {}
        for i, num in enumerate(inorder):
            inorder_dict[num] = i
       
        def build(start, end):
            if start > end:
                return None
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            root_idx = inorder_dict[root_val]
            root.left = build(start,root_idx-1)
            root.right = build(root_idx+1, end)
            return root
        
        return build(0, len(inorder) - 1)  
 
#Alternatively, you can also Optimize by using an iterator an iterator for traversing through preorder.   
class Solution(object):
    def buildTree(self, preorder, inorder):
        inorder_dict = {}
        for i, num in enumerate(inorder):
            inorder_dict[num] = i
 
        preorder_iter = iter(preorder)
        
        def build(start, end):
            if start > end:
                return None
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            root_idx = inorder_dict[root_val]
            root.left = build(start,root_idx-1)
            root.right = build(root_idx+1, end)
            return root
        
        return build(0, len(inorder) - 1)  

# Note: which is faster deque.popleft() or list.pop(0) ?

# deque.popleft() is faster than list.pop(0), because the deque has been optimized to do popleft() approximately in O(1), while list.pop(0) takes O(n) 

# deque.popleft() is O(1) -- a constant time operation. While list.pop(0) is O(n) -- linear time operation: the larger the list the longer it takes.

# Why?
# CPython list implementation is array-based. pop(0) removes the first item from the list and it requires to shift 
# all the remaining (len(lst) - 1) items to fill the gap.

# deque() implementation uses a doubly linked list. No matter how large the deque, deque.popleft() requires a constant number of operations.

# https://stackoverflow.com/questions/32543608/deque-popleft-and-list-pop0-is-there-performance-difference



    