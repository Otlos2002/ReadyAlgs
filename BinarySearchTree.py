from typing import Any, Callable, List


class BinaryNode:
    value: Any
    # left_child: 'BinaryNode'
    # right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def find_min(self) -> 'BinaryNode':
        if self.left_child is None:
            return self
        return self.left_child.find_min()

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)

        visit(self)

        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def PrintTree(self):
        if self.left_child:
            self.left_child.PrintTree()
        print(self.value),
        if self.right_child:
            self.right_child.PrintTree()


f = print


def print(adres: Any) -> None:
    if isinstance(adres, BinaryNode):
        f(adres.value)
    else:
        f(adres)


class BinarySearchTree:
    # root: BinaryNode

    def __init__(self) -> None:
        self.root = None

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def insert(self, value: Any) -> None:
        self.root = self. __insert(self.root, value)

    def __insert(self, node: 'BinaryNode', value: Any) -> 'BinaryNode':
        if node is None:
            return BinaryNode(value)

        if node.value == value:
            return node
        elif node.value < value:
            node.right_child = self.__insert(node.right_child, value)
        else:
            node.left_child = self.__insert(node.left_child, value)

        return node

    def insert_list(self, list_: List[Any]) -> None:
        for x in list_:
            self.insert(x)

    def contains(self, value: Any) -> bool:
        temp = self.root

        while True:
            if temp.value == value:
                return True
            if temp.value < value:
                temp = temp.right_child
            else:
                temp = temp.left_child
            if temp is None:
                return False

    def remove(self, value: Any) -> None:
        self.root = self. __remove(self.root, value)

    def __remove(self, node: 'BinaryNode', value: Any) -> None:
        if node is None:
            return node

        if node.value < value:
            node.right_child = self.__remove(node.right_child, value)

        elif node.value > value:
            node.left_child = self.__remove(node.left_child, value)
        else:
            if node.left_child is None:
                temp = node.right_child
                node = temp
                return node
            if node.right_child is None:
                temp = node.left_child
                node = temp
                return node

            temp = self. find_min_value_node(node.right_child)
            node.value = temp.value

            node.right_child = self.__remove(node.right_child, temp.value)

        return node

    def find_min_value_node(self, node) -> BinaryNode:
        temp = node
        while temp.left_child is not None:
            temp = temp.left_child
        return temp

    def show(self) -> None:
        self.root = self.root.PrintTree()

