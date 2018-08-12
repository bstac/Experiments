from copy import deepcopy
import random
from tkinter import *
from math import *


def butt(a): return int(cos(a)*100000)/100000,int(sin(a)*100000)/100000
def buttt(a): return cos(a),sin(a)

def Paint(ht=600, wd=600):
    psize=4
    master = Tk()
    w = Canvas(master, width=wd, height=ht)
    w.pack()
    delta=[0,0]
    dd=[0,0,0]
    def pnt( event ):
        x1, y1 = (event.x-psize), (event.y-psize)
        x2, y2 = (event.x+psize), (event.y+psize)
        #ccc = str(hex(dd[0]%127))+str(hex(dd[1]%127))+str(hex(dd[2]%127))
        ccc = '#%02x%02x%02x' % (dd[0]%256, dd[1]%256, dd[2]%256)
        #w.create_line( x1, y1, x2, y2, fill = ccc )
        #w.create_oval( x1, y1, x2, y2, fill = ccc )
        w.create_line( event.x, event.y, delta[0], delta[1], fill = ccc )
        delta[0] = event.x
        delta[1] = event.y
        dd[0]+=19
        dd[1]+=17
        dd[2]+=43
    #for not motion <Button-1>
    w.bind( "<B1-Motion>", pnt )
    master.mainloop()


def Image(name,ht=600, wd=600):#does not work
    a = open(name,'rb')
    b = a.read()
    a.close()
    c = []
    x=0
    while(x<len(b)-3):
        c.append([int(b[x]),int(b[x+1]),int(b[x+3])])
        x+=3
    d = []
    master = Tk()
    w = Canvas(master, width=wd, height=ht)
    w.pack()
    for x1 in range(61):
        for y1 in range(61):
            pt = (x1*61)+y1
            fff = '#%02x%02x%02x' % (int(b[pt])%256, int(b[pt])%100, int(b[pt])%200)
            w.create_oval( x1*8, y1*8, x1*8+6, y1*8+6, fill = fff)
    master.mainloop()


def dis():
    canvas_width = 600
    canvas_height =600
    master = Tk()
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    img = PhotoImage(file="cubeDetail.png")
    #canvas.create_image(20,20, anchor=NW, image=img)
    for x in range(img.width()):
        for y in range(img.height()):
            cc = img.get(x,y)
            ccc = '#%02x%02x%02x' % cc
            #canvas.create_oval( 2*x, 2*y, x*2+4, y*2+4, fill = ccc )
            canvas.create_line( 3*x, 3*y, x*3, y*3+7, fill = ccc )
            canvas.create_line( x, y, x+1, y+1, fill = ccc )
        #print(str(img.get(x//5,y)))#dont do this
    mainloop()


