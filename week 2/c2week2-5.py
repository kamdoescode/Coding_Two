#Implement a circular queue

from collections import deque

class CircQueue:
    def __init__(self, data):
        self.storage = deque(data)

    def get(self):
        c = self.storage[0]
        self.storage.rotate(-1)
        return c
    
    def add(self, data):
        self.storage.append(data)

queueObject = CircQueue(["a", "b", "c", "d"])
print(queueObject.storage)
print(queueObject.get()) 
print(queueObject.storage)
