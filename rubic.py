from copy import deepcopy
import random


def ColorNumberToText(n):
    if(n==1): return 'Red'
    elif(n==2): return 'Green'
    elif(n==3): return 'Orange'
    elif(n==4): return 'Blue'
    elif(n==5): return 'Yellow'
    elif(n==6): return 'White'
    else: return 'Error'

#currently other peices only support size 3
def BuildCubeSizeN(n=3):
    #all cubes have six sides
    cube = []
    for x in range(6):
        y=x+1#lets just refer to y for non-indexes
        currentSide = []
        for j in range(n):
            currentRow=[]
            for k in range(n): #all sides are cubes
                currentRow.append(y)
            currentSide.append(currentRow)
        cube.append(currentSide)
    return cube

#reference image for visual
#will eventually need GUI
def TurnRed(cube,layer=0):
    #red side
    TurnSide(cube,0)
    a = cube[1][0][2]
    b = cube[1][1][2]
    c = cube[1][2][2]
    cube[1][2][2] = cube[5][2][0]
    cube[1][1][2] = cube[5][2][1]
    cube[1][0][2] = cube[5][2][2]
    cube[5][2][0] = cube[3][0][0]
    cube[5][2][1] = cube[3][1][0]
    cube[5][2][2] = cube[3][2][0]
    cube[3][2][0] = cube[4][0][0]
    cube[3][1][0] = cube[4][0][1]
    cube[3][0][0] = cube[4][0][2]
    cube[4][0][0] = a
    cube[4][0][1] = b
    cube[4][0][2] = c
    return cube
def TurnGreen(cube,layer=0):
    #green side
    TurnSide(cube,1)
    a = cube[2][0][2]
    b = cube[2][1][2]
    c = cube[2][2][2]
    cube[2][2][2] = cube[5][0][0]
    cube[2][1][2] = cube[5][1][0]
    cube[2][0][2] = cube[5][2][0]
    cube[5][0][0] = cube[0][0][0]
    cube[5][1][0] = cube[0][1][0]
    cube[5][2][0] = cube[0][2][0]
    cube[0][0][0] = cube[4][0][0]
    cube[0][1][0] = cube[4][1][0]
    cube[0][2][0] = cube[4][2][0]
    cube[4][2][0] = a
    cube[4][1][0] = b
    cube[4][0][0] = c
    return cube
def TurnOrange(cube,layer=0):
    #orange side
    TurnSide(cube,2)
    #TurnSide(cube,2)
    #TurnSide(cube,2)
    a = cube[3][0][2]
    b = cube[3][1][2]
    c = cube[3][2][2]
    cube[3][0][2] = cube[5][0][0]
    cube[3][1][2] = cube[5][0][1]
    cube[3][2][2] = cube[5][0][2]
    cube[5][0][2] = cube[1][0][0]
    cube[5][0][1] = cube[1][1][0]
    cube[5][0][0] = cube[1][2][0]
    cube[1][0][0] = cube[4][2][0]
    cube[1][1][0] = cube[4][2][1]
    cube[1][2][0] = cube[4][2][2]
    cube[4][2][2] = a
    cube[4][2][1] = b
    cube[4][2][0] = c
    return cube
def TurnBlue(cube,layer=0):
    #blue side
    TurnSide(cube,3)
    a = cube[0][0][2]
    b = cube[0][1][2]
    c = cube[0][2][2]
    cube[0][2][2] = cube[5][2][2]
    cube[0][1][2] = cube[5][1][2]
    cube[0][0][2] = cube[5][0][2]
    cube[5][2][2] = cube[2][0][0]
    cube[5][1][2] = cube[2][1][0]
    cube[5][0][2] = cube[2][2][0]
    cube[2][0][0] = cube[4][2][2]
    cube[2][1][0] = cube[4][1][2]
    cube[2][2][0] = cube[4][0][2]
    cube[4][0][2] = a
    cube[4][1][2] = b
    cube[4][2][2] = c
    return cube
def TurnYellow(cube,layer=0):
    #yellow side
    TurnSide(cube,4)
    a = cube[1][2][0]
    b = cube[1][2][1]
    c = cube[1][2][2]
    cube[1][2][2] = cube[0][2][2]
    cube[1][2][1] = cube[0][2][1]
    cube[1][2][0] = cube[0][2][0]
    cube[0][2][0] = cube[3][2][0]
    cube[0][2][1] = cube[3][2][1]
    cube[0][2][2] = cube[3][2][2]
    cube[3][2][0] = cube[2][2][0]
    cube[3][2][1] = cube[2][2][1]
    cube[3][2][2] = cube[2][2][2]
    cube[2][2][0] = a
    cube[2][2][1] = b
    cube[2][2][2] = c
    return cube
