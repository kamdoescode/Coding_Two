#Implement a reverse method
#implement a rotate method

from collections import deque

class Queue:
    def __init__(self):
        self.storage = deque()
    
    def add(self, data):
        self.storage.append(data)

    def get(self):
        return self.storage.popleft()

    def reverse(self):
        self.storage.reverse()

    def rotate(self, n):
        self.storage.rotate(n)

queueObject = Queue()
queueObject.add(1)
queueObject.add(2)
queueObject.add(3)
queueObject.add(4)
queueObject.add(5)
queueObject.add(6)
queueObject.reverse()
#queueObject.rotate(2)
print(queueObject.get())