def diss():
    canvas_width = 300
    canvas_height =300
    master = Tk()
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    img = PhotoImage(file="cubeDetail.png")
    canvas.create_image(20,20, anchor=NW, image=img)
    for x in range(4 * canvas_width):
        y = int(canvas_height/2 + canvas_height/4 * sin(x/80.0))
        img.put("#ffffff", (x//4,y))
        #print(str(img.get(x//5,y)))#dont do this
    mainloop()




def Char():
    psize = 10
    ccc = '#%02x%02x%02x' % (100,100,100)
    #head,neck,tailbone
    spine = [[300,40],[300,80],[300,120]]
    lArm = [[260,80],[220,120]]
    rArm = [[340,80],[380,120]]
    lLeg = [[260,160],[220,200]]
    rLeg = [[340,160],[380,200]]
    body = [spine,lArm,rArm,lLeg,rLeg]
    canvas_width = 600
    canvas_height =600
    master = Tk()
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    for x in body:
        for y in x:
            canvas.create_oval( y[0]-psize, y[1]-psize, y[0]+psize, y[1]+psize, fill = ccc )
    canvas.create_line( spine[0][0], spine[0][1], spine[1][0], spine[1][1], fill = ccc )
    canvas.create_line( spine[1][0], spine[1][1], spine[2][0], spine[2][1], fill = ccc )
    canvas.create_line( spine[1][0], spine[1][1], lArm[0][0], lArm[0][1], fill = ccc )
    canvas.create_line( spine[1][0], spine[1][1], rArm[0][0], rArm[0][1], fill = ccc )
    canvas.create_line( lArm[0][0], lArm[0][1], lArm[1][0], lArm[1][1], fill = ccc )
    canvas.create_line( rArm[0][0], rArm[0][1], rArm[1][0], rArm[1][1], fill = ccc )
    canvas.create_line( spine[2][0], spine[2][1], lLeg[0][0], lLeg[0][1], fill = ccc )
    canvas.create_line( spine[2][0], spine[2][1], rLeg[0][0], rLeg[0][1], fill = ccc )
    canvas.create_line( lLeg[0][0], lLeg[0][1], lLeg[1][0], lLeg[1][1], fill = ccc )
    canvas.create_line( rLeg[0][0], rLeg[0][1], rLeg[1][0], rLeg[1][1], fill = ccc )
        #print(str(img.get(x//5,y)))#dont do this
    mainloop()




def ReChar():
    #root[x,y, nodes[]]
    #node[x-length,y-length,size,children[]]
    lHand = [-5,50,5,[]]#base case is len(children)==0
    rHand = [5,50,5,[]]#base case is len(children)==0
    lElbow = [-10,60,8,[lHand]]
    rElbow = [10,60,8,[rHand]]
    lArm = [-40,10,10,[lElbow]]
    rArm = [40,10,10,[rElbow]]
    lFoot = [-10,70,5,[]]#base case is len(children)==0
    rFoot = [10,70,5,[]]#base case is len(children)==0
    lKnee = [-25,80,10,[lFoot]]
    rKnee = [25,80,10,[rFoot]]
    lLeg = [-20,10,10,[lKnee]]
    rLeg = [20,10,10,[rKnee]]
    tail = [0,80,5,[lLeg,rLeg,]]
    neck = [0,40,5,[lArm,rArm,tail]]
    head = [300,40,20,[neck]]
    canvas_width = 640
    canvas_height =640
    master = Tk()
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    def shit(node,x,y,root):
        ccc = '#%02x%02x%02x' % (100,100,100)
        xx = x + node[0]
        yy = y + node[1]
        psize = node[2]
        for n in node[3]:
            shit(n,xx,yy,False)
        canvas.create_oval( xx-psize, yy-psize, xx+psize, yy+psize, fill = ccc )
        if(not root):canvas.create_line( x, y, xx, yy, fill = ccc )
    shit(head,0,0,True)
    mainloop()






def AngleFeet():
    #root[x,y, nodes[]]
    #node[limbLength,theta,h-symmetry,size,children[]]
    lFore = [pi/6,50,5,True,[]]#base case is len(children)==0
    rFore = [pi/6,50,5,False,[]]#base case is len(children)==0
    lElbow = [pi/4,60,8,True,[lFore]]
    rElbow = [pi/4,60,8,False,[rFore]]
    lShoulder = [pi/2,30,10,True,[lElbow]]
    rShoulder = [pi/2,30,10,False,[rElbow]]
    lFoot = [pi/12,70,5,True,[]]#base case is len(children)==0
    rFoot = [pi/12,70,5,False,[]]#base case is len(children)==0
    lKnee = [pi/8,80,10,True,[lFoot]]
    rKnee = [pi/8,80,10,False,[rFoot]]
    lLeg = [pi/2,20,10,True,[lKnee]]
    rLeg = [pi/2,20,10,False,[rKnee]]
    tail = [0,80,5,False,[lLeg,rLeg,]]
    neck = [0,40,5,False,[lShoulder,rShoulder,tail]]
    head = [0,40,20,False,[neck]]
    canvas_width = 640
    canvas_height =640
    master = Tk()
    #text = Text(master)
    #text.insert(INSERT, "Jui Jitsoo!!!!!!")
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    def shit(node,x,y,root):
        ccc = '#%02x%02x%02x' % (100,100,100)
        ang = node[0]
        if(node[3]): ang*= -1
        xx,yy = butt(ang+(pi/2))
        xx = (xx * node[1])+x
        yy = (yy * node[1])+y
        psize = node[2]
        for n in node[4]:
            shit(n,xx,yy,False)
        canvas.create_oval( xx-psize, yy-psize, xx+psize, yy+psize, fill = ccc )
        if(not root):canvas.create_line( x, y, xx, yy, fill = ccc )
    shit(head,300,80,True)
    #mainloop()
    ff=1
    fff=1
    ffff=1
    while(True):
        master.update_idletasks()
        master.update()
        canvas.delete("all")
        if(lElbow[0]>6*pi+3 or lElbow[0]<-6*pi ): fff *=-1
        lFore[0]+=fff*pi/64
        lElbow[0]+=fff*pi/77
        if(rElbow[0]>2*pi+3 or rElbow[0]<-2*pi ): ffff *=-1
        rElbow[0]-=ffff*pi/125
        rKnee[0]+=pi/1000
        if(lKnee[0]>pi*2/3 or lKnee[0]<-pi/32): ff *=-1
        fact = ff*(pi/1200)
        lKnee[0]+=fact
        lFoot[0]+= pi*fact*fact
        #text.pack()
        shit(head,300,80,True)
        


def Reach(ht=600, wd=600):
    ccc = '#%02x%02x%02x' % (120,100,200)
    canvas_width = ht
    canvas_height = wd
    master = Tk()
    w = Canvas(master, width=wd, height=ht)
    w.pack()
    numSeg = 2
    segLen = 200
    xList = []
    yList = []
    for n in range(numSeg):
        xList.append(0)
        yList.append(0)
    xList[-1] = wd//2
    yList[-1] = ht
    def rea(i,xx,yy):
        dx = xx - xList[i]
        dy = yy - yList[i]
        ang = atan2(dy,dx)
        targX = xx - (cos(ang) * segLen)
        targY = yy - (sin(ang) * segLen)
        if(i==numSeg-1):
            x1 = (wd//2) + (cos(ang) * segLen)
            y1 = ht + (sin(ang) * segLen)
            w.create_line( wd//2, ht, x1, y1, fill = ccc )
            xList[i-1] = x1
            yList[i-1] = y1
            return x1,y1
        else:
            x1, y1 = rea(i+1, targX, targY)
            x2 = x1 + (cos(ang) * segLen)
            y2 = y1 + (sin(ang) * segLen)
            w.create_line( x1, y1, x2, y2, fill = ccc )
            if(i > 0):
                xList[i-1] = x2
                yList[i-1] = y2
            return x2,y2           
    def pnt( event ):
        w.delete("all")
        rea(0,event.x,event.y)
    w.bind( "<B1-Motion>", pnt )
    master.mainloop()



def Point(ht=600, wd=600):
    #root[x,y, nodes[]]
    #node[limbLength,theta,h-symmetry,size,children[], position x, position y]
    lFore = [pi/6,50,5,True,[],0,0]#base case is len(children)==0
    rFore = [pi/6,50,5,False,[],0,0]#base case is len(children)==0
    lElbow = [pi/4,60,8,True,[lFore],0,0]
    rElbow = [pi/4,60,8,False,[rFore],0,0]
    lShoulder = [pi/2,30,10,True,[lElbow],0,0]
    rShoulder = [pi/2,30,10,False,[rElbow],0,0]
    lFoot = [pi/12,70,5,True,[],0,0]#base case is len(children)==0
    rFoot = [pi/12,70,5,False,[],0,0]#base case is len(children)==0
    lKnee = [pi/8,80,10,True,[lFoot],0,0]
    rKnee = [pi/8,80,10,False,[rFoot],0,0]
    lLeg = [pi/2,20,10,True,[lKnee],0,0]
    rLeg = [pi/2,20,10,False,[rKnee],0,0]
    tail = [0,80,5,False,[lLeg,rLeg,],0,0]
    neck = [0,40,5,False,[lShoulder,rShoulder,tail],0,0]
    head = [0,40,20,False,[neck],0,0]
    arm = [lFore,lElbow]
    rarm = [rFore,rElbow]#,rShoulder]
    canvas_width = 640
    canvas_height =640
    master = Tk()
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    def rea(rx,ry,limb):
        xx=rx
        yy=ry
        for lmb in limb:
            dx = xx - lmb[5]
            dy = yy - lmb[6]
            ang = atan2(dy,dx)
            xx = xx - (cos(ang) * lmb[1])
            yy = yy - (sin(ang) * lmb[1])
            ang-=(pi/2)
            if(lmb[3]): ang*= -1
            lmb[0] = ang  
    def pnt( event ):
        canvas.delete("all")
        rea(event.x,event.y,arm)
        rea(event.x,event.y,rarm)
        draw(head,300,80,True)
    def draw(node,x,y,root):
        ccc = '#%02x%02x%02x' % (100,100,100)
        ang = node[0]
        if(node[3]): ang*= -1
        xx,yy = buttt(ang+(pi/2))
        xx = (xx * node[1])+x
        yy = (yy * node[1])+y
        node[5] = x
        node[6] = y
        psize = node[2]
        for n in node[4]:
            draw(n,xx,yy,False)
        canvas.create_oval( xx-psize, yy-psize, xx+psize, yy+psize, fill = ccc )
        if(not root):canvas.create_line( x, y, xx, yy, fill = ccc )
    draw(head,300,80,True)
    canvas.bind( "<B1-Motion>", pnt )
    mainloop()



def Follow(ht=600, wd=600, nummy=200, seggy=2):
    ccc = '#%02x%02x%02x' % (120,100,200)
    canvas_width = ht
    canvas_height = wd
    master = Tk()
    w = Canvas(master, width=wd, height=ht)
    w.pack()
    numSeg = nummy
    numSegAdjust = (numSeg//4)+numSeg
    numAdjust = (numSegAdjust//2)
    numAdjust = (numAdjust*numAdjust)+(numAdjust*numSegAdjust)
    segLen = seggy
    xList = []
    yList = []
    for n in range(numSeg):
        xList.append(0)
        yList.append(0)
    xList[-1] = wd//2
    yList[-1] = ht
    def rea(i,xx,yy):
        dx = xx - xList[i]
        dy = yy - yList[i]
        ang = atan2(dy,dx)
        targX = xx - (cos(ang) * segLen)
        targY = yy - (sin(ang) * segLen)
        linewidth = (((-i*i)+(i*numSegAdjust))//numAdjust) + 1
        if(i==numSeg-1):
            x1 = targX + (cos(ang) * segLen)
            y1 = targY + (sin(ang) * segLen)
            w.create_line( targX, targY, x1, y1, fill = ccc, width=linewidth )
            xList[i-1] = x1
            yList[i-1] = y1
            return x1,y1
        else:
            x1, y1 = rea(i+1, targX, targY)
            x2 = x1 + (cos(ang) * segLen)
            y2 = y1 + (sin(ang) * segLen)
            w.create_line( x1, y1, x2, y2, fill = ccc, width=linewidth )
            if(i > 0):
                xList[i-1] = x2
                yList[i-1] = y2
            return x2,y2           
    def pnt( event ):
        w.delete("all")
        rea(0,event.x,event.y)
    w.bind( "<B1-Motion>", pnt )
    master.mainloop()



def tree():
    ccc = '#%02x%02x%02x' % (120,66,18)
    cct = '#%02x%02x%02x' % (20,90,50)
    canvas_width=1000
    canvas_height=900
    br=3
    dp=6
    ed=25
    tr = [pi/2,2,5,False,[],dp*ed,dp+2]
    base = [-pi/2,10,10,False,[],dp*ed//2,dp+20]
    def trRec(brr,i,ll):
        if(i<1):
            return []
        for x in range(brr):
            angy=(pi/4)*(x)+(pi/4)
            angy+=(pi/(64//(1+dp-i)))*((random.random()*9//2)-2) 
            lll=trRec(brr, i-1,[-angy,0*i,(dp-1),False,[],ed*i,i])
            if(lll!=[]):ll[4].append(lll)
        return ll
    tr = trRec(br,dp,tr)
    tr[0]=-pi/2
    base[4].append(tr)
    master = Tk()
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    def draw(node,x,y,root):
        ang = node[0]
        if(node[3]): ang*= -1
        xx,yy = buttt(ang)
        happy = int(node[1])
        if(happy<node[5]):
            node[1]+=(random.random()*(node[6]+1)//2)
        if(node[0]<pi+0.1 and node[0]>-0.01 and not root):
            node[0]+=(pi/(64*(1+dp-node[6])))*((random.random()*9//2)-2)    
        xx = (xx * happy)+x
        yy = (yy * happy)+y
        psize = node[2]//17+1
        if(node[2]<(node[6])*50):node[2]+=node[2]/ed
        for n in node[4]:
            h=False
            if(len(node[4])==1):h=True
            draw(n,xx,yy,False)
        if(node[6]<4 and not root):
            canvas.create_oval( xx-psize, yy-psize, xx+psize, yy+psize, fill = cct)
        llww = node[6] * ((node[1]//100)+ 1)
        if(root):llww = node[6] * ((node[1]//77)+ 1)
        canvas.create_line( x, y, xx, yy, fill = ccc, width=llww  )
    draw(base,canvas_width//2,canvas_height,True)
    while(True):
        master.update_idletasks()
        master.update()
        canvas.delete("all")
        draw(base,canvas_width//2,canvas_height,True)
    

    
