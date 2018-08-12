from copy import deepcopy
import random
from tkinter import *
import itertools


#0 = no peice
#1 = white
#2 = black
#3 ->?how to handle removed peices and situations?
def CreateBoard(n=19):
    l=[]
    for x in range(n):
        k=[]
        for y in range(n):
            k.append(0)
        l.append(k)
    return l

def PrintBoard(l):
    for x in l:
        print(x)

def PersonInputMakeMove(board, player):
    size = len(board)
    check = False
    row=''
    col=''
    while(not check):
        print(NumberToPlayerName(player))
        rowIn = input('Choose a Row (%'+str(size)+'): ')
        row= (ConvertUserInput(rowIn)-1)%size
        colIn = input('Choose a Column (%'+str(size)+'): ')
        col = (ConvertUserInput(colIn)-1)%size
        check=CheckSpotIsVacant(board,row,col)
    board[row][col]=player
    PrintBoard(board)

def NumberToPlayerName(number):
    name='none'
    if(number==1): name='White'
    elif(number==2): name='Black'
    return name

def ConvertUserInput(s):
    digit=1
    num=0
    for x in s:
        num+=((ord(x)+2)%10)*(pow(10,len(s)-digit))
        digit+=1
    return num

def CheckSpotIsVacant(board, row, col):
    check=False
    if(board[row][col]==0):check=True
    return check

def CheckBoardHasOpenSpace(board):
    check=False
    for x in board:
        for y in x:
            if(y==0):check=True
    return check

def NoRulesMonoVsMono(n=19):
    board = CreateBoard(n)
    white = [1,PersonInputMakeMove]
    black = [2,PersonInputMakeMove]
    while(CheckBoardHasOpenSpace(board)):
        white[1](board,white[0])
        if(not CheckBoardHasOpenSpace(board)):
            break
        black[1](board,black[0])
    print('The Game Has Ended')


def ReportLiberty(board):
    n=len(board)
    white=[]
    black=[]
    atari = []     #[[],[]]
    for x in range(n):
        for y in range(n):
            string = []
            lib=[]
            center=board[x][y]
            if(center==0): continue
            posLib = 4
            up=x-1
            down=x+1
            left=y-1
            right=y+1
            if(up < 0):
                posLib-=1
            else:
                if(board[up][y]==center):
                   string.append((up,y))
                lib.append(board[up][y])
            if(down >= n):
                posLib-=1
            else:
                if(board[down][y]==center):
                    string.append((down,y))
                lib.append(board[down][y])
            if(left < 0):
                posLib-=1
            else:
                if(board[x][left]==center):
                    string.append((x,left))
                lib.append(board[x][left])
            if(right >= n):
                posLib-=1
            else:
                if(board[x][right]==center):
                    string.append((x,right))
                lib.append(board[x][right])
            same=0
            enemy=0
            none=0
            for li in lib:
                if(li==0):none+=1
                if(li==center):same+=1
                if(li!=center and li!=0):enemy+=1
            state=str(none) + ' open'
            if(enemy==posLib):state='Capture'
            if(enemy==(posLib-1)):state='Atari'
            #if():state=''
            report = [posLib,none,same,enemy,state,string]
            if(center == 1):white.append([[x,y], lib, report])
            if(center == 2):black.append([[x,y], lib, report])
    atari.append(white)
    atari.append(black)
    StringBean(atari[0]+atari[1])
    return atari

