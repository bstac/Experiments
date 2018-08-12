import math
pi = math.pi

theta=[]
for x in range(30):
  theta.append((-pi + (pi/8.0))+(x*(pi/4.0)))

r1=[]
for x in theta:
  r1.append((pi+x))

r2 = []
for x in r1:
  r2.append((x*20))

xp1=[]
for x in range(len(theta)):
  xp1.append(r1[x]*math.cos(theta[x]))
    
xp2=[]
for x in range(len(theta)):
  xp2.append(r2[x]*math.cos(theta[x]))
    
yp1=[]
for x in range(len(theta)):
  yp1.append(r1[x]*math.sin(theta[x]))
    
yp2=[]
for x in range(len(theta)):
  yp2.append(r2[x]*math.sin(theta[x]))


sss=''
for x in range(len(xp1)-1):
  pn1 = str(220+int(xp1[x]/4))+','+str(300-int(yp1[x]/4))
  pn2 = str(220+int(xp2[x]/4))+','+str(300-int(yp2[x]/4))
  pn3 = str(220+int(xp2[x+1]/4))+','+str(300-int(yp2[x+1]/4))
  pn4 = str(220+int(xp1[x+1]/4))+','+str(300-int(yp1[x+1]/4))
  pn = pn1+' '+pn2+' '+pn3+' '+pn4+' '
  left = '<polygon points="'
  right = '" style="fill:lime;stroke:purple;stroke-width:1" />'
  sss+=left + pn+ right + '\n'

print(sss)




