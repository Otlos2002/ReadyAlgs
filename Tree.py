from typing import Any, List, Callable, Union
import graphviz
import queue
from collections import deque


class Queue:

    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size

    def enqueue(self, item):
        if self.available == 0:
            print('Queue Overflow!')
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.available -= 1

    def dequeue(self):
        if self.available == self.size:
            print('Queue Underflow!')
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1

    def peek(self):
        print(self.queue[self.front])

    def print_queue(self):
        print(self.queue)


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
            x.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        if (self == None):
            return

            # Standard level order traversal code
            # using queue
        q = []  # Create a queue
        q.append(self)  # Enqueue root
        while (len(q) != 0):

            n = len(q)

            # If this node has children
            while (n > 0):

                # Dequeue an item from queue and print it
                p = q[0]
                q.pop(0)
                print(p.value, end=' ')

                # Enqueue all children of the dequeued item
                for i in range(len(p.children)):
                    q.append(p.children[i])
                n -= 1

            print()  # Print new line between two levels

    def search(self, value: Any) -> Union['TreeNode', None]:
        pass

    def show(self, node: 'TreeNode'):
        if self.children:
            for child in self.children:
                if child.value == node.value:
                    print(child.value)


class Tree:
    root: TreeNode

    def __init__(self, drzewo: 'TreeNode'):
        self.root = drzewo

    def add(self, value: Any, parent_name: Any) -> None:
        if not parent_name:
            raise Exception('zly rodzic')
        else:
            parent_name.children.append(TreeNode(value))

    def for_each_deep_first(self, visit: Callable[['Tree'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['Tree'], None]) -> None:
        self.root.for_each_level_order(visit)

    def show(self, dot):
        return self.root.show(dot)