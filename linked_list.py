from node import Node

class LinkedList:
    def __init__(self, iterable):
        next_node = None
        for item in reversed(iterable):
            node = Node(item, next_node)
            next_node = node
        self.head = next_node

