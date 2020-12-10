
def part2(ids):
    ids.sort()
    mn = 23
    mx = 828
    i = 0
    while i < len(ids):
        if ids[i] != i + mn:
            print(i+mn)
            mn+=1
        i+=1
    return ids




def toBin(zero, one, string):
    num = 0
    for i in range(len(string)):
        #print (i, string[i])
        if string[i] == one:
            #print(len(string) - 1 - i)
            num += 2 ** (len(string) - 1 - i);
    return num

def main():
    file = open("inputDay5.txt", "r");
    orig = file.read().splitlines();
    print(orig)
    m = 0
    IDs = []
    for o in orig:
        first = o[:7]
        second = o[7:]
        row = toBin("F", "B", first)
        col = toBin("L", "R", second)
        seatID = row * 8 + col;
        IDs.append(seatID)
        print(row,col, seatID)
    print(IDs)
    print(part2(IDs))
main()
    
