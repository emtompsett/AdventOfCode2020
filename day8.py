#day 8

def part1(opps):
    visited = []
    accumulator = 0
    pos = 0
    while pos not in visited:
        print(pos)
        visited.append(pos)
        op = opps[pos][0]
        val = opps[pos][1]
        neg = 1;
        if val[0] == "-":
            neg = -1;
        val = int(val[1:]) * neg
        if op == "acc":
            accumulator += val
            pos += 1
        elif op == "jmp":
            pos += val
        else:
            pos += 1
 
    return accumulator
        
        
    
def part2(opps, numSwap):   
    visited = []
    accumulator = 0
    pos = 0
    if opps[numSwap][0] == "acc":
        return None
    while pos not in visited and pos < len(opps):
        #print(pos)
        op = opps[pos][0]
        val = opps[pos][1]
        neg = 1;
        if val[0] == "-":
            neg = -1;
        val = int(val[1:]) * neg
                
        if pos == numSwap:
            if op == "jmp":
                op = "nop"
            else:
                op = "jmp"
        visited.append(pos)
        if op == "acc":
            accumulator += val
            pos += 1
        elif op == "jmp":
            pos += val
        else:
            pos += 1
    if pos == len(opps):
        return accumulator
    return None
    #return accumulator




def main():
    file = open("inputDay8.txt", "r");
    orig = file.read().splitlines();
    for i in range(len(orig)):
        orig[i] = orig[i].split();
    #print(orig);
    for i in range(len(orig)):
        var = part2(orig,i)
        if var != None:
            print(var)
main();
