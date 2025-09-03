text = "To be or not to be that is the question"
freq = {}
for word in text.lower().split():
    freq[word] = freq.get(word, 0) + 1
print(freq)
