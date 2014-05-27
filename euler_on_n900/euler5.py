

# 11 13 17 19
done=False
i=11*13*17*19*20*7*3
c=0
incr=11*13*17*19*20*7*3
#incr=2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20-20
#incr=20
done=False
while not done:
  modnull=True
  if c > 10000:
    print i
    c=-1
  c+=1
  if i % 19 != 0:
    modnull = False
    i+=incr
    continue
  for x in range(2,21):
    #print x
    if i % x != 0:
      modnull=False
      break
  
  
  if modnull:
    print i
    done=True
  #i+=380
  #11 13 17 19  
  i+=incr
