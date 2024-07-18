# ref: Amulya's youtube videos
#ref: https://stackoverflow.com/questions/5444394/how-to-implement-a-binary-search-tree-in-python
#ref: https://www.youtube.com/watch?v=9RHO6jU--GU
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert in BST
    def insert(self, data):
        
        if not self.data: # if the tree is empty, initialize the root and return
            self.data = data
            return
        
        if self.data==data:   # if the node already exists, just return
            return

        if data < self.data: # If less than root node, traverse left-wise recursively in the left substree and inserting when we don't find any left child.To traverse leftwise in the left subtree, we call insert function recursively on every left child node we come across.
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)   # inserting when there is no left child
                
        else:                 # If more than root node, traverse right-wise recursively in the left substree and inserting when we don't find any right child. To traverse leftwise in the left subtree, we call insert function recursively on every left child node we come across.
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)  # inserting when ther is no right child

# Function to search in BST
    def search(self, data):
        if not self.data:
            return None
        if data==self.data:
            return "Found"
        elif data < self.data and self.left:
            return self.left.search(data)
        elif data > self.data and self.right:
            return self.right.search(data)
        else:
            return "Not found" 
        
        
    def preorder(self):

        print(self.data)
        
        if self.left:
            self.left.preorder()
            
        if self.right:
            self.right.preorder()

        
    def inorder(self):

        if self.left:
            self.left.inorder()
            
        print(self.data)
            
        if self.right:
            self.right.inorder() 
            
            
            
    def postorder(self):

        if self.left:
            self.left.postorder()
            
        if self.right:
            self.right.postorder() 
            
        print(self.data)
                       
    def min(self):    # min. value will lie in the left subtree of root and will be the leftmost node.
        cur_node = self
        while cur_node and cur_node.left: # traverse leftwise until there is no left child
            cur_node = cur_node.left
        return cur_node

    def max(self):    # max. value will lie in the right subtree of root and will be the rightmost node.
        cur_node = self
        while cur_node and cur_node.right: # traverse leftwise until there is no left child
            cur_node = cur_node.right
        return cur_node   
            
    # function to print a BST (inorder traversal)
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
            
                    
    
# creating root node and inserting values in a binary
# for the below insertion, you can visualize the tree by referring to the figure given here: https://www.askpython.com/python/examples/delete-a-binary-tree
# root = BST(None) # BST is empty
root = BST(15)
root.insert(10)
root.insert(25)
root.insert(6)
root.insert(14)
root.insert(20)
root.insert(60)
root.preorder()
# searching the values
print(root.search(14))