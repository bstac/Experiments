from fractions import Fraction
import math
import random
import pickle

def redPF(f,h):
    if(type(f)!=list or type(h)!=list or len(f)!=len(h)):
        return('Garbage! DANGER ZONE')
    a=1
    cnt=0
    while(cnt<len(f)):
        a*=(pow(h[cnt],f[cnt]))
        cnt+=1
    return a

def mulPF(a,b):
    t=[]
    if(len(a[0])>len(b[0])):
        t=a
        a=b
        b=t
    f = a[0]
    h = b[0]
    if(type(f)!=list or type(h)!=list):
        return('Garbage! DANGER ZONE')
    l=[]
    cnt=0
    while(cnt<len(f)):
        l.append(h[cnt]+f[cnt])
        cnt+=1
    t = l+h[len(l):len(h)]
    return [t,b[1]]

def divPF(a,b):
    if(type(a)!=list or type(b)!=list):
        return('Garbage! DANGER ZONE')
    f = a[0]
    h = b[0]
    if(type(f)!=list or type(h)!=list):
        return('Garbage! DANGER ZONE')
    #at this point we know we have all lists
    c=[]#bogey
    num=1
    if(len(f)>len(h)):
        c=a
        num = 1
    else:
        c=b
        num = -1
    #f/h
    t=[]
    l=[]
    cnt=0
    co=min([len(f),len(h)])
    while(cnt<co):
        l.append(f[cnt]-h[cnt])
        cnt+=1
    t = l
    for x in c[0][len(l):len(c[1])]:
        t.append(num*x)
    return [t,c[1]]


def pFact(n):
    #if given a list, returns list of ordered pairs
    #otherwise,gives an ordered pair
    #maybe should be primes to sqrt(n), not suremath.sqrt(n)
    l = primes(n)
    ret = []
    if(type(n)==list):
        for x in n:
            ret.append(pFact(x))
        return ret
    if n in l:
        for x in l[:len(l)-1]:ret.append(0)
        ret.append(1)
        return [ret,l]
    for x in l:
        ret.append(0)
        if n%x==0:
            ret[-1]+=1
            ex=x*x
            while(n%ex==0):
                ret[-1]+=1
                ex=ex*x
    return [ret,l]
            
    

def primes(n):
    if(type(n)==list):n=max(n)
    if(n < 2):
        return []
    lp = [2]
    cnt = 3
    while(cnt<=n):
        trip = True
        for x in lp:
            if(x*x>n):
                break
            if(cnt%x==0):
                trip = False
                break
        if(trip):
            lp.append(cnt)
        cnt+=2
    return lp

def pCont(n,l):
    lp = l
    cnt = l[-1]+2
    #+2 is needed, dont remove
    if(n < cnt):
        return primes(n)
    while(cnt<=n):
        trip = True
        for x in lp:
            if(x*x>n):
                break
            if(cnt%x==0):
                trip = False
                break
        if(trip):
            lp.append(cnt)
        cnt+=2
        #could this function be messed with
    return lp
        
def delta(l):
    a = []
    cnt = 0
    while(cnt<len(l)-1):
        a.append(l[cnt+1]-l[cnt])
        cnt+=1
    return a

def fact(n):
    g = 1
    for x in range(n):
        g*=x+1
    if(n==0):
        g=1
    return g


#misc functions that really dont do anything that cool
def ei(l):
    e=0
    for x in l:
        e+=1.0/x
    return e

def ea(l):
    e=0
    for x in l:
        e+=1.0/fact(x)
    return e

def fib(n):
    c = 1
    a = 0
    l=[]
    for x in range(n):
        tm = a
        a+=c
        c = tm
        l.append(a+c)
    return l

def binP(n):
    ret = []
    if(type(n)==list):
        n=max(n)
    l = primes(n)
    for x in l:ret.append(bin(x))
    return ret

# pfact runner for real numbers

def pfReal(n):
    g = Fraction(str(n))
    a = g.numerator
    b = g.denominator
    #print(str(a) + " " + str(b) + " "+str(g))
    ret = divPF(pFact(a),pFact(b))
    return ret

