def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1  # pointer to the end of valid nums1
    p2 = n - 1  # pointer to the end of valid nums2
    p = m + n - 1  # pointer to the end of full nums1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # if nums2 still has elements, copy them
    nums1[: p2 + 1] = nums2[: p2 + 1]
