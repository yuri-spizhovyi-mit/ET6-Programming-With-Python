def get_list_of_items(lst: list, index: int) -> int:
    assert isinstance(lst, list), "Input must be a list"
    assert isinstance(index, int), "Index must be an integer"
    assert 0 <= index < len(lst), "Index out of range"
    return lst[index]


lst = [1, 2, 3]
i = 4
print(get_list_of_items(lst, i))  # Output: 2
