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
L1= LinkedList()
L1.append("1")
L1.append("3")
L1.append("8")
L2= LinkedList()
L2.append("2")
L2.append("7")


#ref: https://www.youtube.com/watch?v=l92wSWAZmnI

class Solution:
    def merge_two_LL(self, L1, L2):
        dummy_node = Node(0)  
        cur_node = dummy_node
        while L1 and L2:
            if L1.data < L2.data:
                cur_node.next= L1
                L1 = L1.next
            else:
                cur_node.next= L2
                L2 = L2.next
            cur_node = cur_node.next
            
        if L1:
            cur_node.next =L1
        elif L2:
            cur_node.next =L2

        return dummy_node.next # return the address of 1st node in the resultant merged linked list

mergedLL_head = Solution().merge_two_LL(L1.head,L2.head)


def print_LL(head): # Traverse through LL and print all data and count of nodes.
    cur_node= head
    while cur_node is not None:# when cur_node is None, it means you have already visited all nodes
        print(cur_node.data)
        cur_node = cur_node.next
print_LL(mergedLL_head)