def StringBean(report):
    #report = report[0]+report[1]
    ll=[]
    for rep in report:
        potential=[(rep[0][0],rep[0][1])] + rep[2][5]
        ll.append(potential)
    for rep in report:
        potential=[(rep[0][0],rep[0][1])] + rep[2][5]
        found=False
        cnt=0
        for pot in potential:
            cnt=0
            for fl in ll:
                if pot in fl:
                    ll[cnt]+=potential
                    ll[cnt]=list(set(ll[cnt]))
                cnt+=1
            #if(found):
                #break
        #if(not found):ll.append(potential)
    lll=[]
    for x in ll:
        zz=list(set(x))
        zz.sort()
        lll.append(zz)
    lll.sort()
    llll = list(lll for lll,_ in itertools.groupby(lll))
    for lil in llll:
        count=0
        for little in lil:
            for rep in report:
                if((rep[0][0],rep[0][1])==little
                   and rep[2][0] - rep[2][2] - rep[2][3] == 0 ):
                    count+=1
        if(count==len(lil)): lil.append('Captured')
        else: lil.append('')
    for rep in report:
        for lil in llll:
            if((rep[0][0],rep[0][1]) in lil):
                rep[2][5]=lil[0:len(lil)-1]
                if(lil[-1]!=''):rep[2][4]=lil[-1]
    return llll
        

def test_b():
    b=CreateBoard(9)
    b[5][5]=1
    b[5][6]=2
    b[8][8]=2
    b[7][8]=1
    b[8][7]=1
    b[0][7]=2
    b[0][8]=1
    b[3][3]=2
    b[3][2]=1
    b[3][4]=1
    b[4][3]=1
    b[8][0]=2
    b[7][1]=2
    b[7][2]=2
    b[8][1]=2
    b[6][2]=2
    b[7][0]=1
    b[6][1]=1
    b[5][2]=1
    b[6][3]=1
    b[7][3]=1
    b[8][2]=1
    PrintBoard(b)
    a = ReportLiberty(b)
    PrintLibReport(a)
    return a
    

def PrintLibReport(rep):
    print('White:')
    for x in rep[0]:
        print('\tpeice\t\t\t ' + str(x[0]))
        print('\tliberties:\t\t ' + str(x[1]))
        print('\tpossible liberties:\t ' + str(x[2][0]))
        print('\tstate:\t\t\t ' + x[2][4])
        print('\tstrings:\t\t ' + str(x[2][5]))
    print('Black:')
    for x in rep[1]:
        print('\tpeice\t\t\t ' + str(x[0]))
        print('\tliberties:\t\t ' + str(x[1]))
        print('\tpossible liberties:\t ' + str(x[2][0]))
        print('\tstate:\t\t\t ' + x[2][4])
        print('\tstrings:\t\t ' + str(x[2][5]))

#todo --------------------------------------------
#1)Introduce rules for moves
#2)Atari (and all rules) based on whos moving
#3)Document Land Control
#Idea* web gui? Server?
#Idea* spawn, simple video game?
#-------------------------------------------------


def show(n=19, bb=32):
    psize=10
    beg=bb
    wmax=(n+2)*beg
    end=beg*(n+1)
    master = Tk()
    w = Canvas(master, width=wmax, height=wmax)
    w.pack()
    def paint( event ):
        xx=int((event.x+(beg/2))/beg)*beg
        yy=int((event.y+(beg/2))/beg)*beg
        if(xx<beg):xx=beg
        if(xx>end):xx=end
        if(yy<beg):yy=beg
        if(yy>end):yy=end
        x1, y1 = (xx-psize), ( yy-psize)
        x2, y2 = ( xx+psize), ( yy+psize)
        w.create_oval( x1, y1, x2, y2, fill = "black" )
        #"<B1-Motion>" -> for motion
    w.bind( "<Button-1>", paint )
    w.create_rectangle(beg, beg, end, end, fill="white")
    for x in range(n):
        top = beg + (x*beg)
        w.create_line(top, beg, top, end,  fill="black", width=2)
        w.create_line(beg, top, end, top,  fill="black", width=2)
    mainloop()



