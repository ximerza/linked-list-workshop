from datastruct.classes.lists import LinkedList


def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:
    if linked_list.is_empty():
        return linked_list

    current = linked_list.head
    current_pair = current.next
    new_head = current_pair

    while current and current_pair:
        next_pair = current_pair.next
        current_pair.next = current

        if next_pair and next_pair.next:
            current.next = next_pair.next
        else:
            current.next = next_pair
            break

        current = next_pair
        current_pair = next_pair.next

    if new_head:
        linked_list.head = new_head

    return linked_list
