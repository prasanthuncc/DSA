class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        self.q.pop(0)

    def display(self):
        print(self.q)
