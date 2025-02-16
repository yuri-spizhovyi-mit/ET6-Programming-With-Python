import re

file_path = r"C:\Users\yspizhoviy\ET6-Programming-With-Python\mit_6001x\unit_2\she_loves_you.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Extract words only (ignoring punctuation)
she_loves_you = re.findall(r"\b\w+\b", text)

# print(words)  # Output clean list of words


def lyrics_to_frequencies(lyrics):
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict


beatles = lyrics_to_frequencies(she_loves_you)
# print(beatles)


def most_common_words(frequency):
    values = frequency.values()
    best = max(values)
    words = []
    for k in frequency:
        if frequency[k] == best:
            words.append(k)
    return (words, best)


mcw = most_common_words(beatles)
print(mcw)


def words_often(frequency, min_times):
    result = []
    done = False
    while not done:
        temp = most_common_words(frequency)
        if temp[1] >= min_times:
            result.append(temp)
            for w in temp[0]:
                del frequency[w]
        else:
            done = True
    return result


# print(words_often(beatles, 5))
