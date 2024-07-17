# ref: https://leetcode.com/problems/count-good-nodes-in-binary-tree/solutions/3140956/12-lines-of-python-code-easy-to-understand-72-faster/?page=4&languageTags=python3
#ref: https://leetcode.com/problems/count-good-nodes-in-binary-tree/solutions/3185858/python-simple-dfs-solution/?languageTags=python3
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res= 0
        def dfs(node, cur_max) :
            if not node: 
                return 

            if node.val>=cur_max: 
                self.res += 1
                cur_max = node.val # computing cur_max like this inside the if statement is more efficient then putting computing it using the max() function as shown in the below commented statement
        #   cur_max = max(cur_max, node.val) # computing cur_max like this is less efficient
           
            dfs(node.left,cur_max)
            dfs(node.right,cur_max)

        dfs(root,float('-inf'))
        return self.res
    
  
#ref: https://leetcode.com/problems/count-good-nodes-in-binary-tree/solutions/3271577/recursive-dfs-with-python/?page=3&languageTags=python3    
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, cur_max):
            nonlocal res
            if not node:
                return
            if node.val >= cur_max:
                res += 1
                cur_max = node.val
            if node.left:
                dfs(node.left, cur_max)
            if node.right:
                dfs(node.right, cur_max)
        
        dfs(root, float('-inf'))
        return res
    

#ref: https://leetcode.com/problems/count-good-nodes-in-binary-tree/solutions/3478551/python-simple-clean-solution-using-dfs/?languageTags=python3
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(node, cur_max):
            if node.val >= cur_max:
                res[0] += 1
            cur_max = max(cur_max, node.val)
            if node.left:
                dfs(node.left, max(cur_max, node.val))
            if node.right:
                dfs(node.right, max(cur_max, node.val))
                
        dfs(root, float('-inf'))
        return res[0]
    
# BFS approach 
# ref : https://leetcode.com/problems/count-good-nodes-in-binary-tree/solutions/635351/bfs-with-maxvalue-template-of-similar-problems-python/?languageTags=python3
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque
        res = 0
        q = deque()
        q.append((root,float('-inf')))

        while q:
            node,cur_max = q.popleft()
            if node:
                if node.val >= cur_max:  
                    res += 1  
                cur_max = max(cur_max, node.val)  
                q.append((node.left,cur_max))
                q.append((node.right,cur_max))

        return res 
    


