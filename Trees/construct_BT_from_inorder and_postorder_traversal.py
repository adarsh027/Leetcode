#ref: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/3304658/easiest-8lines-only-python3/?languageTags=python3
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root_val=postorder[-1]
        root=TreeNode(root_val)
        root_idx=inorder.index(root_val)
        #exclude root while building left and right subtree of root
        root.left=self.buildTree(inorder[:root_idx],postorder[:root_idx])
        root.right=self.buildTree(inorder[root_idx+1:],postorder[root_idx:-1])
        return root
    
# Intuitive solution 
#ref: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/3304658/easiest-8lines-only-python3/?languageTags=python3
class Solution:
    from collections import deque
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:       
        if not inorder:
            return None
        
        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val) # Using the index method to retrive the index is an O(n) operation. In order to make it an O(1) operation, use dictionary .
        # when I used dictinary in this code, the efficiency didn't increase as dictinary was getting creating in every recursive call.
        # ignoring the root in the inorder subproblems, dividing problem in two parts
        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx+1:]
        
        # ignoring the root, which is the last element in the postorder subproblems, dividing
        # problem in two parts by using the length of the inorder subproblems. 
        postorder_left = postorder[:root_idx]# this is same as  postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[root_idx:-1] # this is same as postorder_right = postorder[len(inorder_left):-1]
       
        
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        
        return root



# optimized solution that makes use of the following:
# 1. A helper function that allows us to process inorder using start and end parameters.
# 2. A dictionary to store inorder indexes since retrieving index from a dictionary is an O(1) operation.

#ref: https://www.youtube.com/watch?v=vm63HuIU7kw (neetcode)
#ref: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/3302339/python3-solution/?languageTags=python3
#ref: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/3304474/good-code-is-readable-code/?languageTags=python3
class Solution(object):
    def buildTree(self, inorder, postorder):
        inorder_dict = {}
        for i, num in enumerate(inorder):
            inorder_dict[num] = i
 
        def build(start, end):
            if start > end:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            root_idx = inorder_dict[root_val]
            root.right = build(root_idx+1, end)
            root.left = build(start,root_idx-1)
            return root
        
        return build(0, len(inorder) - 1)  
    
    
#Understanding how mutable objects like lists and dictionaries defined outside a function can be accesed/modified inside that function
#ref: https://stackoverflow.com/questions/14323817/global-dictionaries-dont-need-keyword-global-to-modify-them
    
stringvar = "mod"
count = 0
dictvar = {'key1': 1,
           'key2': 2}
lst=[1,2,3]

# lst = lst + [4,5]
# print(lst) # prints [1, 2, 3, 4, 5]

def mutable_test():
    dictvar['key1'] += 1
    dictvar['key2'] = 22
    lst[0] = lst + [4,5]# you can't use lst = lst + [4,5]

def non_mutable_test():
    stringvar = "bar" # Here, strinvar is a local variable
    count = 1         # Here, count is a local variable
    print(stringvar, count)

print(dictvar, lst)
mutable_test()
print(dictvar, lst)

print(stringvar,count)
non_mutable_test()
print(stringvar, count)