def TurnWhite(cube,layer=0):
    #white side
    TurnSide(cube,5)
    a = cube[1][0][0]
    b = cube[1][0][1]
    c = cube[1][0][2]
    cube[1][0][0] = cube[2][0][0]
    cube[1][0][1] = cube[2][0][1]
    cube[1][0][2] = cube[2][0][2]
    cube[2][0][0] = cube[3][0][0]
    cube[2][0][1] = cube[3][0][1]
    cube[2][0][2] = cube[3][0][2]
    cube[3][0][0] = cube[0][0][0]
    cube[3][0][1] = cube[0][0][1]
    cube[3][0][2] = cube[0][0][2]
    cube[0][0][0] = a
    cube[0][0][1] = b
    cube[0][0][2] = c
    return cube

def TurnSide(cube, index):
    #print(ColorNumberToText(index+1))
    a = cube[index][0][0]
    b = cube[index][0][1]
    cube[index][0][0] = cube[index][0][2]
    cube[index][0][1] = cube[index][1][2]
    cube[index][0][2] = cube[index][2][2]
    cube[index][1][2] = cube[index][2][1]
    cube[index][2][2] = cube[index][2][0]
    cube[index][2][1] = cube[index][1][0]
    cube[index][2][0] = a
    cube[index][1][0] = b


def PrintSide(cube,index):
    print(ColorNumberToText(index+1))
    for x in cube[index]:
        print(x)

def PrintCube(cube):
    for x in range(len(cube)):
        PrintSide(cube,x)

def Histogram(cube):
    k=[0,0,0,0,0,0]
    for x in cube:
        for y in x:
            for z in y:
                k[z-1]+=1
    return k
        
def TurnRedCounter(cube,layer=0):
    TurnRed(cube,layer)
    TurnRed(cube,layer)
    TurnRed(cube,layer)
    return cube
def TurnGreenCounter(cube,layer=0):
    TurnGreen(cube,layer)
    TurnGreen(cube,layer)
    TurnGreen(cube,layer)
    return cube
def TurnOrangeCounter(cube,layer=0):
    TurnOrange(cube,layer)
    TurnOrange(cube,layer)
    TurnOrange(cube,layer)
    return cube
def TurnBlueCounter(cube,layer=0):
    TurnBlue(cube,layer)
    TurnBlue(cube,layer)
    TurnBlue(cube,layer)
    return cube
def TurnYellowCounter(cube,layer=0):
    TurnYellow(cube,layer)
    TurnYellow(cube,layer)
    TurnYellow(cube,layer)
    return cube
def TurnWhiteCounter(cube,layer=0):
    TurnWhite(cube,layer)
    TurnWhite(cube,layer)
    TurnWhite(cube,layer)
    return cube
                

def RandomTest(n=20,spf=6,exclude=[]):
    l=BuildCubeSizeN()
    fa=[TurnRed,TurnGreen,TurnOrange,TurnBlue,TurnYellow,TurnWhite,
        TurnRedCounter,TurnGreenCounter,TurnOrangeCounter,
        TurnBlueCounter,TurnYellowCounter,TurnWhiteCounter]
    path=[]
    for x in range(n):
        if (spf > 6 or spf < 1): spf=6
        i=int(random.random()*spf)
        while(i in exclude):
            i=int(random.random()*spf)
            print('whoops!')
        path.append(i)
        s=''
    for x in path:
        s+=str(x) + ', '
        fa[x](l)
    print(s)
    path.reverse()
    s=''
    for x in path:
        s+=str(x+6) + ', '
        fa[x+6](l)
    print(s)
    PrintCube(l)
    klj=BuildCubeSizeN()
    print(l==klj)
    print(Histogram(l))
    return l

