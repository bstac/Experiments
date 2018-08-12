import time

#driver skills from site
#line1 = ['b','c','e','h','k']       #,     '0']  #the last item means no shift scheduled for the early hours
#line2 = ['a','d','e','f','g','i']   #, '1']      #I am currently not using them until I can get a score without them
#line3 = ['d','f','h','j']           #,         '2']

#daysOff = ['ef','fg','agh','abhi','bcij','cdjk','dek','ef','fg','agh','abhi','bcij','cdjk','dek']
#prefEarly = ['g','h',' ',' ','f','b','g','ck','ah','d','j','ae','ae',' ']  #space blanks
#prefLate = ['b','j','fj',' ','k','i','a','i','b',' ',' ',' ',' ','cf']     #space blanks
#prefOff = ['chj','','dk','d','g','fgh','bh','abj','jk','ce','de','f','','agi']

##driver skills attempt 1
line1 = ['d','f','h','i','k', ' ']       
line2 = ['a','b','e','g','j','k', ' ']   
line3 = ['b','c','f','g', ' ']           

daysOff = ['ef','fg','agh','abhi','bcij','cdjk','dek','ef','fg','agh','abhi','bcij','cdjk','dek']
prefEarly = ['g',' ','b',' ',' ',' ','cgj','i',' ','f',' ','dk','ei','c']           #space blanks
prefLate = ['ch','e','ef','g','d','a',' ',' ','ch',' ',' ','a','bg','f']            #space blanks
prefOff = ['bdk','ij','c','e','g','fh','ahi','ach','bj','d','def','eg','','bg']

#from attempt 2
#line1 = ['b','c','f','h','k',' ']       
#line2 = ['a','d','e','g','j','k',' ']   
#line3 = ['a','f','g','i',' ']           

#daysOff = ['agh','abhi','bcij','cdjk','dek','ef','fg','agh','abhi','bcij','cdjk','dek','ef','fg']
#prefEarly = ['e',' ','ak','g',' ','bcdg',' ','ck','f',' ','a',' ','d',' ']                     #space blanks
#prefLate = [' ','egj',' ',' ',' ',' ',' ','bdi','j','dh',' ','ac','i','eik']                        #space blanks
#prefOff = ['dfjk','d','f','a','bghi','ai','cdik','e','k','g','g','bi','achj','bd']

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

def lateShift():
    #for generating al late shifts for each day
    return genDayByDay(genShifts(line1,line2,line3),daysOff)


def scoreBad(lisp):
    #this one scores but removes nothing
    #no breaks
    l=[]
    count = 0
    totes = 0
    while(count < 14):
        temp=[]
        maxi=0
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
            for ch in x:
                if(ch == ' '):
                    scor -= 20
                    pLost+= 20
            if(pLost<25):
                temp.append(dict(name=x,score=scor,lost=pLost,remove=0))
            if(scor>maxi):
                maxi=scor
        #temp.sort(key=lambda z: z['lost'])
        #not sure if i want the above line
        l.append(temp)
        totes+=maxi
        count+=1
    print('Max preference points: ' + str(totes)) #total prefereces pts possible
    return l
                        

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
                        boo = False #late night, early morn
                if(boo):
                    scor = x['score']+y['score']
                    #no points lost
                else:
                    scor = x['score']+y['score']-30
                    pLost=x['lost']+30
                if(pLost<25): #this does the job of removeLow()
                    temp.append(dict(name=x['name']+y['name'],score=scor,lost=pLost,remove=x['remove']+y['remove']))
        #temp.sort(key=lambda h: h['lost'])
        L.append(temp)
        count+=2
    if(danielBoo): #trail the tail
        L.append(lisp[jon])#for odd numbered lists of lists
    return L

                        

