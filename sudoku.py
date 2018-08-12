global_list = []
global_length_const = 9
Potential_Round1 = [[],[],[],[],[],[],[],[],[]]
Potential_Round2_help = [[],[],[],[],[],[],[],[],[]]
grids_start = []

p_set = [[0,0,0,0,9,3,0,6,0],
         [0,0,0,6,2,8,0,0,0],
         [0,0,0,1,4,0,0,5,0],
         [0,3,0,0,5,0,0,4,0],
         [0,1,0,8,0,2,0,7,0],
         [0,9,0,0,7,0,0,6,0],
         [0,8,0,0,1,7,0,0,0],
         [0,0,0,5,9,3,0,0,0],
         [0,3,0,4,2,0,0,0,0]]

s_set = [[0,8,0,3,0,4,0,6,0],
         [4,0,7,0,0,0,0,0,0],
         [0,9,0,8,0,2,0,7,0],
         [6,0,0,0,0,0,8,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,9],
         [0,1,0,2,0,5,0,3,0],
         [0,0,0,0,0,0,8,0,9],
         [0,3,0,1,0,7,0,5,0]]


def reset(global_list,global_length_const,Potential_Round1,Potential_Round2_help,grids_start):
    global_list = []
    global_length_const = 9
    Potential_Round1 = [[],[],[],[],[],[],[],[],[]]
    Potential_Round2_help = [[],[],[],[],[],[],[],[],[]]
    grids_start = []
    
def create(l):
    ll = [1,2,3,4,5,6,7,8,9]
    if len(l) < global_length_const:
        for x in ll:
            if x not in l:
                xx = l + [x]
                create(xx)
    else:
        global_list.append(l)



def round1(problem_set):
    cnt=0
    #0 means empty
    #anything else marks
    for box in problem_set:
        for matchee in global_list:
            count = 0
            match=True
            for x in box:
                if (matchee[count] != x and x !=0):
                    match = False
                count+=1
            if match == True:
                Potential_Round1[cnt].append([matchee[:3],matchee[3:6],matchee[6:]])
        cnt+=1



def create_grids_start():
    grids_start = [Potential_Round1[:3],Potential_Round1[3:6],Potential_Round1[6:]]

#for the set of potentials after round 1
#Start with the first two, get rid of anything that cannot go together
#and register the rest as potentials

#grids [ rows of thre boxes [ individual boxes [  rows [1,2,3], ... [],  [] ], ... [],  [] ]  ,  []  ,  []   ]
#grid[1][2][1][0]
#row of boxes number 1,
#individual box within number 2,
#box internal row number 1
#item 0

def combine(xx,yy):
    ret = []
    for x in xx:
        for y in yy:
            h = True
            for t in x[0]:
                if t in y[0]:
                    h = False
                    break
            for t in x[1]:
                if t in y[1]:
                    h = False
                    break
            for t in x[2]:
                if t in y[2]:
                    h = False
                    break
            if(h==True):ret.append([x[0]+y[0],x[1]+y[1],x[2]+y[2]])
    return ret



def r2list(pset):
    l = []
    #indx = [0,1,2,3,4,5,6,7,8]
    indx = [0,1,2]
    for i in indx:
        cnt = 0
        for x in pset:
            Potential_Round2_help[(cnt%3)+(i*3)].append(x[i])
            Potential_Round2_help[(cnt%3)+(i*3)].append(x[i+3])
            Potential_Round2_help[(cnt%3)+(i*3)].append(x[i+6])
            cnt+=1
    for x in Potential_Round2_help:
        l.append([r2(x[3:6],x[6:]),r2(x[:3],x[6:]),r2(x[:3],x[3:6])])
    return l
#return Potential_Round2_help


def r2(l1,l2):
    l=[]
    for x in l1:
        if x != 0 and x not in l:l.append(x)
    for x in l2:
        if x != 0 and x not in l:l.append(x)
    return l