def KinterGame(n=19, bb=32):
    board = CreateBoard(n)
    n=n-1
    psize=10
    beg=bb
    wmax=(n+2)*beg
    end=beg*(n+1)
    master = Tk()
    w = Canvas(master, width=wmax, height=wmax)
    w.pack()
    ct=[0]
    def pnt( event ):
        if(not CheckBoardHasOpenSpace(board)): master.destroy()
        xx=int((event.x+(beg/2))/beg)*beg
        yy=int((event.y+(beg/2))/beg)*beg
        if(xx<beg):xx=beg
        if(xx>end):xx=end
        if(yy<beg):yy=beg
        if(yy>end):yy=end
        col=int(((event.x/wmax)*(len(board)+1))-.5)
        row=int(((event.y/wmax)*(len(board)+1))-.5)
        if(col<0):col=0
        if(col>len(board)-1):col=len(board)-1
        if(row<0):row=0
        if(row>len(board)-1):row=len(board)-1
        if(CheckSpotIsVacant(board,row,col)):
            board[row][col]=ct[0]%2+1
            x1, y1 = (xx-psize), ( yy-psize)
            x2, y2 = ( xx+psize), ( yy+psize)
            if(ct[0]%2==0):
                w.create_oval( x1, y1, x2, y2, fill = "black" )
            else:
                w.create_oval( x1, y1, x2, y2, fill = "white" )
            #PrintBoard(board)
            aaa = ReportLiberty(board)
            #PrintLibReport(aaa)
            ct[0]+=1
        #"<B1-Motion>" -> for motion
    w.bind( "<Button-1>", pnt )
    w.create_rectangle(beg, beg, end, end, fill="yellow")
    for x in range(n):
        top = beg + (x*beg)
        w.create_line(top, beg, top, end,  fill="black", width=2)
        w.create_line(beg, top, end, top,  fill="black", width=2)
    master.mainloop()

    

def test_c(n=40):
    b=CreateBoard(19)
    count=0
    for x in range(n):
        p=int(random.random()*(len(b)))
        r=int(random.random()*(len(b)))
        b[p][r]=1+(count%2)
        count+=1
    return b


def Kindling(board=[], n=19, bb=32):
    if(board==[]):board = CreateBoard(n)
    n=len(board)
    psize=10
    beg=bb
    wmax=(n+1)*beg
    end=beg*(n)
    master = Tk()
    w = Canvas(master, width=wmax, height=wmax)
    w.pack()
    ct=[0]
    def pnt( event ):
        if(not CheckBoardHasOpenSpace(board)): master.destroy()
        xx=int((event.x+(beg/2))/beg)*beg
        yy=int((event.y+(beg/2))/beg)*beg
        if(xx<beg):xx=beg
        if(xx>end):xx=end
        if(yy<beg):yy=beg
        if(yy>end):yy=end
        col=int(((event.x/wmax)*(len(board)+1))-.5)
        row=int(((event.y/wmax)*(len(board)+1))-.5)
        if(col<0):col=0
        if(col>len(board)-1):col=len(board)-1
        if(row<0):row=0
        if(row>len(board)-1):row=len(board)-1
        if(CheckSpotIsVacant(board,row,col)):
            board[row][col]=ct[0]%2+1
            x1, y1 = (xx-psize), ( yy-psize)
            x2, y2 = ( xx+psize), ( yy+psize)
            if(ct[0]%2==1):
                w.create_oval( x1, y1, x2, y2, fill = "black" )
            else:
                w.create_oval( x1, y1, x2, y2, fill = "white" )
            PrintBoard(board)
            print("-----------------------------------------------")
            print("-----------------------------------------------")
            aaa = ReportLiberty(board)
            #PrintLibReport(aaa)
            ct[0]+=1
        #"<B1-Motion>" -> for motion
    w.bind( "<Button-1>", pnt )
    w.create_rectangle(beg, beg, end, end, fill="yellow")
    for x in range(n):
        top = beg + (x*beg)
        w.create_line(top, beg, top, end,  fill="black", width=2)
        w.create_line(beg, top, end, top,  fill="black", width=2)
    for x in range(len(board)):
        for y in range(len(board)):
            color="black"
            if(board[x][y]==1):color = "white"
            if(board[x][y]!=0):
                yy=(x*beg)+beg
                xx=(y*beg)+beg #board is inverse x,y from list
                w.create_oval( xx-psize, yy-psize, xx+psize, yy+psize, fill = color )
    master.mainloop()
