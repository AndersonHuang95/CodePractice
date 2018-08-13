#!/usr/bin/env python3

class Node:
    """Node class for linked list implementation
    """
    def __init__(self, key, value): 
        """Constructor
        
        Args: 
            key (int) - key to initialize
            value (int) -  value to initialize 
        """
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache: 
    """An efficient LRU cache implementation using a linked list and a dictionary
    """
    def __init__(self, capacity):
        """Constructor
        
        Initializes a LRU cache with set capacity. A linked list keeps track of 
        all current items with the convention that items at the back of the list
        are more recently referenced, and items at the front are older. A dummy 
        head and dummy tail allow us to eliminate implementing special cases for 
        zero-element and one-element lists, which are tricky and time-consuming.
        A dictionary tracks existence of keys in the cache, allowing quick retrieval. 
        These two data structures allow 'get' and 'put' methods to return in constant 
        time. 

        Args: 
            capacity (int) - size of LRU cache
        """
        if capacity < 1: 
            raise ValueError("LRUCache capacity must be nonnegative")
        self.capacity = capacity
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.table = {}

    def get(self, key):
        """Returns the value of associated key, -1 if key is not in cache 

        At a deeper level, retrieving a key is a multi-step process
        1. Check if key exists in cache 
        2. If key exists, move the item to the end of the cache since we just accessed it
        3. Return the value 

        Args: 
            key (int) - key of item to retrieve

        Returns: 
            int - value of item retrieved, -1 if key is not in cache
        """
        if key in self.table: 
            node = self.table[key]
            self._remove_item(node)
            self._add_item(node)
            return node.value
        return -1 


    def put(self, key, value):
        """Adds a key with associated value to cache

        At a deeper level, inserting a key with value is a multi-step process
        1. Check if cache is at full capacity 
        2. If cache is full, remove oldest item (least recently used)
            a. This requires removing from the list, and deletion from the dictionary
        3. Create a new item 
        4. Add the item to the list and dictionary

        Args: 
            key (int) - key of item to insert
            value (int) - value of item to insert

        Returns:
            void - modifies cache in-place
        """
        if key in self.table: 
            node = self.table[key]
            self._remove_item(node) 
            self.table.pop(key)
        elif self.is_full():
            lru = self.head.next
            self._remove_item(lru)
            self.table.pop(lru.key)
        node = Node(key, value)
        self._add_item(node)
        self.table[key] = node

    def _add_item(self, node):
        """Updates cache list with item

        This action is equivalent to inserting at the end of the list

        Args:
            item (Node) - list node to insert

        Returns: 
            void - adds node in-place
        """
        prev = self.tail.prev
        node.prev = prev
        node.next = self.tail
        prev.next = node
        self.tail.prev = node


    def _remove_item(self, node):
        """Updates cache list by removing item

        This action is equivalent to maneuvering four pointers.

        Args:
            item (Node) - list node to remove

        Returns:
            void - removes node in-place
        """
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before

    def is_full(self):
        """Checks if LRU cache is at full capacity
        """
        return self.capacity == len(self.table)

def main(): 
    lru = LRUCache(2)
    assert lru.get(1) == -1
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(2) == 2
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

if __name__ == "__main__":
    main()

