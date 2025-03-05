from datastruct.classes.lists import LinkedList


def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:
    # Implement solution here
    resultado = LinkedList()
    acarreo = 0

    current1 = l1.head
    current2 = l2.head

    while current1 or current2 or acarreo:
        num1 = current1.data if current1 else 0
        num2 = current2.data if current2 else 0
        total = num1 + num2 + acarreo
        acarreo = total // 10

        resultado.insert(total % 10)

        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next

    # Revertir la lista antes de retornarla
    resultado.head = reversar(resultado.head)

    return resultado


def reversar(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

