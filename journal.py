from datetime import datetime
from random import random

def owc(story,fn,at='w'):
    a = open(fn,at)
    a.write(story)
    a.close()

def orc(fn):
    a = open(fn,'r')
    b = a.read()
    a.close()
    return b

def journal_write():
    date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file = 'C:\\Users\\brandon\\Desktop\\journal\\'+date_time+'_journal.txt'
    owc('',file,'w+')
    try:
        while(True):
            new_story=''
            new_story=str(input(' -\t')+'\n')
            owc(hide_str(new_story),file,'a+')
    except Exception as e:
        print(str(e))
    except:
        print(file)
        print('\nstory complete :) \n\n')

def journal_read():
    try:
        while(True):
            book=''
            book+=str(input('What file to read? '))
            story = orc(book)
            print(view_st(story))
    except Exception as e:
        print(str(e))
    except:
        print('\nLibrary closed :( \n\n')


#c=~a^b
#d=~c^a
#e = ~c^d
#f = ~c^e

def hide_str(st):
    outman=''
    for x_i in list(st):
        x=ord(x_i)
        y = int((random() * 123) + 3)&127
        c=((~x&127)^y)
        d=((~c&127)^x)
        outman+=chr(c)+chr(d)
    return outman

def view_st(st):
    outman = ''
    l_st = list(st)
    for cnt in range(int(len(st)/2)):
        c=ord(l_st[2*cnt])
        d=ord(l_st[(2*cnt)+1])
        e = (~c&127)^d
        f = (~c&127)^e
        outman+=chr(e)
    return outman



while(True):
    print('Menu')
    print('\t -> write')
    print('\t -> read')
    print('\t -> exit')
    decision=''
    decision+=str(input('\nHow may I help you?   '))
    print(decision)
    if(decision.lower().strip()=="read"):
        journal_read()
    elif(decision.lower().strip()=="write"):
        journal_write()
    else:
        print('goodbye!')
        break
