from collections.abc import Callable
from typing import Any, override

from datastruct.classes.util import identity


class Node[T]:
    def __init__(self, data: T):
        self.data: T = data
        self.next: Node[T] | None = None


class LinkedList[T]:

    def __init__(self):
        self.head: Node[T] | None = None

    def is_empty(self):
        return self.head is None

    def insert(self, data: T):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = identity):
        if self.is_empty():
            raise Exception("List is empty")
        current = self.head
        while current:
            if key(current.data) == goal:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise Exception("Key not found")

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        if self.is_empty():
            raise Exception("List is empty")
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def find(self, goal: Any, key: Callable[[T], Any] = identity) -> Node[T] | None:
        current = self.head
        while current:
            if key(current.data) == goal:
                return current
            current = current.next
        return None

    def __contains__(self, item):
        return self.find(item) is not None

    def delete(self, goal: Any, key: Callable[[T], Any] = identity):
        if self.is_empty():
            raise Exception("List is empty")

        if key(self.head.data) == goal:
            self.head = self.head.next
            return

        current = self.head
        previous = None
        while current:
            if key(current.data) == goal:
                previous.next = current.next
                return
            previous = current
            current = current.next

        raise Exception("Key not found")

    def clear(self):
        self.head = None

    def __len__(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        return f"LinkedList([{', '.join(repr(data) for data in self)}])"

    def __str__(self) -> str:
        return " -> ".join(str(data) for data in self)


class OrderedLinkedList[T](LinkedList):

    def __init__(self, key: Callable[[Any], Any] = identity):
        super().__init__()
        self.key: Callable[[Any], Any] = key

    @override
    def insert(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        if self.key(self.head.data) > self.key(data):
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if self.key(current.next.data) > self.key(data):
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        current.next = new_node

    @override
    def find(self, goal: Any, key: Callable[[T], Any] = identity) -> Node[T] | None:
        return super().find(goal, self.key)

    @override
    def delete(self, goal: Any, key=identity):
        super().delete(goal, self.key)

    @override
    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = identity):
        raise NotImplementedError("insert_at is not supported for OrderedLinkedList")

    @override
    def reverse(self):
        raise NotImplementedError("reverse is not supported for OrderedLinkedList")

    @override
    def append(self, data: T):
        raise NotImplementedError("append is not supported for OrderedLinkedList")

    def __repr__(self):
        return f"OrderedList([{', '.join(repr(data) for data in self)}])"


class DoubleEndedLinkedList[T](LinkedList):
    def __init__(self):
        super().__init__()
        self.tail: Node[T] | None = None

    def insert(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    @override
    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    @override
    def delete(self, goal: Any, key: Callable[[Any], Any] = identity):
        if self.is_empty():
            raise Exception("List is empty")
        if key(self.head.data) == goal:
            self.head = self.head.next
            return

        current = self.head.next
        previous = self.head
        while current:
            if key(current.data) == goal:
                if current == self.tail:
                    self.tail = previous
                previous.next = current.next
                return
            previous = current
            current = current.next
        raise Exception("Key not found")

    @override
    def reverse(self):
        super().reverse()
        self.head, self.tail = self.tail, self.head


class CircularLinkedList[T](DoubleEndedLinkedList[T]):
    def __init__(self):
        super().__init__()

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            return

        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = identity):
        if self.is_empty():
            raise Exception("List is empty")

        current = self.head
        while current:
            if key(current.data) == goal:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            if current == self.tail:
                raise Exception("Key not found")
            current = current.next

    def find(self, goal: Any, key: Callable[[T], Any] = identity) -> Node[T] | None:
        if self.is_empty():
            return None

        current = self.head
        while current:
            if key(current.data) == goal:
                return current
            if current == self.tail:
                return None
            current = current.next

    def __len__(self):
        if self.is_empty():
            return 0

        count = 1
        current = self.head
        while current != self.tail:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        if self.is_empty():
            return

        current = self.head
        while current != self.tail:
            yield current.data
            current = current.next
        yield self.tail.data


class DoublyNode[T]:
    def __init__(self, data: T):
        self.data: T = data
        self.next: DoublyNode[T] | None = None
        self.prev: DoublyNode[T] | None = None


class DoublyLinkedList[T]:

    def __init__(self):
        self.head: DoublyNode[T] | None = None

    def is_empty(self):
        return self.head is None

    def insert(self, data: T):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = identity):
        if self.is_empty():
            raise Exception("List is empty")
        current = self.head
        while current:
            if key(current.data) == goal:
                new_node = DoublyNode(new_data)
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                return
            current = current.next
        raise Exception("Key not found")

    def append(self, data: T):
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def reverse(self):
        if self.is_empty():
            raise Exception("List is empty")
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            current.prev = next_node
            previous = current
            current = next_node
        self.head = previous

    def find(self, goal: Any, key: Callable[[T], Any] = identity) -> DoublyNode[T] | None:
        current = self.head
        while current:
            if key(current.data) == goal:
                return current
            current = current.next
        return None

    def delete(self, goal: Any, key: Callable[[T], Any] = identity):
        if self.is_empty():
            raise Exception("List is empty")
        if key(self.head.data) == goal:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if key(current.next.data) == goal:
                current.next = current.next.next
                return
            current = current.next
        raise Exception("Key not found")

    def clear(self):
        self.head = None

    def __contains__(self, item):
        return self.find(item) is not None

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return " <-> ".join(map(str, result))

    def __repr__(self):
        return f"DoublyLinkedList([{', '.join(repr(data) for data in self)}])"