def scoreGoods(lisp):
    L=[] #scores a single list
    #scores based on what hasn't been done by the other functions
    #this version calculates for full schedules
    drivers = 'abcdefghijk'
    busDrN = len(drivers)
    for x in lisp:
        nm = x['name']
        sc = x['score'] + x['remove']
        pLost = x['lost'] - x['remove']
        from4 =0
        from3 =0
        from3G = 0
        longRest = [0]*busDrN
        late4 = [4]*busDrN
        late3 = [0]*busDrN
        count = 0
        while(count<len(nm) and len(nm)>6):
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
                        from3G+=5
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
        for y in late4:
            from4+=(abs(y)*8)
            sc-=(abs(y)*8)
        pLost+=from4+from3
        if(pLost<24):
            L.append(dict(name=nm, score=sc, lost=pLost, remove=(from4+from3)))
    L.sort(key=lambda h: h['score'])
    return L

def score5(lisp):
    L=[] #scores a single list
    #scores based on what hasn't been done by the other functions
    #this version calculates for full schedules
    drivers = 'abcdefghijk'
    busDrN = len(drivers)
    for x in lisp:
        nm = x['name']
        sc = x['score'] + x['remove']
        pLost = x['lost'] - x['remove']
        fr4 =0
        late4 = [4]*busDrN
        count = 0
        while(count<len(nm) and len(nm)>6):
            day = nm[count:(count+6)]
            for y in drivers:
                if y in day[3:]:
                    late4[drivers.index(y)]+=1
            count+=6
        for y in late4:
            from4=0
            if(y>4):
                from4=(y-4)*8
                sc-=from4
                pLost+=from4
                fr4+=from4
        if(pLost<24):
            L.append(dict(name=nm, score=sc, lost=pLost, remove=fr4))
    L.sort(key=lambda h: h['score'])
    return L

def score4(lisp):
    L=[] #scores a single list
    #scores based on what hasn't been done by the other functions
    #this version calculates for full schedules
    drivers = 'abcdefghijk'
    busDrN = len(drivers)
    for x in lisp:
        nm = x['name']
        sc = x['score'] + x['remove']
        pLost = x['lost'] 
        longRest = [0]*busDrN
        late3 = [0]*busDrN
        from3G= 0
        from3 = 0
        count = 0
        while(count<len(nm) and len(nm)>6):
            day = nm[count:(count+6)]
            for y in drivers:
                if y not in day:
                    longRest[drivers.index(y)]+=1
                else:
                    fmp = longRest[drivers.index(y)]
                    longRest[drivers.index(y)]=0
                    if(fmp>2):
                        sc+=5
                        from3G+=1
                if y not in day[3:]:
                    fmp = late3[drivers.index(y)]
                    late3[drivers.index(y)]=0
                    if(fmp>3):
                        from3+=10
                        sc-=10
                else:
                    late3[drivers.index(y)]+=1
            count+=1
        if(from3G<1):
            pLost+=3
        if(pLost<25):
            L.append(dict(name=nm, score=sc, lost=pLost, remove=from3 -(from3G*5)))
            #remove is for things that need to be removed before the next scoring
    L.sort(key=lambda h: h['score'])
    return L



#phase 1
def phase1(lisp):
    newGuy = []
    print('Analysis for phase 1: ')
    hardCode = 2000
    for l in lisp:
        leng = len(l)
        maxi = 0
        mini = 100
        tote = 0
        for item in l:
            temp = item['score']
            tote+=temp
            if(temp>maxi):
                maxi = temp
            if(temp<mini):
                mini = temp
        avg = tote/leng
        if(leng<hardCode):
            newGuy.append(l)
        else:
            l.sort(key=lambda h: h['score'])
            right = ((avg*leng)/(maxi-mini))
            #i might beable to bump up this 2000 to something alittle bigger if need be
            if(leng-right > hardCode):
                right = []
                for item in l:
                    tmp = (maxi-avg)/2
                    if(item['score'] >= (maxi-tmp)):
                        right.append(item)
                newGuy.append(right)
            else:
                newGuy.append(l[right:])
        print("Length: %7d,  Average Score: %3d,  Max: %3d ,  Min: %3d" % (leng,avg,maxi,mini))
    print('trimmed to')
    for l in newGuy:
        print(len(l))
    return newGuy

