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
    for value in data[::-1]:
        linked_list.insert(value)

    original_head_id = id(linked_list.head)

    result = swap_nodes_in_pairs(linked_list)

    new_head_id = id(result.head)

    if len(linked_list) > 1:
        assert original_head_id != new_head_id

    assert list(result) == expected
    assert len(result) == len(expected)

@pytest.mark.parametrize(
    "data, expected",
    [
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([1, 3, 2, 4], [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 3, 2], [1, 2, 3]),
        ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]),
        ([1, 3, 2, 5, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([], [])
    ]
)
def test_sort_list_by_insertion(data, expected):
    from datastruct.classes.lists import LinkedList
    from datastruct.exercises.solution_3 import sort_list_by_insertion

    linked_list = LinkedList[int]()
    for value in data:
        linked_list.insert(value)

    result = sort_list_by_insertion(linked_list)
    assert list(result) == expected
    assert len(result) == len(expected)


@pytest.mark.parametrize(
    "operations, params, expected",
    [
        (
            ["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back", "back"],
            [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]],
            [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com", "google.com", "leetcode.com"]
        )
    ]
)
def test_browser_history(operations, params, expected):
    from datastruct.exercises.solution_4 import BrowserHistory

    browser_history = None
    results = []
    for operation, param in zip(operations, params):
        if operation == "BrowserHistory":
            browser_history = BrowserHistory(*param)
            results.append(None)
        else:
            method = getattr(browser_history, operation)
            results.append(method(*param))

    assert results == expected
    assert len(results) == len(expected)
    assert all(result is None or isinstance(result, str) for result in results)