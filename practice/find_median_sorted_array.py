def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A  # always binary search the smaller array

    m, n = len(A), len(B)
    total = m + n
    half = total // 2

    left, right = 0, m
    while True:
        i = (left + right) // 2  # partition A
        j = half - i  # partition B

        Aleft = A[i - 1] if i > 0 else float("-infinity")
        Aright = A[i] if i < m else float("infinity")
        Bleft = B[j - 1] if j > 0 else float("-infinity")
        Bright = B[j] if j < n else float("infinity")

        # Correct partition
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            right = i - 1
        else:
            left = i + 1
