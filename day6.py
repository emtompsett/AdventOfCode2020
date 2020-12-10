def part1(lines):
    count = 0
    print(len(lines))
    for l in lines:
        print(l)
        yes = []
        for i in range(len(l)):
            print(l[i])
            if l[i] not in yes:
                if l[i] != " ":
                    yes.append(l[i])
        count += len(yes)
    return count

def getGroupCount(group):
    group = splitGroup(group)
    print(group)
    alpha = "abcdefghijklmnopqrstuvwxyz";
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(len(alpha), len(counts))
    size = len(group)
    c = 0
    for p in group:
        print(p)
        for i in range(len(p)):
            print(p[i])
            counts[alpha.index(p[i])] += 1
    for count in counts:
        if count == len(group):
            c+=1
    return c


def part2(lines):
    c = 0
    print(len(lines))
    for l in lines:
        c+= getGroupCount(l)
    return c


def printCodes(lst):
    for l in lst:
        print(l)
        print("****");


def splitOnBlank(lst):
    newList = []
    curr = ""
    for l in lst:
        if l == "":
            newList.append(curr)
            curr = ""
        else:
            curr= curr + " " + l
    return newList

def splitGroup(group):
    grp = []
    curr = ""
    for i in range(1, len(group)):
        if group[i] != " ":
            curr += group[i]
        else:
            grp.append(curr)
            curr = ""
    grp.append(curr);
    #print("in splitGroup", type(grp))
    return grp

def main():
    file = open("inputDay6.txt", "r");
    orig = file.read().splitlines();
    newLst = splitOnBlank(orig);
    print(newLst);
    print(part2(newLst));

main()



["faded chartruse", "
