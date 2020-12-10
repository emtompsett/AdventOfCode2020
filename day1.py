#advent of code 2020
#day 1

def getNums(inNums):
    for i in range(len(inNums)):
        for j in range(i+1, len(inNums)):
            for k in range(j+1, len(inNums)):
                if int(inNums[i]) + int(inNums[j]) == 2020:
                    return int(inNums[i]),int(inNums[j])
    return false;

def main():
    file = open("inputDay1.txt", "r");
    lines = file.read().strip().split();
    print(lines)
    nums = getNums(lines)
    print(nums[0] * nums[1])
        
main();
