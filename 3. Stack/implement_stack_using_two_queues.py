#Short notes on stack and queues
# Stack
# In a stack, we add elements in LIFO (Last In, First Out) order. This means that the last element inserted in the stack will be the first one removed. The basic operations of a stack are:
# a.push — insert an element at the top
# b.pop — remove an element from the top
# Queue
# In a queue, we add elements in FIFO (First In, First Out) order, meaning that the first element inserted is the first one to be removed. The basic operations of the queue are:
# a.enqueue — insert an element at the rear
# b.dequeue — remove an element from the front

# Ref: https://www.techiedelight.com/implement-stack-using-queue-data-structure/
# Ref: https://www.youtube.com/watch?v=mDcP7tLuBhc
# Ref: https://stackoverflow.com/questions/22430803/implement-a-queue-using-two-stacks-python

class MyStack:
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
 
if __name__ == '__main__':
 
    keys = [1, 2, 3, 4, 5]
 
    # insert the above keys into the stack
    s = MyStack()
    for key in keys:
        s.push(key)

    print(s.pop())
 