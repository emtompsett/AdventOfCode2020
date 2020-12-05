# day 4
def part1(codes):
    countV = 0
    for code in codes:
        code = splitAndSort(code)
        if valid(code):
            countV += 1

    return countV

def part2(codes):
    countV = 0
    for code in codes:
        code = splitAndSort(code)
        if valid(code) and allFieldsValid(code):
                countV += 1
    return countV

def splitAndSort(code):
    newCode = code.split(" ")
    newCode.remove("")
    newCode.sort();
    return newCode
    

def valid(c):
    if len(c) < 7:
        return False
    elif len(c) == 7:
        for i in range(len(c)):
            if c[i][0:3] == "cid":
                return False
    return True;

def toInt(string):
    num = 0;
    for s in string:
         if s.isdigit():
            num*=10
            num+=int(s)
        else:
            return -1
    return num

def isValidHex(c):
    pound = c[0] == "#";
    if len(c) != 7:
        return False
    c = c[1:]
    for ch in c:
        if not ch.isdigit() and ch not in "abcdef":
            return False
    return True

def isValidNineDigitNum(c):
    if len(c) != 9:
        return False
    for l in c:
        if not l.isdigit():
            return False
    return True
        
def validate(code):
    field = code[0:3]
    rest = code[4:]
    toReturn = True;
    if field == "byr":
        byr = toInt(rest)
        toReturn = byr >= 1920 and byr <=2002;
    elif field == "iyr":
        iyr = toInt(rest)
        toReturn = iyr >= 2010 and iyr <= 2020;
    elif field == "eyr":
        eyr = toInt(rest)
        toReturn = eyr >= 2020 and eyr <= 2030;
    elif field == "hgt":
        num = rest[0:-2]
        unit = rest[-2:]
        if unit == "cm":
           toReturn =  toInt(num) >= 150 and toInt(num) <= 193;
        elif unit == "in":
            toReturn =toInt(num) >= 59 and toInt(num) <= 76;
        else:
            toReturn = False

    elif field == "hcl":
        toReturn = isValidHex(rest)

    elif field == "ecl":
         if rest not in ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]:
             toReturn = False

    elif field == "pid":
        toReturn = isValidNineDigitNum(rest)
    return toReturn
            
        
def allFieldsValid(code):
    toRet = True
    for c in code:
        if not validate(c):
           toRet = False;
    return toRet;

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

def printCodes(lst):
    for l in lst:
        print(l)
        print("****");

def main():
    file = open("inputDay4.txt", "r");
    orig = file.read().splitlines();
    newLst = splitOnBlank(orig);
    printCodes(newLst);
    print(part2(newLst));
    
        
    
main();
