def fib(n):
   if (n<=1):
        return n
   else:
       return (fib(n-1) + fib(n-2))

limit = int(input('enter the length of sequence: '))
for i in range(limit):
     print (fib(i), end = ' ')
