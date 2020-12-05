
def part1(l, mX, mY):
    count = 0
    pos = [0,0]
    while pos[0] < len(l):
        #print(pos)
        if l[pos[0]][pos[1]] == '#':
            l[pos[0]][pos[1]] = 'X'
            count += 1;
        else:
             l[pos[0]][pos[1]] = 'O'
        pos[0] += mY
        pos[1] += mX
    return count


def extendPattern(l, num):
    for i in range(len(l)):
        l[i] = list(l[i] * num)
    return l

def printLines(lines):
    for l in lines:
        print(l)

def main():
    total = 1;
    file = open("inputDay3.txt", "r");
    orig = file.read().strip().split();
    slopes = [(1,1), (3,1), (5, 1), (7,1), (1, 2)]
    for slope in slopes:
        mX = slope[0]
        mY = slope[1]
        lines = list(orig)
        extended = extendPattern(lines, mX * len(lines))
        num = part1(extended, mX, mY)
        total *= num
        print("OUTPUT:", num)
    print(total);
    

main();


#print(lines)
#product = 1;
#
#for slope in slopes:
# mX = slope[0]
# mY = slope[1]
#print(lines)
#extended = []#product *= num
