words = "a b c a b a c c".split()
freq, first_pos = {}, {}
print(words)
for i, w in enumerate(words):
    freq[w] = freq.get(w, 0) + 1
    if w not in first_pos:
        first_pos[w] = i

best = None
for w, c in freq.items():
    if best is None:
        best = w
    else:
        bw = best
        if c > freq[bw] or (c == freq[bw] and first_pos[w] < first_pos[bw]):
            best = w
print(best, freq[best])  # word + count
