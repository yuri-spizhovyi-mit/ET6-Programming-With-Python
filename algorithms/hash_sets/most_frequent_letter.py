def most_frequent_letter(text: str) -> str:
    freq = {}
    for ch in text.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    return max(freq, key=freq.get) if freq else None


s = "The rain in SPAIN falls mainly on the plain!!!"
print(most_frequent_letter(s))  # Output: 'n'