def BuildRandomCube(n=30,fill=True,spf=12,exclude=[]):
    l=BuildCubeSizeN()
    fa=[TurnRed,TurnGreen,TurnOrange,TurnBlue,TurnYellow,TurnWhite,
        TurnRedCounter,TurnGreenCounter,TurnOrangeCounter,
        TurnBlueCounter,TurnYellowCounter,TurnWhiteCounter]
    path=[]
    treepoop=int(random.random()*n)+1
    if(fill):treepoop=n
    last=-35
    for x in range(treepoop):
        if (spf > 12 or spf < 1): spf=12
        i=int(random.random()*spf)
        while(i in exclude or (i+6==last or i-6==last)):
            i=int(random.random()*spf)
            print('whoops!')
        path.append(i)
        last = i
    s=''    
    for x in path:
        s+=str(x) + ', '
        fa[x](l)
    print(s)
    PrintCube(l)
    print(Histogram(l))
    return l


def InsertIntoCubit(cubert,cubit):
    count=0
    for x in cubit:
        if(x[2]>=cubert[2]):
            cubit.insert(count,cubert)
            return
        count+=1
    cubit.append(cubert)
    return

def ScoreCube(cube,pathLength,gameCube,layerMatch=[]):
    weight = 0
    for x in range(len(cube)):
        for y in range(len(cube[x])):
            for z in range(len(cube[x][y])):
                if(cube[x][y][z]!=gameCube[x][y][z]):
                    weight+=1
    return weight*(pathLength+1)
    
def GenerateMoves(cubert,funcs,cubit,gameCube,layerMatch=[]):
    sc = ScoreCube
    if(layerMatch!=[]):sc=LayerScore
    for x in range(len(funcs)):
        #print('\t'+str(x))
        if(len(cubert[1])==0 or (cubert[1][-1]!=6+x and cubert[1][-1]!=x-6)):
            c=deepcopy(cubert)
            funcs[x](c[0])
            c[1].append(x)
            c[2]=sc(c[0],len(c[1]),gameCube,layerMatch)
            InsertIntoCubit(c,cubit)
            #add Hash to hash table

def LayerScore(cube,length,gameCube,layerMatch):
    weight=0
    for w in layerMatch:
        if(gameCube[w[0]][w[1]][w[2]]!=cube[w[0]][w[1]][w[2]]):
            weight+=1
    return  weight*(length+1)
        
def FSAstar(cube,debug=False):
    #stuff we need
    gameCube=BuildCubeSizeN()
    fa=[TurnRed,TurnGreen,TurnOrange,TurnBlue,TurnYellow,TurnWhite,
        TurnRedCounter,TurnGreenCounter,TurnOrangeCounter,
        TurnBlueCounter,TurnYellowCounter,TurnWhiteCounter]
    cubit = [] #[] -> [cube:0,Path:1,Score:2]
    cubert = [deepcopy(cube),[],ScoreCube(cube,1,gameCube)]
    #cubit.append(cubert)
    #gen Neighbors
    head = cubert
    count=0
    person = ''
    while(head[2]>0 and head[0]!=gameCube and person != 'x'):
        #print(count)
        if(count%100==0 and count > 0):
            print(count)
            print('Array Length: ' + str(len(cubit)))
        GenerateMoves(head,fa,cubit,gameCube)
        head=cubit.pop(0)
        count+=1
        if(debug):
            s=''
            for x in cubit:
                s+= str(x[2]) + ' -> ' + str(x[1])+ ', '
            print(str(head[2]) + ' -> ' + str(head[1]))
            PrintCube(head[0])
            print(s)
            person = input('x to exit')
    print('done')
    print('Loops: '+str(count))
    print('Length of list: ' + str(len(cubit)))
    print('path: ' + str(head[1]))
    PrintCube(head[0])

#todoInsertIntoCubit
#optimize
#1)Create hash table
#2)Do not insert unless shorter
#3)Binary search
#4)Find A way to make the above make sense
#Hueristic
#Find better hueristic for long paths
#1)weight corners different than middle of side
#   - which should have higher wieght?
#2)Force search in layers, not optimal, but preform in stages
#3)nueral nets
#4)many little hueristics, search for weights
#5)create testing, documentation and refactoring platform
#   -add timers
#
#ideas
#1) middle moves are neccessary(only for optimal solution?)
#2) need to find a way to deal with lots of potential overlap
#   -regarding 1 above
#   -regarding hash table from optimize
#3) have it find and memorize algorithms
#4) look, via data abstraction, for redundant permutations
#Rewrite as IDA*
#"Although the Fifteen Puzzle graph is not strictly a tree,
#the edge branching factor is only slightly greater than
#the node branching factor, and hence the
#iterative-deepening algorithm is still effective." ~R.E.Korf



