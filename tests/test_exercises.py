import pytest


@pytest.mark.parametrize(
    "l1_data, l2_data, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
        ([9, 8, 7], [6, 5, 4], [5, 4, 2, 1]),
        ([0, 1], [0, 9, 9], [0, 0, 0, 1])
    ],
)
def test_add_two_numbers(l1_data, l2_data, expected):
    from datastruct.classes.lists import LinkedList
    from datastruct.exercises.solution_1 import add_two_numbers

    l1 = LinkedList[int]()
    l2 = LinkedList[int]()
    for data in l1_data[::-1]:
        l1.insert(data)

    for data in l2_data[::-1]:
        l2.insert(data)

    result = add_two_numbers(l1, l2)
    assert list(result) == expected
    assert len(result) == len(expected)


@pytest.mark.parametrize(
    "data, expected",
    [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),
        ([], [])
    ]
)
def test_swap_nodes_in_pairs(data, expected):
    from datastruct.classes.lists import LinkedList
    from datastruct.exercises.solution_2 import swap_nodes_in_pairs

    linked_list = LinkedList[int]()
    original = LinkedList[int]()
    for value in data[::-1]:
        linked_list.insert(value)
        original.insert(value)

    result = swap_nodes_in_pairs(linked_list)

    if len(linked_list) > 1:
        assert result.head.data != linked_list.head.data

    assert list(result) == expected
    assert len(result) == len(expected)
