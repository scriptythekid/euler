import math


x =999
y=999
pl=[]
done=False
while not done:
  p=x*y
  s=str(p)
  rs=s[::-1]
  #print s
  #print rs
  if s == str(rs):
    if len(pl) ==0 or s > pl[len(pl)-1][0]:
      print s
      print x,y
      pl.append((s,x,y))
    #done=True
  x-=1
  if x<900:
    if y==900:
      done=True
    x=999
    y-=1
    
    #done=True
    