#rewrite as IDA*
def FSIDAstar(cube,debug=False):
    #stuff we need
    gameCube=BuildCubeSizeN()
    fa=[TurnRed,TurnGreen,TurnOrange,TurnBlue,TurnYellow,TurnWhite,
        TurnRedCounter,TurnGreenCounter,TurnOrangeCounter,
        TurnBlueCounter,TurnYellowCounter,TurnWhiteCounter]
    cubit = [] #[] -> [cube:0,Path:1,Score:2]
    cubert = [deepcopy(cube),[],ScoreCube(cube,1,gameCube)]
    #cubit.append(cubert)
    #gen Neighbors
    head = cubert
    count=0
    person = ''
    while(head[2]>0 and head[0]!=gameCube and person != 'x'):
        #print(count)
        if(count%100==0 and count > 0):
            print(count)
            print('Array Length: ' + str(len(cubit)))
        GenerateMoves(head,fa,cubit,gameCube)
        head=cubit.pop(0)
        count+=1
        if(debug):
            s=''
            for x in cubit:
                s+= str(x[2]) + ' -> ' + str(x[1])+ ', '
            print(str(head[2]) + ' -> ' + str(head[1]))
            PrintCube(head[0])
            print(s)
            person = input('x to exit')
    print('done')
    print('Loops: '+str(count))
    print('Length of list: ' + str(len(cubit)))
    print('path: ' + str(head[1]))
    PrintCube(head[0])


# path              current search path (acts like a stack)
# node              current node (last node in current path)
# g                 the cost to reach current node
# f                 estimated cost of the cheapest path (root..node..goal)
# h(node)           estimated cost of the cheapest path (node..goal)
# cost(node, succ)  step cost function
# is_goal(node)     goal test
# successors(node)  node expanding function, expand nodes ordered by g + h(node)
# ida_star(root)    return either NOT_FOUND or a pair with the best path and its cost
# 
# procedure ida_star(root)
#   bound := h(root)
#   path := [root]
#   loop
#     t := search(path, 0, bound)
#     if t = FOUND then return (path, bound)
#     if t = NUL then return NOT_FOUND
#     bound := t
#   end loop
# end procedure
# 
# function search(path, g, bound)
#   node := path.last
#   f := g + h(node)
#   if f > bound then return f
#   if is_goal(node) then return FOUND
#   min := NUL
#   for succ in successors(node) do
#     if succ not in path then
#       path.push(succ)
#       t := search(path, g + cost(node, succ), bound)
#       if t = FOUND then return FOUND
#       if t < min then min := t
#       path.pop()
#     end if
#   end for
#   return min
# end function








#Layers
#
#
#
#
def FSLayersBad(cube,debug=False):
    #stuff we need
    gameCube=BuildCubeSizeN()
    fa=[TurnRed,TurnGreen,TurnOrange,TurnBlue,TurnYellow,TurnWhite,
        TurnRedCounter,TurnGreenCounter,TurnOrangeCounter,
        TurnBlueCounter,TurnYellowCounter,TurnWhiteCounter]
    cubit = [] #[] -> [cube:0,Path:1,Score:2]
    cubert = [deepcopy(cube),[],ScoreCube(cube,1,gameCube)]
    #cubit.append(cubert)
    #gen Neighbors
    head = cubert
    count=0
    layerCount=0 #sequence ends at 2
    person = ''
    layerMatch=set1()
    threshhold=100 #find better way to set
    while(head[2]>0 and head[0]!=gameCube and person != 'x'):
        if(count%1800==0 and count > 0):
            print('BOOM!!!!')
            StartOver(cubit, threshhold)
        if(layerCount < 1 and validateLayer(gameCube,head[0],layerMatch)):
            layerMatch=set2()
            layerCount+=1
            StartOver(cubit, threshhold)
        if(layerCount < 2 and validateLayer(gameCube,head[0],layerMatch)):
            layerMatch=[]
            layerCount+=1
            StartOver(cubit, threshhold)
            
        #print(count)
        if(count%100==0 and count > 0):
            threshhold=cubit[int(len(cubit)/14)][2]
            print(count)
            print('Array Length: ' + str(len(cubit)) + ', thresh: ' + str(threshhold))
            print('Layers Complete: ' + str(layerCount) + ', Head Score: ' + str(head[2]))
        GenerateMoves(head,fa,cubit,gameCube,layerMatch)
        head=cubit.pop(0)
        count+=1
        if(debug):
            s=''
            for x in cubit:
                s+= str(x[2]) + ' -> ' + str(x[1])+ ', '
            print(str(head[2]) + ' -> ' + str(head[1]))
            PrintCube(head[0])
            print(s)
            person = input('x to exit')
    print('done')
    print('Loops: '+str(count))
    print('Length of list: ' + str(len(cubit)))
    print('path: ' + str(head[1]))
    PrintCube(head[0])



