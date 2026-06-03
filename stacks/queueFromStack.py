class MyQueue(object):

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.push_stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.pop_stack:
            return self.pop_stack.pop()
        
        N = len(self.push_stack)
        for _ in range(N-1):
            self.pop_stack.append(self.push_stack.pop())
        return self.push_stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.pop_stack:
            return self.pop_stack[-1]
        
        N = len(self.push_stack)
        for _ in range(N):
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        leng = len(self.push_stack) + len(self.pop_stack)
        return leng == 0
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()

obj.push(1)
obj.push(2)
obj.push(3)

print(obj.pop())
print(obj.peek())
print(obj.empty())