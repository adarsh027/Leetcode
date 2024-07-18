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

# ref: https://www.youtube.com/watch?v=S5bfdUTrKLM&t=237s

class Solution:
    def reorderLL(self, head):
        if not head:
            return head

        # find mid point
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        # slow.next: the starting node of 2nd half

        cur_node = slow.next
        prev_node = slow.next = None
        while cur_node:
            temp= cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node= temp

        # merge in-place
        first, second = head, prev_node

        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2


Solution().reorderLL(LL.head)