def validateLayer(gc,cc,l):
    #if(l==gc)
    #l=[ [1,2,3],[2,3,1],[2,0,0] ... ]
    #l[whatever [always, 2, 3]]
    test=True
    for w in l:
        if(gc[w[0]][w[1]][w[2]]!=cc[w[0]][w[1]][w[2]]):
            test=False
            break
    return test

def set1():
    cube=[]
    cube.append([0,0,0])
    cube.append([0,0,0])
    cube.append([0,0,1])
    cube.append([0,0,2])
    cube.append([0,1,2])
    cube.append([0,2,2])
    cube.append([0,2,1])
    cube.append([0,2,0])
    cube.append([0,1,0])
    cube.append([2,0,2])
    cube.append([2,1,2])
    cube.append([2,2,2])
    cube.append([5,0,0])
    cube.append([5,1,0])
    cube.append([5,2,0])
    cube.append([0,0,0])
    cube.append([0,1,0])
    cube.append([0,2,0])
    cube.append([4,0,0])
    cube.append([4,1,0])
    cube.append([4,2,0])
    return cube



def set2():
    cube=[]
    cube.append([0,0,0])
    cube.append([0,0,0])
    cube.append([0,0,1])
    cube.append([0,0,2])
    cube.append([0,1,2])
    cube.append([0,2,2])
    cube.append([0,2,1])
    cube.append([0,2,0])
    cube.append([0,1,0])
    cube.append([2,0,2])
    cube.append([2,1,2])
    cube.append([2,2,2])
    cube.append([5,0,0])
    cube.append([5,1,0])
    cube.append([5,2,0])
    cube.append([0,0,0])
    cube.append([0,1,0])
    cube.append([0,2,0])
    cube.append([4,0,0])
    cube.append([4,1,0])
    cube.append([4,2,0])
    cube.append([4,1,0])
    cube.append([4,1,1])
    cube.append([4,1,2])
    cube.append([3,0,1])
    cube.append([3,1,1])
    cube.append([3,2,1])
    cube.append([5,1,0])
    cube.append([5,1,1])
    cube.append([5,1,2])
    cube.append([1,0,1])
    cube.append([1,1,1])
    cube.append([1,2,1])
    return cube


def StartOver(cubit, threshhold):
    count=0
    for x in cubit:
        if(x[2]>threshhold):cubit.pop(count)
        count+=1


#
#
def fsbad(cube,debug=False):
    #stuff we need
    gameCube=BuildNamedCube()
    fa=[TurnRed,TurnGreen,TurnOrange,TurnBlue,TurnYellow,TurnWhite,
        TurnRedCounter,TurnGreenCounter,TurnOrangeCounter,
        TurnBlueCounter,TurnYellowCounter,TurnWhiteCounter]
    cubit = [] #[] -> [cube:0,Path:1,Score:2]
    cubert = [deepcopy(cube),[],ScoreCube(cube,1,gameCube)]
    #cubit.append(cubert)
    #gen Neighbors
    head = cubert
    count=0
    layerCount=0 #sequence ends at 2
    person = ''
    layerMatch=set1()
    threshhold=100 #find better way to set
    matchedSideIndex=-1
    while(head[2]>0 and head[0]!=gameCube and person != 'x'):
        if(count%1000==0 and count > 0):
            print('BOOM!!!!')
            StartOver(cubit, threshhold)
        if(layerCount < 1 and validateSide(gameCube,head[0],layerMatch)>-1):
            apple=validateSide(gameCube,head[0],layerMatch)
            matchedSideIndex=apple
            if(apple in [0,2]):
                layerMatch=RedOrangeBelt()
            elif(apple in [1,3]):
                layerMatch=GreenBlueBelt()
            elif(apple in [4,5]):
                layerMatch=YellowWhiteBelt()
            layerCount+=1
            StartOver(cubit, threshhold)
        if(layerCount < 2 and layerCount > 0 and validateBelt(gameCube,head[0],layerMatch)):
            layerMatch=[]
            layerCount+=1
            StartOver(cubit, threshhold)
        #print(count)
        if(count%100==0 and count > 0):
            threshhold=cubit[int(len(cubit)/32)][2]
            print(count)
            print('Array Length: ' + str(len(cubit)) + ', thresh: ' + str(threshhold))
            print('Layers Complete: ' + str(layerCount) + ', Head Score: ' + str(head[2]))
        GenNameMoves(head,fa,cubit,gameCube,layerMatch,matchedSideIndex)
        head=cubit.pop(0)
        count+=1
        if(debug):
            s=''
            for x in cubit:
                s+= str(x[2]) + ' -> ' + str(x[1])+ ', '
            print(str(head[2]) + ' -> ' + str(head[1]))
            PrintCube(head[0])
            print(s)
            person = input('x to exit')
    print('done')
    print('Loops: '+str(count))
    print('Length of list: ' + str(len(cubit)))
    print('path: ' + str(head[1]))
    PrintNamedCube(head[0])



