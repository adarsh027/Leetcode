class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_LL(self,rhead=None): # Traverse through LL and print all data and count of nodes.
        count=0
        if self.head is None:
           print("LL is empty")
        else: 
            cur_node= self.head
            while cur_node is not None:# when cur_node is None, it means you have already visited all nodes
                print(cur_node.data)
                cur_node = cur_node.next
                count=count+1
        print(count)
        
    def append(self, data): # remember for append, you need to make the next of last node to point to the new node.
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
        cur_node = self.head
        while cur_node.next is not None: # when cur_node.next is None, it means you are at the last node.
            cur_node = cur_node.next
        cur_node.next = new_node 
LL= LinkedList()
LL.append("A")
LL.append("B")
LL.append("C")
LL.print_LL()        
# As the linked has been built, we can now proceed to reverse it.

# reference: https://www.youtube.com/watch?v=ugQ2DVJJroc&t=5s
#iterative solution
class Solution:
    def reverse_LL(self, head): 
        cur_node = head
        prev_node = None 
        # we have to assign the next of current node
        #to prev_node and keep moving prev_node further by 
        # assigning it the cur_node.
        while cur_node is not None:
            temp= cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node= temp
        return prev_node # prev_node(which is a node object) is the new head and points to the 1st node in the reversed LL.
    
    def print_rLL(self,new_head): 
            cur_node= new_head
            while cur_node is not None:# when cur_node is None, it means you have already visited all nodes
                print(cur_node.data)
                cur_node = cur_node.next

           

new_head=Solution().reverse_LL(LL.head)
Solution().print_rLL(new_head)

#recursive solution
class Solution:
    def reverse_LL(self, head): 
        if not head or not head.next:
            return head
        new_head = self.reverse_LL(head.next)
        head.next.next= head
        head.next = None
        return new_head
        
     
    def print_rLL(self,new_head): 
            cur_node= new_head
            while cur_node is not None:# when cur_node is None, it means you have already visited all nodes
                print(cur_node.data)
                cur_node = cur_node.next

new_head=Solution().reverse_LL(LL.head)
Solution().print_rLL(new_head)