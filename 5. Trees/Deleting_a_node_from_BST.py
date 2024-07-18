#ref: Amulya's youtube video
#ref: leetcoder786786 solution(in comments) on page https://leetcode.com/problems/delete-node-in-a-bst/solutions/93374/simple-python-solution-with-explanation/?page=2
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
        
        if self.data is None:
            self.data = data
            return
        if self.data==data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)     
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def delete(self, data):

        if not self.data: # if tree is empty, just return it
            return None
        if data < self.data: # if key value is less than root value, find the node in the left subtree
            self.left = self.left.delete(data)
        elif data > self.data: # if key value is greater than root value, find the node in right subtree
            self.right = self.right.delete(data)
        else: #we found the node (ie, self.data == data), start to delete it
            if not self.right: # if it doesn't have right children, we delete the node then new root would be root.left
                return self.left
            if not self.left: # if it has no left children, we delete the node then new root would be root.right
                return self.right
                   
            # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            cur_node = self.right
            while cur_node.left: #traverse leftwise in the right subtree to find the minimum value in the right subtree
                cur_node = cur_node.left
            self.data = cur_node.data # replace value
            self.right = self.right.delete(cur_node.data) # delete the minimum node in right subtree
        return self 
    
    # preoder traversal
    def preorder(self):

        print(self.data)
        
        if self.left:
            self.left.preorder()
            
        if self.right:
            self.right.preorder()
              
# creating root node and inserting values in a binary
# for the below insertion, you can visualize the tree by referring to the figure given here:  https://www.askpython.com/python/examples/delete-a-binary-tree
root = BST(15)
root.insert(10)
root.insert(25)
root.insert(6)
root.insert(14)
root.insert(20)
root.insert(60)

root.preorder()
root.delete(14)
print('after deletion:')
root.preorder()


# using data as per Amulya's youtube video
root = BST(10)
root.insert(6)
root.insert(3)
root.insert(1)
root.insert(6)
root.insert(98)
root.insert(3)
root.insert(7)

root.preorder()
root.delete(10)
print('after deletion:')
root.preorder()


#ref:  https://leetcode.com/problems/delete-node-in-a-bst/solutions/3274735/450-solution-with-step-by-step-explanation/?languageTags=python3
#ref: https://www.youtube.com/watch?v=a-53QSxovUA
#ref: https://www.youtube.com/watch?v=petKaikRiIA
class Solution:
    def deleteNode(self, root, key):
        # If the root is None, return None
        if not root:
            return None
        
        # If the key to be deleted is less than the root's key,
        # then the function is recursively called with the left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # If the key to be deleted is greater than the root's key,
        # then the function is recursively called with the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # If the root has only one child, then the root is replaced with its child. Here, the case where root is having no child also gets handled here.
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # If the root has two children, then the inorder successor of the root (i.e., the smallest value in the right subtree) is found.
            else:
                node = root.right
                while node.left: # traversing as left as possible in the right subtree to find the smallest(minimum) value in the right subtree
                    node = node.left
                # The value of the inorder successor is copied to the root
                root.val = node.val
                # The inorder successor is then deleted from the right subtree of the root
                root.right = self.deleteNode(root.right, node.val)
        
        return root