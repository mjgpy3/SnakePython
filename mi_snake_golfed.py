import random as r
import curses as c
def g(s,w,l):
 while 1:
  p=[r.randrange(0,w),r.randrange(0,l)]
  for l in s:
   if l==p:continue
  return p
s=[]
d=[0,1]
p=k=n=0
e=100
v={65:[-1,0],66:[1,0],68:[0,-1],67:[0,1]}                                                                                     
z=c.initscr()
w,l=z.getmaxyx()[0],z.getmaxyx()[1]
c.noecho()
z.clear()
x=g(s,w,l)
s.append([w/2,l/2])
z.nodelay(1)
q=lambda h,i:range(h,len(i))
while k!=101:
 k=z.getch()
 if k in v and not (d[0]==(v[k][0]*-1) and d[1]==(v[k][1]*-1)):d=v[k]
 f=[0,0]
 for i in q(0,s):
  if i == 0:
   f=[s[i][0],s[i][1]]
   s[i][0]+=d[0]
   s[i][1]+=d[1]
  else:s[i],f=f,s[i]
 if s[0]==x:
  n+=1
  s.append(f)
  x=g(s,w,l)
 z.clear()
 if s[0][0]>=w or s[0][1]>=l or s[0][0]<0 or s[0][1]<0:break
 for i in q(1,s):
  if s[0] == s[i]: k = 101
 for i in q(0,s):z.addch(s[i][0],s[i][1],"X")
 z.addch(x[0],x[1],"O")
 z.move(0,0)
 z.refresh()
 if d[1]!=0:c.napms(e/2)
 else:c.napms(e)       
c.endwin()
print 'Score: %s'%n
