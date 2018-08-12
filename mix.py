import wave
import audioop
import random
import time
from time import time

#set up handyRandy
#the random number generator
random.seed(time())
handyRandy = random.random
#generate song structure


def overAny():
    x = handyRandy()
    x*=16
    x+=1
    x=int(x)
    if(x<=8):
        return wave.open("over/any/" + str(x) + ".wav")
    else:
        return 'no'
    
def Brandon():
    x = handyRandy()
    x*=14
    x+=1
    x=int(x)
    return wave.open("over/Brandon/E/" + str(x) + ".wav")
    

def E():
    x = handyRandy()
    y = handyRandy()
    x*=20
    x+=1
    x = int(x)
    return wave.open("E/" + str(x) + ".wav")
    
def A():
    x = handyRandy()
    x*=6
    x+=1
    x = int(x)
    return wave.open("A/" + str(x) + ".wav")

def B():
    x = handyRandy()
    x*=3
    x+=1
    x = int(x)
    return wave.open("B/" + str(x) + ".wav")

def Ebump():
    x = handyRandy()
    x*=4
    x+=1
    x = int(x)
    return wave.open("Ebump/" + str(x) + ".wav")

def begin():
    return wave.open("spec/1.wav")

def end():
    return wave.open("spec/2.wav")


def anE(count, countList):
    x = handyRandy()
    x *= 5
    x = int(x)
    if(x<=1):
        countList.append(count)
        return Ebump()
    if(x>1):
        return E()
    
def tbb(count, countList):
    #twelve bar blues
    l = []
    l.append(anE(count,countList))
    count+=1
    l.append(anE(count,countList))
    count+=1
    l.append(anE(count,countList))
    count+=1
    l.append(anE(count,countList))
    count+=1
    l.append(A())
    count+=1
    l.append(A())
    count+=1
    l.append(E())
    count+=1
    l.append(E())
    count+=1
    l.append(B())
    count+=1
    l.append(A())
    count+=1
    l.append(anE(count, countList))
    count+=1
    l.append(B())
    count+=1
    return l
    

    
def create(t):
    count = 0
    countList = []
    countList.append(0)
    x = 0
    l = []
    l.append(begin())
    print(l[0].getparams()[3])
    w = wave.open("mix.wav", 'w')
    fs = l[0].getparams()
    w.setparams(fs)
    while(x<t):
        l.extend(tbb(count,countList))
        x+=1
    countList.append(len(l))
    l.append(end())
    counter = 0
    for x in l:
        f = None
        b = overAny()
        two = x.readframes(fs)
        if(b!='no'):
            one = b.readframes(fs)
            #this 'if' is for unequal lengths
            #i fixed the only problem identified
            #but im leaving it here for now
            if(len(one)!=len(two)):
                two = two[:len(one)]
            f = audioop.add(one,two,x.getparams()[1])
            w.writeframes(f)
        else:
            if((counter in countList) or (counter%2 == 1)):
                print('ouch!\n')
                w.writeframes(two)
            else:
                ra = Brandon()
                three = ra.readframes(fs)
                two = audioop.add(two,three,x.getparams()[1])
                w.writeframes(two)
        counter+=1
    w.close()
    for x in l:
        x.close()
    
    return "Success :P"


#so I got a plan, if A is one less than B, if B is on less than A
#then were gonna want to use the sliding window technique cause its faster
#otherwise, we find the least common multiple
#if the least common multiple is where were from or where were going to,aka A or B
#then we scale once, either up or down depending
#other wise we scale up, and then down,
def chSpeed(a=1,b=1): #written for ratio a/b duration change
    b = int(b)  #B number of buckets
    a = int(a)  #translates to A number of buckets
    c = 1
    if(b==0 or a==0):
        return
    if(a>b):
        c = int(a/b)
    else:
        c = int(b/a)
    w = wave.open("nFactorialBarBlues.wav", 'w')
    r = wave.open("mix.wav", 'r')
    pa = r.getparams()
    pi = [pa[0],pa[1],pa[2],1,pa[4],pa[5]]
    print(pa)
    print(pi)
    w.setparams(pa)
    it = 0
    song=[]
    while(it < pa[3]):
        one = r.readframes(1)
        two = r.readframes(1)
        three = r.readframes(1)
        four = r.readframes(1)
        five = r.readframes(1)
        #if there not equal cause there are odd packets, bad fix, just write one
        if(len(one)!=len(two)):
            song.append(one)
        if(len(three)!=len(four)):
            song.append(three)
        one=((audioop.mul(audioop.add(one,two,pi[3]),pi[3],0.5)))
        two=((audioop.mul(audioop.add(two,three,pi[3]),pi[3],0.5)))
        three=((audioop.mul(audioop.add(three,four,pi[3]),pi[3],0.5)))
        four=((audioop.mul(audioop.add(four,five,pi[3]),pi[3],0.5)))
        song.append((audioop.mul(audioop.add(one,two,pi[3]),pi[3],0.5)))
        song.append((audioop.mul(audioop.add(two,three,pi[3]),pi[3],0.5)))
        song.append((audioop.mul(audioop.add(three,four,pi[3]),pi[3],0.5)))
        #song.append((audioop.mul(audioop.add(four,five,pi[3]),pi[3],0.5)))
        it=it+5
    sing = ''.join(song)
    w.writeframes(sing)
    it = 0
    w.close()
    r.close()
    #practice with 4/5 duration
    
        

# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


#coming soon... fft, pitch, and tempo 













