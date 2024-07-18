# DFS recursive(postorder traversal)
#ref: https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/3088996/python-bfs-and-dfs-solution-with-intuition-approach-complexity-and-code-explained-o-n/?languageTags=python3&topicTags=depth-first-search%2Cbreadth-first-search
#ref: https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/2011835/python-dfs-recursive-dfs-iterative-and-bfs-solutions/?topicTags=stack
#ref: https://www.youtube.com/watch?v=hTM3phVI6YQ&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=23
#ref: https://www.youtube.com/watch?v=AWIJwNf0ZQE
#ref : https://www.youtube.com/watch?v=_pnqMz5nrRs
class Solution:
    def maxDepth(self, root):

        if not root:
            return 0# return -1 will be used if the height of tree is defined in terms of no. of edges, instead of no. of nodes, in the longest path between root node and any leaf node
        
        left_ht = self.maxDepth(root.left)  # height of left subtree
        right_ht = self.maxDepth(root.right) # height of right subtree
        
        return 1 + max(left_ht,right_ht)# Here, 1 is added is for the root node.
    
    
# note: height of tree = root node + maximum of height of left subtree or right subtree


# note: 
# How to visualize the tree structure from the root given in the form of a list in leetcode problems
# Example:
# root = [3,9,20,null,null,15,7]

#The above statment implies that the binary tree has 3 as the root and its strcuture is formed 
# by inserting the elements given in the list using level order traversal, as shown below:

   #             3
   #        9         20
   #   null  null   15   7


# DFS iterative using stack(preorder traversal)
# ref: https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/2011835/python-dfs-recursive-dfs-iterative-and-bfs-solutions/?topicTags=stack
class Solution:
    def maxDepth(self, root):
        stack = [(root,1)]
        max_depth = 0
        while stack:
            node,depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return max_depth   


# BFS using queue
#ref: https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/2011835/python-dfs-recursive-dfs-iterative-and-bfs-solutions/?topicTags=stack
class Solution:
    def maxDepth(self, root):
        from collections import deque
        queue = deque()
        queue.append((root,1))
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            if node:
                max_depth = max(max_depth, depth)
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
        return max_depth
   
  
#
