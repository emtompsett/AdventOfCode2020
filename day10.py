def part1(lst):
    count = 0
    curr = 0
    ones = 0
    threes = 0
    #print(lst)
    while (count < len(lst)):
        ads = nextAdapter(curr, lst)
        #print(ads)
        if ads == -1:
            threes += 1
            
        elif ads - curr == 1:
            #print("1 diff")
            ones += 1
        elif ads - curr == 3:
            #print("3 diff")
            threes += 1
        curr = ads
        count+= 1
    #print( ones, threes+1)
    return ones,threes+1

def numBranches(start, dct, lst):
    #print("calling numBranches:", start)
    if start in dct:
        #print(start, dct[start])
        return dct[start]
    ads = allAdapters(start, lst, lst.index(start))
    #print(ads)
    s = 0
    for a in ads:
        #print("PATHS: ", a)
        s += numBranches(a, dct, lst)
    return s


def part2(lst):
    lst.insert(0,0);
    dct = {lst[len(lst)-1]:1}
    print(lst)

    for i in range(len(lst)-1, -1, -1):
       # print(dct)
        #print(i)
        #print(lst[i])
        n = numBranches(lst[i], dct, lst)
        #print(n)
        dct[lst[i]] = n
        #input()
    print(dct)
    return(dct[lst[0]])
    
    
    

def part2Try1(lst):
    des = []
    count = 0
    curr = 0
    while (count < len(lst)):
        ads = allAdapters(curr,lst)
        if len(ads) == 0:
            return des
        if len(ads) != 1:
            des.append(len(ads))
        curr = ads[0]
    return des


def allAdapters(val,lst, pos):
    ads = []
    for i in range(pos, len(lst)):
        #print("IN ALL ADAPTERS", val, pos)
        v = lst[i]
        if v <= val + 3 and v > val:
            ads.append(v)
    return ads


def nextAdapter(val, lst):
    ads = []
    for v in lst:
        #print(v, val)
        if v <= val + 3 and v > val:
            #print("next adapter:", v)
            #ads.append(v)
            return v
    return -1
    #return ads




def main():
    file = open("inputDay10.txt", "r");
    orig = file.read().splitlines();
    #print(orig)
    for i in range(len(orig)):
        orig[i] = int(orig[i])
    orig.sort()
    
    #ones, threes = part1(orig)
    #print(ones * threes)
    print(part2(orig))
            
            
            
main()
