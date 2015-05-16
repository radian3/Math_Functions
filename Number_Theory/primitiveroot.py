

def simp():
 primlist = []
 x = -1   
# a = int(input("Checking numbers 1-"))
 b = int(input("Put in modulus: "))
 for j in range(1, b+1):
  if (GCD(j, b)!=1):
     continue
  for i in range (1, b+1): # only need to check powers that divide b
   val = j**i
   reducedval = (val-(val//b)*b) 
   if (reducedval == 1):
      x = i
      break
  r = phi(b)
  if (x == r):
   primlist.append(j)
 
 if (len(primlist)==0):
    print("No primitive roots")
 else:
     print(primlist)
 return simp()




def phi(n):
 if (n==1):
    
    return 1
 counter = 0
 for i in range (1, n):
    if (GCD(i, n) == 1):
        counter += 1
 
 return counter       




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
simp()
