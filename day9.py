def part2(pream, num, nums):
    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums) - 1):
            currSum += int(nums[j])
            if num == currSum:
                return (i, j)
            if currSum > num:
                break
    return -1

def sums(pream, nums, pos):
    s = []
    #print(pos, pream)
    for i in range(pos - pream, pos):
        for j in range(pos - pream, pos):
            if j != i:
                s.append(int(nums[j]) + int(nums[i]))
    return s

def part1(pream, nums):
    for i in range(pream, len(nums)):
        if int(nums[i]) not in sums(pream, nums, i):
            return(nums[i])
            

def main():
    file = open("inputDay9.txt", "r");
    orig = file.read().splitlines();
    preamLen = int(input("enter preamble length"))
    print(orig);
    num = part1(preamLen, orig);
    start, end = part2(preamLen, int(num), orig);
    lst = []
    for i in range(start, end+1):
        lst.append(int(orig[i]))
    print(min(lst) + max(lst))
main()
