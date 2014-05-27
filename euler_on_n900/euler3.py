import math

n=600851475143

fs=[]
x=2
def pdiv(k):
  global x  
  p=math.sqrt(k)
  while x < p:
    while k % x ==0:
      print x
      fs.append(x)
      #a eval a day keeps sanity at bay
      if int(eval('*'.join([str(r) for r in fs]))) == n:
        return
      k=k/x
    x+=2 if x > 2 else 1
pdiv(n)

print "n",n
print fs
a=1
for x in fs:
  a=a*x
print "n2",a