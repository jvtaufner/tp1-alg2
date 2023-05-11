from functools import reduce

from Node import Node


def getNode(node: Node, char: str):
    return node.get_child(char)

class Trie:
    code = 1

    def __init__(self) -> None:
        self.root = Node(0)

    def insert(self, key: str) -> int:
        node = reduce(getNode, key, self.root)
        if node.value == -1:
            node.update(self.code)
            self.code += 1
        return node.value

    def find(self, key: str) -> int:
        node = reduce(getNode, key, self.root)
        return node.value
