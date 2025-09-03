words = ["eat","tea","tan","ate","nat","bat"]
groups = {}
for w in words:
    key = ''.join(sorted(w))            # canonical signature
    groups.setdefault(key, []).append(w)
print(list(groups.values()))
