#impliment stack and queue

#FILO
class Stack:
    def __init__(self):
        self.stackList = []
    
    def add(self, data):
        self.stackList.append(data)

    def get(self):
        return self.stackList.pop()

stackobject = Stack()
stackobject.add("hello")
stackobject.add("everyone")
stackobject.add("!!!")

print(stackobject.get())


#FIFO
class Queue:
    def __init__(self):
        self.queueList = []
    
    def add(self, data):
        self.queueList.append(data)

    def get(self):
        return self.queueList.pop(0)