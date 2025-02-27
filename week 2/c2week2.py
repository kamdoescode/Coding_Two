#linked lists
from collections import deque

l = deque([1, 2, 3, 4, 5])
print(l)

l.appendleft(0)
print(l)

l.pop()
print(l)

l.popleft()
print(l)

for i in l:
    print(i)