aDict = {"a": ["aardvark", 2, 2, 2, 2], "c": ["coati", 2, 3, "coati"]}

# def biggest(aDict):
#   list_keys = aDict.keys()
#   longest = 0
#   for i in list_keys:
#     if len(aDict[list_keys[i]]) > longest
#       longest = len(i)
#   return longest

list_keys = aDict.keys()
aDict_num = {}
for i in list_keys:
    aDict_num[len(aDict[i])] = i
print(aDict_num)
max_num = max(aDict_num.keys())
print(aDict_num[max_num])