#phase 2
def phase2(lisp):
    shnew = []
    snard = len(lisp)
    csn = 1
    hardCode=2000
    newGuy=[]
    for l in lisp:
        leng = len(l)
        maxi = 0
        mini = 100
        tote = 0
        for item in l:
            temp = item['score']
            tote+=temp
            if(temp>maxi):
                maxi = temp
            if(temp<mini):
                mini = temp
        avg = tote/leng
        if(leng<hardCode):
            newGuy.append(l)
        else:
            l.sort(key=lambda h: h['score'])
            right = leng - hardCode
            newGuy.append(l[right:])
        print("Length: %7d,  Average Score: %3d,  Max: %3d ,  Min: %3d" % (leng,avg,maxi,mini))
    print('Removing excess')
    for l in newGuy:
        print(str(csn)+'/'+str(snard))
        print("%9d Items in this list" % (len(l)))
        a = score4(l)
        shnew.append(a)
        csn+=1
    for l in shnew:
        leng = len(l)
        maxi = 0
        mini = 1000
        tote = 0
        for item in l:
            temp = item['score']
            tote+=temp
            if(temp>maxi):
                maxi = temp
            if(temp<mini):
                mini = temp
            avg = tote/leng
        print("Length: %6d,  Average Score: %3d,  Max: %3d ,  Min: %3d" % (leng,avg,maxi,mini))
    return shnew


#phase 3
def phase3(lisp):
    shnew = []
    snard = len(lisp)
    csn = 1
    hardCode=2000
    newGuy=[]
    oldGuy=[]
    for l in lisp:
        leng = len(l)
        maxi = 0
        mini = 1000
        tote = 0
        for item in l:
            temp = item['score']
            tote+=temp
            if(temp>maxi):
                maxi = temp
            if(temp<mini):
                mini = temp
            avg = tote/leng
        print("Length: %6d,  Average Score: %3d,  Max: %3d ,  Min: %3d" % (leng,avg,maxi,mini))
    print('Removing excess')
    for l in lisp:
        print(str(csn)+'/'+str(snard))
        print("%9d Items in this list" % (len(l)))
        a = score5(l)
        oldGuy.append(a)
        csn+=1
    csn = 1
    for l in oldGuy:
        print(str(csn)+'/'+str(snard))
        print("%9d Items in this list" % (len(l)))
        a = score4(l)
        shnew.append(a)
        csn+=1
    for l in shnew:
        leng = len(l)
        maxi = 0
        mini = 100
        tote = 0
        for item in l:
            temp = item['score']
            tote+=temp
            if(temp>maxi):
                maxi = temp
            if(temp<mini):
                mini = temp
        avg = tote/leng
        if(leng<hardCode):
            newGuy.append(l)
        else:
            l.sort(key=lambda h: h['score'])
            right = leng - hardCode
            newGuy.append(l[right:])
        print("Length: %6d,  Average Score: %3d,  Max: %3d ,  Min: %3d" % (leng,avg,maxi,mini))
    return newGuy

def prype(x):
    #print the dict struct we are using
    print(x['name'])
    print(x['lost'])
    print(x['score'])
    print('----- ----- ----- ----- ----- ----- ----\n')
        
    
def runn():
    start = time.clock()
    print('Phase 1 and combining')
    x = combineRate(scoreBad(monkeyButt()))
    a = phase1(x)
    del x
    print('Seconds: ' + str(int(time.clock()-start)))
    timer = time.clock()
    print('Phase 2 Combining')
    b = combineRate(a)
    print('Seconds: ' + str(int(time.clock()-timer)))
    print('Phase 2 analysis and removal')
    timer = time.clock()
    a = phase2(b)
    del b
    print('Seconds: ' + str(int(time.clock()-timer)))
    print('Phase 3 combining')
    timer = time.clock()
    x = combineRate(a)
    print('Seconds: ' + str(int(time.clock()-timer)))
    print('Phase 3 analysis')
    b = phase3(x)
    timer = time.clock()
    print('Seconds: ' + str(int(time.clock()-timer)))
    print('Total Time in Minutes: ' + str(int(time.clock()- start)/60))
    return b
    
    
    
