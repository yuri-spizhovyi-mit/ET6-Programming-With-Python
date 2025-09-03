nums = [2, 7, 11, 15]
target = 9
seen = {}  # num -> index

ans = None
for i, x in enumerate(nums):
    need = target - x
    if need in seen:
        ans = (seen[need], i)
        break
    seen[x] = i
print(seen)
print(ans)  # (0, 1)
