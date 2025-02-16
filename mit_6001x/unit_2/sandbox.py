# Paste your code into this box
# s = 'azcbobobegghakl'

s = 'bobegghakl'
s = 'zyx'
s = 'cqnqiehzynwwre'

sub = ''
longest_sub = ''

if len(s) == 1:
    print("Longest substring in alphabetical order is: " + str(longest_sub))
sub = s[0]
longest_sub = s[0]
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        sub = sub + s[i + 1]
        if len(longest_sub) < len(sub):
            longest_sub = sub[:]
    else:
        sub = s[i+1]
        if len(longest_sub) < len(sub):
            longest_sub = sub[:]
print("Longest substring in alphabetical order is: ", longest_sub)
