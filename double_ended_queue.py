# Design Double-ended Queue
# Solved 
# Design a Double-ended Queue class.

# Your Deque class should support the following operations:

# Deque() will initialize an empty queue.
# bool isEmpty() will return whether the queue is empty or not.
# void append(int value) will insert value at the end of the queue.
# void appendleft(int val) will insert value at the beginning of the queue.
# int pop() will remove and return the value at the end of the queue. If the queue is empty, return -1.
# int popleft() will remove and return the value at the beginning of the queue. If the queue is empty, return -1.
# Note: You should implement each operation in 
# O
# (
# 1
# )
# O(1) time complexity.

# Example 1:

# Input:
# ["isEmpty", "append", 10, "isEmpty", "appendLeft", 20, "popLeft", "pop", "pop", "append", 30, "pop", "isEmpty"]

# Output:
# [true, null, false, null, 20, 10, -1, null, 30, true]


class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None
        self.prev = None 

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head 

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        newNode.next = self.tail
        newNode.prev = self.tail.prev 
        self.tail.prev.next = newNode
        self.tail.prev = newNode 

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        newNode.next = self.head.next 
        newNode.prev = self.head 
        self.head.next.prev = newNode 
        self.head.next = newNode 

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1 
        removeNode = self.tail.prev 
        self.tail.prev = removeNode.prev 
        self.tail.prev.next = self.tail 
        return removeNode.val 
      

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        
        removeNode = self.head.next 
        self.head.next = removeNode.next 
        self.head.next.prev = self.head 
        return removeNode.val 
        
    
