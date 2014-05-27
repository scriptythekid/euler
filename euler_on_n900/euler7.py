import math
def isprime(n):
  w=int(math.sqrt(n))
  for i in range(2,w+1):
    if n % i ==0:
      return False
  return True
  
done=False
ps=[2,]
x=3
while not done:
  if isprime(x):
    ps.append(x)
    #print "prime:",x

  x+=2
  if len(ps) >= 10001:
    done=True
print len(ps),":",ps[len(ps)-1]
