#AoC day 2 2020

def part1(pWrds):
    #list of lists - [min, max, char, pwrd]
    valid = 0
    for p in pWrds:
        char = p[2]
        mn = p[0]
        mx = p[1]
        pW = p[3]
        countChar = 0
        for c in pW:
            #print(c)
            if c == char:
                countChar += 1
        #print(pW, countChar, mn, mx, countChar >=mn, countChar <=mx)        
        if countChar >= mn and countChar <= mx:
            #print("greater than min:",countChar >=mn)
            #print("Less than max:",countChar <= mx)
            valid += 1
            print(p, "is valid")
        else:
            print(p, "is not valid")
    return valid

def part2(pWrds):
    valid = 0
    for p in pWrds:
        char = p[2]
        first = p[0]-1
        second = p[1] - 1
        pW = p[3]

        if pW[first] == char and pW[second] != char or pW[first] != char and pW[second] == char:
            valid += 1
            print(pW, "is valid")
    return valid

def parseInput(lines):
    pWrds = []
    i = 0;
    while (i < len(lines)):
        nums = lines[i]
        i+=1
        letter = lines[i][:-1]
        i+=1
        pW = lines[i]
        i+=1
        nums = nums.strip().split("-");
        nums = [int(nums[0]), int(nums[1])]
        pWrds.append([nums[0], nums[1], letter, pW])
    return pWrds


        
def main():
    file = open("inputDay2.txt", "r");
    lines = file.read().strip().split();
    #print(lines)
    pwrds = parseInput(lines);
    print(part2(pwrds))

main();
        
