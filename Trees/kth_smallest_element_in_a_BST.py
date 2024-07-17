#ref: https://leetcode.com/problems/kth-smallest-element-in-a-bst/solutions/682643/python-faster-than-100-in-order-traversal-using-stack-solution-easy/
#ref: https://www.youtube.com/watch?v=5LUXSvjmGCw&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=11
# notes: use a counter variable and do inorder traversal using stack.Return the popped node's value when count equals k.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 # counter for the popped node
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                count+=1
                if count==k:
                    return node.val
                node = node.right
