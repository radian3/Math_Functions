def phi():
 n = int(input("Euler Phi Function input: "))
 if (n==1):
    print(1)
    return phi()
 counter = 0
 for i in range (1, n):
    if (GCD(i, n) == 1):
        counter += 1
 print(counter)
 return phi()       




def GCD(x,y):

 if (x > y):
    a = x
    b = y
 else:
     a = y
     b = x
 q = int(a/b)
 r = a%b
 while (r !=0):
  a = b
  b = r
  q = int(a/b)
  r = a%b
 return b 



phi()

 
