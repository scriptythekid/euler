#euler2
sum=2
f=[1,2]
def nf():
  i=len(f)-1
  return f[i-1]+f[i]

done=False
while not done:
  x=nf()
  if x >= 4000000:
    done=True
  else:
    f.append(x)
    if x % 2 ==0:
      sum+=x
print sum
