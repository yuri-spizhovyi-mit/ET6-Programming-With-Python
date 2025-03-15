def bisection_search(L, e):
    def search_helper(L, e, low, high):
        if low > high:
            return False  # Base case: If search range is invalid, return False

        mid = (low + high) // 2  # Integer division midpoint

        if L[mid] == e:
            return True
        elif L[mid] > e:
            return search_helper(L, e, low, mid - 1)  # Search left half
        else:
            return search_helper(L, e, mid + 1, high)  # Search right input

    return search_helper(L, e, 0, len(L) - 1) if L else False


# Example usage:
L = [1, 2, 3, 4, 5]
e = 5
print(bisection_search(L, e))  # Output: True
print(bisection_search(L, 6))  # Output: False
