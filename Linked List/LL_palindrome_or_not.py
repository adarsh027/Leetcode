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
LL.append("B")
LL.append("A")
LL.print_LL()   

#Ref: https://www.youtube.com/watch?v=yOzXms1J6Nk
# array solution
class Solution:
    def isPalindrome(self, head): 
        #find middle(slow)
        arr = []
        while head:
            arr.append(head.data)
            head = head.next
        l,r = 0, len(arr)-1
        while l<=r:
            if arr[l]!=arr[r]:
                return False
            l+=1
            r-=1
        return True

Solution().isPalindrome(LL.head)

#slow and fast pointer solution
class Solution:
    def isPalindrome(self, head): 
        #find middle(slow)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
            
        #reverse 2nd half  
        prev= None
        while slow:
            temp= slow.next
            slow.next= prev
            prev = slow
            slow = temp
          
        #check palindrome
        left, right = head, prev
        while right:
            if left.data!=right.data:
                return False
            left = left.next
            right = right.next
        return True
            

Solution().isPalindrome(LL.head)

