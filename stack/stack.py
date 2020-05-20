"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

array = [1, 2, 3, 7, 9, 3]
linkedList = [1, 4, 3, 2]


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        for item in self.storage:
            self.size += 1
        return self.size

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        del self.storage[-1]

joint = Stack()

joint.push(13)
joint.push(13)
joint.push(13)
joint.pop()

print(len(joint))