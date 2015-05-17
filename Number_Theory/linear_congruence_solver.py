# ax = b mod m
# m | ax - b or ax-b%m = 0

def main():
 print("ax = b mod m")
 a = input("Put in a: ")
 if (a == "x"):
    return
 a = int(a)
 b = int(input("Put in b: "))
 m = int(input("Put in the modulus: "))
 b = b%m
 a = a%m
 numberOfSolutions = GCD(a, m)
 if (b%numberOfSolutions!=0):
    print ("No Solutions.")
    return
 solutions = []
 for x in range (1, m):
     if ((a*x-b)%m==0):
      solutions.append(x)
      if (len(solutions) == numberOfSolutions):
        break
 print ("The solutions are:")
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
