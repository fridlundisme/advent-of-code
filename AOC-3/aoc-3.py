def countTrees(treeline,down,right):
    trees = 0
    d = down
    r = right
    while down < len(treeline):
        currentline = treeline[down]
        if right == 180:
            print()
        char = currentline[right]
        if char == '#':
            trees = trees + 1

        right = right + r
        down = down + d
    return trees

if __name__ == "__main__":
    f = open('/home/fridlund/codeprojects/justforfun/advent-of-code/AOC-3/data/input.in','r')
    right = [1,3,5,7,1]
    down = [1,1,1,1,2]
    treeline = []

    for line in f.readlines():
        s = line.strip('\n')
        treeline.append(s * (7*31))
    trees = []
    treeproduct = 1
    for i,r in enumerate(right):
        d = down[i]
        trees.append(countTrees(treeline,d,r))
        treeproduct = treeproduct * trees[i]
        print("# Trees: ",trees[i])

    print(treeproduct)
    