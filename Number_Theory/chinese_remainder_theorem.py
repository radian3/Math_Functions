# chinese remainder theorem
# input the equations
# output is the solution to all of the equatios

def main():
 n = int(input("List the number of equations: ")) 
 aValues = []
 mValues = []
 print ("") 
 for i in range (1, n+1):
  print("x = a" + str(i) + " mod m" + str(i)) # showing the user the format
 print("")
 M = 1 # setting up to compute our M
 for i in range (0, n):
  a = int(input("Please enter a" + str(i+1) + ": ")) # getting the a value for the equation
  aValues.append(a)
  m = int(input("Please enter m" + str(i+1) + ": ")) # getting the m value for the equation
  mValues.append(m)
  M*=m # multiplying or m's together to get M

 # checking if our modulus values are pairwise relatively prime   
 for j in range (0, n-1): # compare the first value to the second value; then the first value to the third value.......
  for i in range (j+1, n): # all the way up to the second to last value compared to the last value
   if (GCD(mValues[j], mValues[i]) != 1): # if the GCD is not 1, then our modulus values are not pairwise relatively prime
    print("Modulus values are not pairwise relatively prime")
    return  # no solutions
  
 
 
 inverseValues=[] 
 solution = 0 # going to be used for the answer to the system of congruences
 for i in range (0, n):
  inverseValues.append(inverse((M/mValues[i]), mValues[i])) # computing the inverse values
  solution += aValues[i]*inverseValues[i]*M/mValues[i] # adding up the values for the solution
  print ("x = " + str(aValues[i]) + " mod " + str(mValues[i]))  # printing off each equation, one at a time
 print("The solution is: ") # done with the loop; about to print the solution
 print ("x = " + str(int(solution%M)) + " mod " + str(M)) # printing the solution
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
    answer = x0
    break
 
 return answer%m


main()







