from binary_search import binary_search


def test_found_middle():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_found_first():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_found_last():
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_not_found():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_empty_list():
    assert binary_search([], 1) == -1


def test_single_element():
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) == -1


def test_two_elements():
    assert binary_search([2, 8], 2) == 0
    assert binary_search([2, 8], 8) == 1
