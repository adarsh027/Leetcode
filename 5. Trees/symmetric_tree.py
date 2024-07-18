#ref: https://leetcode.com/problems/symmetric-tree/solutions/3169564/solution/?page=2&languageTags=python3
#ref: https://www.youtube.com/watch?v=Mao9uzxwvmc
# using inner function isMirror()
class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        if not root:
            return True
        else:
            return isMirror(root.left, root.right)  

 
# using instance method isMirror()        
#ref: https://leetcode.com/problems/symmetric-tree/solutions/2423766/easy-0-ms-100-fully-explained-java-c-python-js-python3/?languageTags=python3   
class Solution(object):
    def isSymmetric(self, root):
        # Special case...
        if not root:
            return True;
        else:
            return self.isMirror(root.left, root.right)
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isMirror(self, t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)