def remove(r1, pset):
    l= [[],[],[],[],[],[],[],[],[]]
    r2_help = r2list(pset)
    cnt = 0
    for box_set in r1:
        for box in box_set:
            h=True
            indx=[0,1,2]
            for id in indx:
                for row in box:
                    #if(row[id] in r2_help[cnt][id]):h=False
                    if(row[id] in r2_help[(3*id)+(cnt%3)][(cnt//3)]):h=False
            if(h):l[cnt].append(box)
        cnt+=1
    return l



def vert_combine(l1,l2):
    return_me = []
    rows = [0,1,2,3,4,5,6,7,8]
    for x in l1:
        for y in l2:
            h = True
            for row in rows:
                temp = []
                for d in x:
                    temp.append(d[row])
                if y[0][row] in temp : h = False
                if y[1][row] in temp : h = False
                if y[2][row] in temp : h = False
            if(h):return_me.append(x+y)
    return return_me

"""
def remove_diag(shadowset,g,d,a):
    l=[[],[],[]]
    for box in g:
        if(    (box[0][0]==shadowset[0][0] or shadowset[0][0] == 0)
           and (box[0][4]==shadowset[1][1] or shadowset[1][1] == 0)
           and (box[0][8]==shadowset[2][2] or shadowset[2][2] == 0)
           and (box[2][2]==shadowset[0][8] or shadowset[0][0] == 0)
           and (box[2][4]==shadowset[1][7] or shadowset[0][0] == 0)
           and (box[2][6]==shadowset[2][6] or shadowset[0][0] == 0)):
            l[0].append(box)
    for box in d:
        if(    (box[1][0]==shadowset[3][3] or shadowset[0][0] == 0)
           and (box[1][2]==shadowset[3][5] or shadowset[0][0] == 0)
           and (box[1][4]==shadowset[4][4] or shadowset[0][0] == 0)
           and (box[1][6]==shadowset[5][3] or shadowset[0][0] == 0)
           and (box[1][8]==shadowset[5][5] or shadowset[0][0] == 0)):
            l[1].append(box)
    for box in a:
        if(    (box[2][0]==shadowset[6][6] or shadowset[0][0] == 0)
           and (box[2][4]==shadowset[7][7] or shadowset[0][0] == 0)
           and (box[2][8]==shadowset[8][8] or shadowset[0][0] == 0)
           and (box[0][2]==shadowset[6][2] or shadowset[0][0] == 0)
           and (box[0][4]==shadowset[7][1] or shadowset[0][0] == 0)
           and (box[0][6]==shadowset[8][0] or shadowset[0][0] == 0)):
            l[2].append(box)
    return l
"""

def run(problem_set,diag=False):
    create([])
    print('create done!')
    round1(problem_set)
    print('round1 done')
    p = remove(Potential_Round1, problem_set)
    print('remove done')
    for x in p:
        print(len(x))
    print('combine rows')
    #p = Potential_Round1
    h = combine(p[0],p[1])
    g = combine(h,p[2])
    print('top row done')
    f = combine(p[3],p[4])
    d = combine(f,p[5])
    print('middle row done')
    s = combine(p[6],p[7])
    a = combine(s,p[8])
    print('bottom row done')
    qw = vert_combine(g,d)
    print('one vertical combine done..')
    qe=[]
    print('combining last vertical row')
    if(diag):
        #wg = Diag(qw)
        eq = vert_combine(qw,a)
        qe = Diag(eq)
    else:
        qe = vert_combine(qw,a)
    print('Done!')
    return qe


def Diag(eq):
    l=[]
    for pot in eq:
        l1 = [pot[0][0],pot[1][1],pot[2][2],pot[3][3],pot[4][4],pot[5][5],pot[6][6],pot[7][7],pot[8][8]]
        l2 = [pot[0][8],pot[1][7],pot[2][6],pot[3][5],pot[4][4],pot[5][3],pot[6][2],pot[7][1],pot[8][0]]
        l3 = [1,2,3,4,5,6,7,8,9]
        l1_test = True
        l2_test = True
        for xx in l3:
            if(l1.count(xx)!=1):l1_test=False
            if(l2.count(xx)!=1):l2_test=False
        if(l1_test and l2_test): l.append(pot)
    return l
    