def validateBelt(gc,cc,l):
    #sp_whoTheHell!
    test=True
    for w in l:
        if(gc[w[0]][w[1]][w[2]]!=cc[w[0]][w[1]][w[2]]):
            test=False
            break
    return test

def validateSide(gc,cc,l):
    count=0
    for side in gc:
        if side == cc[count]:
            return count
        count+=1
    return -1


def RedOrangeBelt():
    cube=[]
    cube.append([4,1,0])
    cube.append([4,1,1])
    cube.append([4,1,2])
    cube.append([3,0,1])
    cube.append([3,1,1])
    cube.append([3,2,1])
    cube.append([5,1,0])
    cube.append([5,1,1])
    cube.append([5,1,2])
    cube.append([1,0,1])
    cube.append([1,1,1])
    cube.append([1,2,1])
    return cube

def YellowWhiteBelt():
    l=[[5,0,1],[5,1,1],[5,2,1],[0,0,1],[0,1,1],[0,2,1],
       [4,0,1],[4,1,1],[4,2,1],[2,0,1],[2,1,1],[2,2,1]]
    return l

def GreenBlueBelt():
    l=[[1,1,0],[1,1,1],[1,1,2],[0,1,0],[0,1,1],[0,1,2],
       [3,1,0],[3,1,1],[3,1,2],[2,1,0],[2,1,1],[2,1,2]]
    return l


#currently other peices only support size 3
def BuildNamedCube(n=3):
    #all cubes have six sides
    cube = []
    for x in range(6):
        y=x+1#is this neeed?
        currentSide = []
        for j in range(n):
            currentRow=[]
            for k in range(n): #all sides are cubes
                temp=(n*j) + ((n*n)*x) + k #0-53 or so
                #print(j)
                #print(k)
                #print(x)
                #print(temp)
                #print('-----')
                currentRow.append(temp)
            currentSide.append(currentRow)
        cube.append(currentSide)
    return cube


def PrintNamedSide(cube,index):
    print(ColorNumberToText(index+1))
    for x in cube[index]:
        temp=[]
        for y in x:
            temp.append(int(y/9)+1)
        print(temp)

def PrintNamedCube(cube):
    for x in range(len(cube)):
        PrintNamedSide(cube,x)


def BuildRandomNamedCube(n=30,fill=True,spf=12,exclude=[]):
    l=BuildNamedCube()
    fa=[TurnRed,TurnGreen,TurnOrange,TurnBlue,TurnYellow,TurnWhite,
        TurnRedCounter,TurnGreenCounter,TurnOrangeCounter,
        TurnBlueCounter,TurnYellowCounter,TurnWhiteCounter]
    path=[]
    treepoop=int(random.random()*n)+1
    if(fill):treepoop=n
    last=-35
    for x in range(treepoop):
        if (spf > 12 or spf < 1): spf=12
        i=int(random.random()*spf)
        while(i in exclude or (i+6==last or i-6==last)):
            i=int(random.random()*spf)
            print('whoops!')
        path.append(i)
        last = i
    s=''    
    for x in path:
        s+=str(x) + ', '
        fa[x](l)
    print(s)
    PrintNamedCube(l)
    return l


