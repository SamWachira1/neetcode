

# Merge Sort
# Solved 
# Implement Merge Sort.

# Merge Sort is a divide-and-conquer algorithm for sorting an array or list of elements. It works by recursively dividing the unsorted list into n sub-lists, each containing one element. Then, it repeatedly merges sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.

# Objective:

# Given a list of key-value pairs, sort the list by key using Merge Sort. If two key-value pairs have the same key, maintain their relative order in the sorted list.

# Input:

# pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).
# Example 1:

# Input:
# pairs = [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]

# Output:
# [(1, "date"), (2, "banana"), (5, "apple"), (9, "cherry"), (9, "elderberry")]
# Note: As you can see, the solution is always stable. The two pairs with the key 9 maintained their relative positions.

# Example 2:

# Input:
# pairs = [(3, "cat"), (2, "dog"), (3, "bird")]

# Output:
# [(2, "dog"), (3, "cat"), (3, "bird")]


# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs):
        if len(pairs) <= 1:
            return pairs 
        
        m = len(pairs) // 2 

        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        res = [] 
        i = j = 0 

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                res.append(left[i])
                i += 1 
            else:
                res.append(right[j])
                j += 1 

        res.extend(left[i:])
        res.extend(right[j:])

        return res 
