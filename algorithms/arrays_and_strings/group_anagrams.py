from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))  # Sort characters to use as key
        anagram_map[key].append(word)

    return list(anagram_map.values())
