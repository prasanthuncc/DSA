class Stack:
    def __init__(self, size):
        self.top = -1
        self.stack = []
        self.capacity = size

    def size(self):
        return self.top + 1

    def is_full(self):
        return self.size() == self.capacity()

    def is_empty(self):
        return self.size() == 0

    def push(self, data):
        if not self.is_full():
            self.top += 1
            self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
