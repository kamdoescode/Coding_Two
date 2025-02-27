#implement a queue with a maximum length

from collections import deque

class Queue:
    def __init__(self):
        #maxlen will remove the front element
        self.storage = deque()
        self.maxlength = 5
    def add(self, data):
        if len(self.storage) == self.maxlength:
            print("Max length reached")
        else:
            self.storage.append(data)

    def get(self):
        return self.storage.popleft()

queueObject = Queue()
queueObject.add(4)
queueObject.add(5)
queueObject.add(6)
queueObject.add(7)
queueObject.add(8)
print(queueObject.get()) #pops the first element to make the list 4 again
queueObject.add(9)
print(queueObject.get())