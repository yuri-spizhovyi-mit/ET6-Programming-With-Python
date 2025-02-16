# Paste your code into this box 
#s = 'azcbobobegghakl'
s = 'sadfanabgsyoiaiwon'
sub = []
longest_sub = []
for char in s:
    if len(sub) == 0:
        sub.append(char)
    elif char > sub[-1]:
        sub.append(char)
        if len(longest_sub) < len(sub):
            longest_sub = sub
    else:
        sub = []
sub_sting = ''.join(longest_sub)
print('Longest substring in alphabetical order is: ' + sub_sting)
