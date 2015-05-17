# ax = b mod m
# m | ax - b
# need (ax-b)%m = 0
def main():
 print ("ax = b (modm)")
 a = int(input("Put in a: "))
 b = int(input("Put in b: "))
 m = int(input("Put in m: "))
 d = GCD(a, m)
 if (b%d!=0):
     print ("No solutions.")
     return main()
 solutions = []
 x = 1
 while (True):
  if ((a*x-b)%m==0):
    solutions.append(x%m)
  if (len(solutions)== d):
      break
  x += 1
 print ("The solutions are: ")
 print (solutions)
 return main()
 





















def GCD(x,y): # Greatest Common Divisor function used in main

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
main()
