from quicksort import quicksort


def test_empty():
    assert quicksort([]) == []


def test_single():
    assert quicksort([1]) == [1]


def test_sorted_input():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_input():
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates():
    assert quicksort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_random():
    assert quicksort([9, 3, 7, 1, 8, 2, 5]) == [1, 2, 3, 5, 7, 8, 9]


def test_negative_numbers():
    assert quicksort([-2, 5, 0, -7, 3]) == [-7, -2, 0, 3, 5]


def test_original_not_modified():
    data = [3, 1, 2]
    quicksort(data)
    assert data == [3, 1, 2]
