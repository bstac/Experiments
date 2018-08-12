#farkle rules
#MAIN
#roll
#count 1's
#count 5's
#find straight
#find 4 of a kind
#find 5 of a kind
#find 6 of a kind
#
#
#
#
#
#
#

def toBase(g,b):
    l = ''
    while( g > 0):
       l=str(g%b)+l
       g/=b
    return l

def fromBase(g,b):
    l = str(g)
    cnt = 0
    g=0
    cnt = 0
    for x in l:
        print(x)
        y = (len(l)-1)-cnt
        g+=pow(b,y)*int(x)
        cnt += 1
    return g



def lastLet(word):
    return word[len(word)-1]

def genPerms(s):
    return perms('',s)

def noDups(s):
    wDups = genPermList(s)
    wOutDups = remDups(wDups)
    wOutDups.sort()
    return wOutDups
    
def perms(buildPerm,togoString):
    togoLen = len(togoString)
    if togoLen == 0:
        print buildPerm
    else:
        for i in range(togoLen):
            perms(buildPerm + togoString[i],togoString[:i] + togoString[i+1:])
 
def genPermList(s):
    L =[]
    return permLis('',s,L)
 
def permLis(buildPerm,togoString,L):
    togoLen = len(togoString)
    if togoLen == 0:
        L.append(buildPerm)
    else:
        for i in range(togoLen):
            permLis(buildPerm + togoString[i],togoString[:i] + togoString[i+1:],L)
    return L

def remDups(L):
    newL = []
    for item in L:
        if not(item in newL):
            newL.append(item)
    return newL

def readAfile(fName):
    f = open(fName,'r')
    return f.read()
 
def rwAfile(fNameIn,fNameOut):
    f_in = open(fNameIn,'r')
    f_out = open(fNameOut,'w')
    contents = f_in.read()
    f_out.write(contents)
    return 'Done!'
                           
                                                                                                                  
def genWordList(fName):
    wordString = readAfile(fName)
    wsLen = len(wordString)
    words = []
    indx = 0
    aWord = ''
    while indx < wsLen:
        aLet = wordString[indx]
        if aLet != ' ' and aLet != '\n':
            aWord += aLet
        else:
            aWord = aWord.lower()
            words.append(aWord)
            aWord = ''
        indx += 1
    words.append(aWord)
    return words
                                     
def zSuf(fName):
    w4=genWordList(fName)
    zWords=[]
    count=0
    for word in w4:
        if word[len(word)-1]=='z':
            count += 1
            zWords.append(word)
    print count
    return zWords

def bigZ(fOne,fTwo):
    w4=zSuf(fOne)
    w5=zSuf(fTwo)
    w=w4+w5
    w.sort()
    return w

