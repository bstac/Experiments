ls = 'Content-Type:application/octet-stream; name = "t.txt" '
ls += '\nContent-Disposition: attachment; filename = "t.txt"\n\n'
print(ls)

fo = open('t.txt','r')
print(fo.read())
fo.close()

