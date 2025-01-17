from datastruct.classes.lists import DoublyLinkedList, DoublyNode


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history: DoublyLinkedList[str] = DoublyLinkedList()
        self.history.insert(homepage)
        self.current: DoublyNode[str] = self.history.head

    def visit(self, url: str):
        self.current = self.history.insert_at(url, self.current.data)
        self.current.next = None

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.data
