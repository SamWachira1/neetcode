# When we want to remove an element from the last index of an array, 
# setting its value to 0 / null or -1 is the best we can do. 
# This is known as a soft delete. The element is not being "deleted" 
# per se, but it is being overwritten by a value that denotes an
# empty index. We will also reduce the length by 1 since we 
# have one less element in the array after deletion.

# we could also use pop()
# Time and space complexity? O(1) both

def removeEnd(arr, length) -> int:
    if length > 0:
        # Overwrite last element with some default value (optional).
        arr[length - 1] = 0
        
        # Decrease the logical length of the list.
        return length - 1
    
    # Return the original length if array is empty.
    return length

# print(removeEnd([1,3,5], 3))


# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.

# A better approach would be the following:

# We are given the deletion index i.
# We iterate starting from i + 1 until the end of the array.
# We shift each element 1 position to the left.
# (Optional) We replace the last element with a 0 or null to mark it empty, and decrement the length by 1.

def removeMiddle(arr, i, length):
    
    # for index in range(i, length - 1):
    #     arr[index] = arr[index + 1]
    # return arr 
       
         #  OR 
    
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    return arr 




print(removeMiddle([4,5,6], 1, 3))


# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n 
    



# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):

    # Why Use i - 1?
    # You need to move elements starting from the end of the array 
    # (index length - 1) to just past the position 
    # where the new element will be inserted.

    # By stopping at i - 1, you ensure that the element at 
    # index i will not be overwritten by the shift operation. 
    # You want to preserve the element 
    # that will be at index i after the shift.

    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    
    arr[i] = n 
    return arr 
  
   
print(insertMiddle([4,5,6, None], 1, 8, 3))




# Build a Double-linkedList 

class Node:
    def __init__(self, val, next_Node = None, prev_Node=None):
        self.val = val 
        self.next = next_Node
        self.prev = prev_Node 

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
        if curr and curr != self.tail and i == index:
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
        
        # Traverse to the node just before the index
        while i < index and curr.next != self.tail:
            i += 1 
            curr = curr.next 
        
        # Only insert if the index is within bounds
        if i == index:
            newNode = Node(val)
            newNode.next = curr.next 
            newNode.prev = curr
            curr.next = newNode
            
            # Update the next node's previous pointer if it's not the tail
            if newNode.next:
                newNode.next.prev = newNode

            # Update the tail's previous pointer if newNode is the last node
            if not newNode.next:
                self.tail = newNode 

                
                
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head 
        i = 0 

        while i < index and curr.next != self.tail:
            i += 1
            curr = curr.next 
        
        if curr.next != self.tail and i == index:
            to_delete = curr.next
            curr.next = to_delete.next  

            if to_delete.next:
                to_delete.next.prev = curr 

            if to_delete.next == self.tail:
                self.tail.prev = curr


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
