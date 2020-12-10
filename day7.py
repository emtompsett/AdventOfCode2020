#day 7
global checked

def makeList(lines):
    graph = {} #by contained in
    for line in lines:
        colors = splitLine(line)
        #print(colors)
        if colors[0] not in graph:
            graph[colors[0]] = []
        for i  in range(1, len(colors)):
            if colors[i] in graph:
                graph[colors[i]].append(colors[0])
            else:
                graph[colors[i]] = [colors[0]]
    #print(graph)
    return graph
            

def part2(lines):
    graph = {} #by contains
    for line in lines:
        colors = splitLine(line)
        counts = getCounts(line)
        contents = {}
        for i in range(1,len(colors)):
            contents[colors[i]] = counts[i-1]
        graph[colors[0]] = contents
   # print(graph)
    return graph

def countContained(graph, c):
    #base case
    #print("Beginning of this",graph[c])
    if graph[c] == {}:
        #print("returning 1")
        return 0
    count = 0
    for col in graph[c]:
        #print(col, graph[c][col])
        contained = countContained(graph, col)
        #print("Contained: ", contained)
        count += contained * graph[c][col]
        count += graph[c][col]
       # print("this is count now: ", count)
    #print(count)
    
    return count

def getCount(r):
    num = ""
    for char in r:
        if char.isdigit():
            num+= char
    return int(num)

def getCounts(line):
    counts = []
    first = line.split(" bags contain")
    if "no other" in first[1]:
        return counts
    rest = first[1].split(", ")
    for r in rest:
        c = getCount(r)
        counts.append(c)
    return counts


def splitLine(line):
    first = line.split(" bags contain")
    if "no other" in first[1]:
        return [first[0]]
    rest = first[1].split(", ")
    first = [first[0]]
    for r in rest:
        color = getColor(r)
        first.append(color)
    return first
    
def getColor(line):   
    newLn = ""
    for l in line:
        if not (l.isdigit() or not l.isalpha()) or l == " ":
            newLn = newLn + l
    if newLn[-1] == "s":
        newLn = newLn[1:-5]
    else:
        newLn = newLn[1:-4]
    if newLn[0] == " ":
        newLn = newLn[1:]
    return newLn
           
def countContains(graph, c):
    colors = []
    for col in graph[c]:
        colors.append(col)
    i = 0
    while i < len(colors):
        for col in graph[colors[i]]:
            if col not in colors:
                colors.append(col)
        i+=1
    return colors

def main():
        file = open("inputDay7.txt", "r");
        orig = file.read().splitlines();
        #print(orig);
        graph = part2(orig)
        print(countContained(graph, "shiny gold"))
        
        
main();