def rFile(fName):
    f = open(fName,'r')
    l = f.read()
    p=[]
    tm=''
    for x in l:
        if(x == ','):
            p.append(int(tm))
            tm=''
            continue
        if(x == ' '):
            continue
        else:
            tm+=x  
    return p

def wFile(ls,fNameOut):
    f_out = open(fNameOut,'w')
    f_out.write(str(ls)[1:-1])
    return 'Done!'


def stoDB(db,fn):
    fn = open(fn+'.pkl','wb')
    pickle.dump(db,fn)
    fn.close
                                                                                                                  
def getDB(fn):
    dbFile = open(fn+'.pkl','rb')
    db = pickle.load(dbFile)
    dbFile.close()
    return db
##############################################
SecretLordFarquad = rFile('p.txt')
SecretLordForhead = 1.7

def big():
    SecretLordFarquad = rFile('p2.txt')


def pf(n):
    #if given a list, returns list of ordered pairs
    #otherwise,gives an ordered pair
    #maybe should be primes to sqrt(n), not suremath.sqrt(n)
    l = []
    for g in range(len(SecretLordFarquad)):
        if(SecretLordFarquad[g]>n):
            l=SecretLordFarquad[:g]
            break
    ret = []
    if(type(n)==list):
        for x in n:
            ret.append(pFact(x))
        return ret
    if n in l:
        for x in l[:len(l)-1]:ret.append(0)
        ret.append(1)
        return [ret,l]
    for x in l:
        ret.append(0)
        if n%x==0:
            ret[-1]+=1
            ex=x*x
            while(n%ex==0):
                ret[-1]+=1
                ex=ex*x
    return [ret,l]

def pr(n):
    g = Fraction(str(n))
    a = g.numerator
    b = g.denominator
    #print(str(a) + " " + str(b) + " "+str(g))
    ret = divPF(pf(a),pf(b))
    return ret

def red(h):
    if(type(h[0])!=list or type(h[1])!=list or len(h[0])!=len(h[1])):
        return('Garbage! DANGER ZONE')
    a=1
    b=1
    cnt=0
    while(cnt<len(h[0])):
        if(h[0][cnt]>0):
            a*=(pow(h[1][cnt],h[0][cnt]))
        else:
            b*=(pow(h[1][cnt],(-1)*h[0][cnt]))
        cnt+=1
    return a/b

def shift(n,b):
    d = round(pow(n,b),2)
    print(d)
    print('suspect')
    return pr(d)

def amp(l):
    #num movemnts
    #a = random.randint(0,len(l[0])-1)
    #currently goes both ways, ha
    if(len(l[0])>2):
        l[0][0] -= 1
        l[0][1] += 2
    else:
        print(l)
    return l

def pam(l):
    #num movemnts
    #a = random.randint(0,len(l[0])-1)
    #currently goes both ways, ha
    if(len(l[0])>2):
        l[0][0] += 2
        l[0][1] -= 4
    else:
        print(l)
    return l

def notZ(l):
    c = 0
    cnt = 1 #+1, to len, not index
    ret = [] #this takes the whole primeFact
    for x in l[0]:
        if(x!=0):
            c = cnt #c is last non zero
        cnt+=1
    return([l[0][:c],l[1][:c]])

def test(a,b):
    base = SecretLordForhead
    g = a+b
    h = a*b
    bert = round(red(notZ(amp(shift(a,base)))),2)
    ernie = round(red(notZ(amp(shift(b,base)))),2)
    print(bert)
    print(ernie)
    j = round(bert*ernie,2)
    print('j= ' + str(j))
    #k = pow(bert,ernie)
    #m = pow(ernie,bert)
    qwe = math.log(red(notZ(pam(pr(j)))),base)
    #qwa = math.log(red(notZ(pam(pr(k)))),base)
    #qwi = math.log(red(notZ(pam(pr(m)))),base)
    print(str(g)+ ' = ' + str(qwe))
    #print(str(h)+ ' = ' + str(qwa)+ ' = ' + str(qwi))
        
     




     
