#use deque to implement to add and get methods
from collections import deque

class Queue:
    def __init__(self):
        self.storage = deque([1, 2, 3])
    
    def add(self, data):
        self.storage.append(data)

    def get(self):
        return self.storage.popleft()

queueObject = Queue()
queueObject.add(4)
queueObject.add(5)
print(queueObject.get())