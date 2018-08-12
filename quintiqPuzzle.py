#driver skills from site
line1 = ['b','c','e','h','k']       #,     '0']  #the last item means no shift scheduled for the early hours
line2 = ['a','d','e','f','g','i']   #, '1']      #I am currently not using them until I can get a score without them
line3 = ['d','f','h','j']           #,         '2']

daysOff = ['ef','fg','agh','abhi','bcij','cdjk','dek','ef','fg','agh','abhi','bcij','cdjk','dek']
prefEarly = ['g','h',' ',' ','f','b','g','ck','ah','d','j','ae','ae',' ']  #space blanks
prefLate = ['b','j','fj',' ','k','i','a','i','b',' ',' ',' ',' ','cf']  #space blanks
prefOff = ['chj','','dk','d','g','fgh','bh','abj','jk','ce','de','f','','agi']

#driver skills attempt 1
#line1 = ['d','f','h','i','k']       
#line2 = ['a','b','e','g','j','k']   
#line3 = ['b','c','f','g']           

#daysOff = ['ef','fg','agh','abhi','bcij','cdjk','dek','ef','fg','agh','abhi','bcij','cdjk','dek']
#prefEarly = ['g',' ','b',' ',' ',' ','cgj','i',' ','f',' ','dk','ei','c']                     #space blanks
#prefLate = ['ch','e','ef','g','d','a',' ',' ','ch',' ',' ','a','bg','f']                        #space blanks
#prefOff = ['bdk','ij','c','e','g','fh','ahi','ach','bj','d','def','eg','','bg']

def genShifts(l1,l2,l3):
    #early and late,
    # only no doubles for a single shift
    l=[]
    #count = 0;
    for x in l1:
        for y in l2:
            if(x != y):
                for z in l3:
                    #count+=1
                    if((x!=z)and(y!=z)):
                        s=x+y+z
                        l.append(s)
    return l


def genDays(L):
    #all days with no doubles,
    #assuming you have used genShifts()
    #to clearify, a day is a possible early
    #and late shift config, no doubles
    L2 = L
    l = []
    for x in L:
        for y in L2:
            boo = True
            for z in x:
                if z in y:
                   boo = False
                   break
            if(boo):
                l.append(x+y)

    return l

def genDayByDay(days,off):
    l = []
    for st in off:
        temp = []
        for x in days:
            boo = True
            for ch in st:
                if ch in x:
                    boo = False
                    break
            if(boo):
                temp.append(x)
        l.append(temp)
    return l

def monkeyButt():
    #test the above functions, set a list equal to it
    return genDayByDay(genDays(genShifts(line1,line2,line3)),daysOff)

def removeBad(lisp):
    l=[] #score and remove the bad ones
    count = 0;
    while(count < 14):
        temp=[]
        temp2=[]
        for x in lisp[count]:
            boo=False
            scor = 0 #note: break statements create false low scores
            for y in prefEarly[count]:
                if y in x[:3]:
                    boo=True
                    scor+=3
                    break
            for y in prefLate[count]:
                if y in x[3:]:
                    boo=True
                    scor+=3
                    break
            for y in prefOff[count]:
                if y not in x:
                    boo=True
                    scor+=4
                    break
            if(boo):
                temp.append(dict(name=x,score=scor))
            temp2.append(dict(name=x,score=scor))
        temp.sort(key=lambda z: z['score'])
        temp2.sort(key=lambda z: z['score'])
        if(len(temp)<100):
            l.append(temp2)
        else:
            l.append(temp)
        count+=1
    return l

def scoreBad(lisp):
    #this one scores but removes nothing
    #no breaks
    l=[]
    count = 0;
    while(count < 14):
        temp=[]
        for x in lisp[count]:
            scor = 0
            pLost = 0
            for y in prefEarly[count]:
                if y in x[:3]:
                    scor+=3
                else:
                    pLost+=3
            for y in prefLate[count]:
                if y in x[3:]:
                    scor+=3
                else:
                    pLost+=3
            for y in prefOff[count]:
                if y not in x:
                    scor+=4
                else:
                    pLost+=4
            temp.append(dict(name=x,score=scor lost=pLost))
        #temp.sort(key=lambda z: z['lost'])
        #not sure if i want the above line
        l.append(temp)
        count+=1
    return l
                        
def buildBridge(lisp):
    count = 0;
    danielBoo=False
    if(len(lisp)%2!=0):
        danielBoo=True
    jon = len(lisp)-1
    L = []
    while(count < jon):
        temp=[]
        for x in lisp[count]:
            leng = len(x['name'])-3
            for y in lisp[count+1]:
                boo = True
                for z in y['name'][:3]:
                    if z in x['name'][leng:]:
                        boo = False
                if(boo):
                    scor = x['score']+y['score']
                    nam = x['name']+y['name']
                    temp.append(dict(name=nam,score=scor))
        temp.sort(key=lambda h: h['score'])
        L.append(temp)
        count+=2
    if(danielBoo):
        L.append(lisp[jon])
    return L

