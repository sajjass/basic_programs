def fib():
 t =[]
 a,b = 1,1
 while a < 4000000:
     if a % 2 == 0:
         t.append(a)
     a,b = b,a+b
 return t
print sum(fib())
