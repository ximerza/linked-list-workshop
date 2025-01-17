from datastruct.classes.lists import LinkedList


def sort_list_by_insertion(linked_list: LinkedList[int]) -> LinkedList[int]:
    """
    Sort a linked list using insertion sort. In the same list (Do not create another)
    :param linked_list:
    :return:
    """
    if linked_list.is_empty():
        return linked_list

    current = linked_list.head
    while current:
        next_node = current.next
        if next_node and current.data > next_node.data:
            previous = None
            temp = linked_list.head
            while temp and temp.data < next_node.data:
                previous = temp
                temp = temp.next

            if previous:
                current.next = next_node.next
                next_node.next = temp
                previous.next = next_node
            else:
                current.next = next_node.next
                next_node.next = linked_list.head
                linked_list.head = next_node
        else:
            current = next_node

    return linked_list

