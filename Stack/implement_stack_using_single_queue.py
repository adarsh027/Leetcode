class MyStack:
    def __init__(self):
        from collections import deque
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]
    
    def empty(self):
        return not len(self.q)
    
    def size(self):
        return len(self.q)
    
if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
 
    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
 
    print("current size: ", s.size())
