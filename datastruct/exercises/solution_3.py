from datastruct.classes.lists import LinkedList
from datastruct.classes.lists import Node

def sort_list_by_insertion(linked_list: LinkedList[int]) -> LinkedList[int]:
    # Implement solution here
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    sorted_list = LinkedList[int]()
    current = linked_list.head

    while current:
       next_node = current.next
       insert_sorted(sorted_list, current)
       current = next_node
    return sorted_list

def insert_sorted(linked_list: LinkedList[int], node: Node) :
    if not linked_list.head or node.data < linked_list.head.data:
        node.next = linked_list.head
        linked_list.head = node
        return

    current = linked_list.head
    while current.next and current.next.data < node.data:
        current = current.next

    node.next = current.next
    current.next = node
