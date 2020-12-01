# Advent of Code 2018
# Day 1


def freqChangeLine(string):
    string = string[:-1]
    num = int(string[1:])
    if string[0] == "-":
        num *= -1
    return num



def mainPart1():
    file = open("Day1_Input.txt","r");
    lines = file.readlines();
    freq = 0
    for line in lines:
        freq += freqChangeLine(line);
    print(freq);

def makeFreqList(lines):
    freqList = []
    freq = 0
    for line in lines:
        freq += freqChangeLine(line);
        if freq in freqList:
            print("THIS IS THE DUPLICATE ", freq)
        freqList.append(freq);
    return freqList
    

def mainPart2():
    freqList = []
    file = open("Day1_Input.txt","r")
    lines = file.readlines();
    duplicates = False;
    freqList = makeFreqList(lines)
    currFreq = freqList[-1]
    while not duplicates:
        for f in freqList:
            if f + currFreq in freqList:
                duplicates = True
                return f + currFreq
        currFreq = currFreq + freqList[-1]
        print(currFreq)
            

print(mainPart2())







