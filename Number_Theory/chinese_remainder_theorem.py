# chinese remainder theorem
def main():
 n = int(input("List the number of equations: "))
 aValues = []
 mValues = []
 print ("x = a1 mod m1")
 print ("      .")
 print ("      .")
 print ("      .")
 print("x = an mod mn")
 for i in range (0, n):
  x = int(input("Please enter a" + str(i+1) + ": "))
  aValues.append(x)
  x = int(input("Please enter m" + str(i+1) + ": "))
  mValues.append(x)
  k = 0 
  
 for j in range (0, n-1):
  for i in range (k, n-2):
   if (GCD(mValues[j], mValues[i+1]) != 1):
    print("Modulus values are not pairwise relatively prime")
    return 
  k+=1
 M = 1
 for i in range (0, n):
  M*=mValues[i]
 inverseValues=[]
 for i in range (0, n):
  inverseValues.append(inverse((M/mValues[i]), mValues[i]))
 solution = 0
 for i in range (0, n):
  solution += aValues[i]*inverseValues[i]*M/mValues[i]
 for i in range (0, n):
  print ("x = " + str(aValues[i]) + " mod " + str(mValues[i])) 
 print("The solution is: ")
 print ("x = " + str(int(solution%M)) + " mod " + str(M))
 return
 
 



    
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


def inverse(a, m):
 # ax = 1 mod m
 # m | ax - 1
 a = a%m
 for x0 in range (1, m):
  if((a*x0-1)%m==0):
    inverse = x0
    break
 
 return inverse%m





main()







