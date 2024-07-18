#ref: https://www.youtube.com/watch?v=nPvjcQBplH4

class Stack:
    def __init__(self):
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()
 
    # Insert an item into the stack
    def push(self, data):
        # Move all elements from the first queue to the second queue
        while len(self.q1):
            self.q2.append(self.q1.pop())
 
        # Push the given item into the first queue
        self.q1.append(data)
 
        # Move all elements back to the first queue from the second queue
        while len(self.q2):
            self.q1.append(self.q2.pop())
 
    # Remove the top item from the stack
    def pop(self):
        # if the first queue is empty
        if not self.q1:
            print('Underflow!!')
            exit(0)
        # return the front item from the first queue
        front = self.q1.popleft()
        return front
    
    def top(self):
        return self.q1[0]
    
    def empty(self):
        return not len(self.q1)
    
    def size(self):
        return len(self.q1) 
 
