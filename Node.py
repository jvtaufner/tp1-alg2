from typing_extensions import Self


class Node:
    def __init__(self, value: int = -1) -> None:
        self.value = value
        self.children: list[Self] = []

    def update(self, value: int) -> None:
        self.value = value

    def get_child(self, key: str) -> Self:
        if not self.children:
            self.children = list(map(Node, [-1] * 256))

        if ord(key) > 256:
            print(key, ord(key))
        return self.children[ord(key)]
