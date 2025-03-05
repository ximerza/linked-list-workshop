from datastruct.classes.lists import LinkedList


def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:
    # Implement solution here
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    cabeza_nueva = linked_list.head.next
    prev = None
    current = linked_list.head

    while current and current.next:
        par_siguiente = current.next.next
        segundo = current.next

        segundo.next = current
        current.next = par_siguiente

        if prev:
            prev.next = segundo

        prev = current
        current = par_siguiente

    linked_list.head = cabeza_nueva
    return linked_list

    return linked_list
