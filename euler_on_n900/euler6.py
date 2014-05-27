sumos=0
sqos=0

for i in range(1,101):
  sumos+=i*i
  sqos+=i
sqos*=sqos
print sqos-sumos