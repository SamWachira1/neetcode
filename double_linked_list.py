# 707. Design Linked List
# Solved
# Medium
# Topics
# Companies
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
 

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None
        self.prev = None 


class MyLinkedList:

    def __init__(self):
        self.head = Node(-1) 
        self.tail = Node(-1) 
        self.head.next = self.tail 
        self.tail.prev = self.head 
        

    def get(self, index: int) -> int:
        curr = self.head.next 
        
        i = 0 
        while curr and i < index:
            i += 1 
            curr = curr.next 
        if curr and i == index and curr != self.tail:
            return curr.val 
        return -1 
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next 
        newNode.prev = self.head 
        self.head.next.prev = newNode 
        self.head.next = newNode 
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev 
        self.tail.prev.next = newNode 
        self.tail.prev = newNode 

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head 
        i = 0 
        while i < index and curr.next != self.tail:
            i += 1 
            curr = curr.next 
        if i == index: 
            newNode = Node(val)
            newNode.next = curr.next 
            newNode.prev = curr
            curr.next = newNode 

            if newNode.next:
                newNode.next.prev = newNode 
            if not newNode.next: 
                self.tail = newNode 
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head 
        i = 0 

        while i < index and curr.next != self.tail:
            i += 1 
            curr = curr.next 
        if i == index and curr.next != self.tail:
            nodeToDelete = curr.next 
            curr.next = nodeToDelete.next 

            if nodeToDelete.next: 
                nodeToDelete.next.prev = curr 
            
            if nodeToDelete.next == self.tail: 
                self.tail.prev = curr 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
