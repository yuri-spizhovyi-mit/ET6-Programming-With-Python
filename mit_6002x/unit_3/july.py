import numpy


def loadFile():
    inFile = open("julytemps.txt")
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        # FILL THIS IN
        if len(fields) != 3 or "Boston" == fields[0] or "Day" == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    diffTemps = list(numpy.array(high) - numpy.array(low))
    return (low, high, diffTemps)


print(loadFile())
