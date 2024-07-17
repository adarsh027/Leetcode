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
LL.append("D")
LL.append("E")
LL.print_LL()   

# ref: https://www.youtube.com/watch?v=gfFn-OXxcgU (Nick White)
# https://www.youtube.com/watch?v=9-ubSA9GA3o

class Solution:
    def removeElements(self, head, val):
        # if head is the node to be removed  
        while head and head.data == val:
            head = head.next

        cur_node = head

        # Removing nodes other than head
        while cur_node and cur_node.next:
            if cur_node.next.data == val:
                cur_node.next=cur_node.next.next
            else:
                cur_node = cur_node.next
        return head


Solution().removeElements(LL.head,'D')