def combineRate(lisp):
    #similar to buildBridge()
    #does not remove anything
    #scores late followed by early shifts
    count = 0;
    danielBoo=False
    if(len(lisp)%2!=0):
        danielBoo=True
    jon = len(lisp)-1
    L = []
    while(count < jon):
        temp=[]
        for x in lisp[count]:
            leng = len(x['name'])-3
            for y in lisp[count+1]:
                scor = 0
                pLost = 0
                boo = True
                for z in y['name'][:3]:
                    if z in x['name'][leng:]:
                        boo = False
                if(boo):
                    scor = x['score']+y['score']
                    #no points lost
                else:
                    scor = x['score']+y['score']-30
                    pLost=x['lost']+30
                nam = x['name']+y['name']
                if(pLost<32): #this if does the job of removeLow()
                    temp.append(dict(name=nam,score=scor,lost=pLost))
        #temp.sort(key=lambda h: h['lost'])
        L.append(temp)
        count+=2
    if(danielBoo): #trail the tail
        L.append(lisp[jon])#for odd numbered lists of lists
    return L




def removeLow(lisp,n):
    L=[]
    for x in lisp:
        temp=[]
        if(len(x)>n):
            size = len(x)-n
            temp=x[size:]
        else:
            temp = x
        L.append(temp)
    return L

                        

def scoreGoods(lisp):
    L=[]
    drivers = 'abcdefghijk'
    busDrN = len(drivers)
    for x in lisp:
        nm = x['name']
        sc = x['score']
        respParty = []
        from4 =0
        from3 =0
        longRest = [0]*busDrN
        late4 = [4]*busDrN
        late3 = [0]*busDrN
        count = 0
        while(count<len(nm)):
            day = nm[count:(count+6)]
            for y in drivers:
                if y not in day:
                    longRest[drivers.index(y)]+=1
                else:
                    fmp = longRest[drivers.index(y)]
                    longRest[drivers.index(y)]=0
                    if(fmp>2):
                        #sc+=(5*(fmp-2))
                        sc+=5
                if y not in day[3:]:
                    fmp = late3[drivers.index(y)]
                    late3[drivers.index(y)]=0
                    if(fmp>3):
                        #sc-=(10*(fmp-3))
                        from3+=10
                        sc-=10
                else:
                    late4[drivers.index(y)]-=1
                    late3[drivers.index(y)]+=1
            count+=6
        cnt=0;
        for y in late4:
            from4+=(abs(y)*8)
            sc-=(abs(y)*8)
            if(y!=0):
                respParty.append([drivers[cnt],y])
            cnt+=1
        if(sc>60 or (sc+from4+from3)>133):
            L.append(dict(hype=(sc+from4+from3), name=nm, score=sc, f3=from3,f4=from4,resp=respParty))
    #L.sort(key=lambda h: h['score'])
    L.sort(key=lambda h: h['hype'])
    return L


#test 3-5 are essentially scattershots that group in different areas of a state space
#they are inherently bad.
#the methods used at this time have shown to be incomplete explorations and therefore
#do not return solutions that attain more than about 50% of points, the most I have seen is about 80/156.
#I have the tools minus one or two functions to implement a better, more guided solution.
#i will need to write a new version of scoreGoods() and removeLow()
#new print functions miht be usefull
#possibly new dictionary structure for new analysis concepts
#if anything looses more than 31 points, it can be removed because it cannot contribute
# to an 80% or above solution
def test5():
    a = monkeyButt()
    e = scoreBad(a)
    c = removeLow(buildBridge(e[3:7]),1000)#4->2
    d = removeLow(buildBridge(e[9:]),1000)#5->3
    a = removeLow(buildBridge(c),1200)#2->1
    b = removeLow(buildBridge(d),1200)#3->2
    c = removeLow(buildBridge(e[:3]+a+e[7:9]+b),1200)#8->4
    a = removeLow(buildBridge(c),1200)#4->2
    b = buildBridge(a) #2->1
    a = scoreGoods(b[0])
    return a

def test4():
    a = monkeyButt()
    b = scoreBad(a)
    c = removeLow(buildBridge(b[3:7]),1000)
    d = removeLow(buildBridge(b[9:]),1000)
    a = removeLow(buildBridge(b[:3]+c+b[7:9]+d),1000)
    b = removeLow(buildBridge(a),1200)
    a = removeLow(buildBridge(b),1200)
    b = buildBridge(a)
    a = scoreGoods(b[0])
    return a


def test3():
    a = test2(test1())
    b = test2(a)
    a = buildBridge(b)
    b = a[0]
    a=scoreGoods(b)
    return a

#test 1 and 2 are for aiding manual analysis
def test1():
    a = monkeyButt()
    b = removeBad(a)
    c = buildBridge(b)
    d = removeLow(c,900)
    return d

def test2(a):
    b = buildBridge(a)
    c = removeLow(b,1200)
    return c
    
def printHype(x):
    print(x['name'])
    print(x['hype'])
    print(x['score'])
    print('f3: '+str(x['f3']))
    print('f4: '+str(x['f4']))
    print(x['resp'])
    print('----- ----- ----- ----- ----- ----- ----\n')
        
    
                
    
    