def ScoreLay(cube,pathLength,gameCube,layerMatch=[],matchedSideIndex=-1):
    weight=0
    for w in layerMatch:
        if(gameCube[w[0]][w[1]][w[2]]!=cube[w[0]][w[1]][w[2]]):
            weight+=1
    cx=0
    for w in gameCube[matchedSideIndex]:
        cy=0
        for y in w:
            if(y!=cube[matchedSideIndex][cx][cy]):
                weight+=2
            cy+=1
        cx+=1
    return  weight*(pathLength+1)
    
def GenNameMoves(cubert,funcs,cubit,gameCube,layerMatch=[],matchedSideIndex=-1):
    sc = ScoreNameCube
    if(layerMatch==[] and matchedSideIndex==-1):sc=SideScore
    elif(matchedSideIndex>-1 and matchedSideIndex<6):sc=ScoreLay
    for x in range(len(funcs)):
        #print('\t'+str(x))
        if(len(cubert[1])==0 or (cubert[1][-1]!=6+x and cubert[1][-1]!=x-6)):
            c=deepcopy(cubert)
            funcs[x](c[0])
            c[1].append(x)
            c[2]=sc(c[0],len(c[1]),gameCube,layerMatch, matchedSideIndex)
            InsertIntoCubit(c,cubit)
            #add Hash to hash table

def SideScore(cube,length,gameCube,layerMatch,matchedSideIndex=-1):
    weight = [0,0,0,0,0,0]
    for x in range(len(cube)):
        for y in range(len(cube[x])):
            for z in range(len(cube[x][y])):
                if(cube[x][y][z]!=gameCube[x][y][z]):
                    weight[x]+=1 * pow(2,weight[x])
    return sum(weight)*(pathLength+1) + 100


def ScoreNameCube(cube,pathLength,gameCube,layerMatch=[], matchedSideIndex=-1):
    weight = 0
    for x in range(len(cube)):
        wate=0
        for y in range(len(cube[x])):
            for z in range(len(cube[x][y])):
                if(cube[x][y][z]!=gameCube[x][y][z]):
                    wate+=1
        if(matchedSideIndex==x):wate=wate*2
        weight+=wate
    return weight*(pathLength+1)


#astar for named cubes
def NameStar(cube,debug=False):
    #stuff we need
    gameCube=BuildNamedCube()
    fa=[TurnRed,TurnGreen,TurnOrange,TurnBlue,TurnYellow,TurnWhite,
        TurnRedCounter,TurnGreenCounter,TurnOrangeCounter,
        TurnBlueCounter,TurnYellowCounter,TurnWhiteCounter]
    cubit = [] #[] -> [cube:0,Path:1,Score:2]
    cubert = [deepcopy(cube),[],ScoreNameCube(cube,1,gameCube)]
    #cubit.append(cubert)
    #gen Neighbors
    head = cubert
    count=0
    person = ''
    while(head[2]>0 and head[0]!=gameCube and person != 'x'):
        #print(count)
        if(count%100==0 and count > 0):
            print(count)
            print('Array Length: ' + str(len(cubit)))
        GeneMove(head,fa,cubit,gameCube)
        head=cubit.pop(0)
        count+=1
        if(debug):
            s=''
            for x in cubit:
                s+= str(x[2]) + ' -> ' + str(x[1])+ ', '
            print(str(head[2]) + ' -> ' + str(head[1]))
            PrintNamedCube(head[0])
            print(s)
            person = input('x to exit')
    print('done')
    print('Loops: '+str(count))
    print('Length of list: ' + str(len(cubit)))
    print('path: ' + str(head[1]))
    PrintNamedCube(head[0])



def GeneMove(cubert,funcs,cubit,gameCube,layerMatch=[]):
    sc = ScoreCube
    if(layerMatch!=[]):sc=LayerScore
    for x in range(len(funcs)):
        #print('\t'+str(x))
        if(len(cubert[1])==0 or (cubert[1][-1]!=6+x and cubert[1][-1]!=x-6)):
            c=deepcopy(cubert)
            funcs[x](c[0])
            c[1].append(x)
            c[2]=sc(c[0],len(c[1]),gameCube,layerMatch)
            InsertIntoCubit(c,cubit)
            #add Hash to hash table
