# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

# class LRUCache:

#     # requirements: get, put in O(1)
#     # when get is run, must update it to last
#     # need pointer to first and last

#     # first, put commanf must replace LRU
#     # get command should run in O(1) even if its in b/w
#     # store hash with pointers to nodes?
#     # on top of that use doubly linked list to maintain order??
    

#     def __init__(self, capacity: int):

#         self.curcapacity = curcapacity
#         self.maxcapacity = capacity
#         self.hashset = {}
#         self.head = None
#         self.tail = None
    
#     # helper functions?

#     def remove_tail(self):
#         if self.curcapacity == 0:
#             print("empty!")
          
#         elif self.curcapacity == 1:
#             self.curcapacity = 0
#             del self.tail
          
#         else:
#             self.curcapacity -= 1
#             temp = self.tail
#             self.tail = temp.prev
#             del temp
    
#     def remove_between(self,val):
#         if self.curcapacity == 0:
#             return
#         self.curcapacity -= 1
#         node = self.hashset[val]

#         if self.curcapacity == 1:
#             del node
#             self.head = None
#             self.tail = None
#             return
        
#         node
        



#     def insert_head(self, val):

#         if self.curcapacity == self.maxcapacity:
#             self.remove_tail()
#             self.curcapacity -= 1

#         temp = self.head
#         new = ListNode(val,temp,None)
#         temp.prev = new
#         self.head = new
#         self.curcapacity +=1

#     def get(self, key: int) -> int:
        
#         if key not in self.hashset:
#             v = -1
        
#         else:
#             if self.hashset[key] == self.tail

        
#         # remove from linked list and add as head
#         # if its tail, need to move tail to prev,+ check if only one elem
        
#         return v

#     def put(self, key: int, value: int) -> None:
        
#         if key not in hashset:
#             # delete tail
#             # insert as head
        
#         else:
#             # search and delete elem (if above maxcapacity)
#             # insert as head
            
# got the logic, i really dont care about the code

class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.head = ListNode()  # most recently used side
        self.tail = ListNode()  # least recently used side

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove node from wherever it currently is
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert node immediately after head
    def insert_head(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to most recently used position
        self.remove(node)
        self.insert_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # Move to most recently used
            self.remove(node)
            self.insert_head(node)

            return

        # New key
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert_head(node)

        # Over capacity -> remove LRU
        if len(self.cache) > self.capacity:
            lru = self.tail.prev

            self.remove(lru)
            del self.cache[lru.key]


