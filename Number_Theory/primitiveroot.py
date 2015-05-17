def main():
 primitiveRootList = [] # initializing our list that will be used to store the primitive roots
 modulus = input("Please enter the modulus: ")
 if (modulus == "x"):
    return
 modulus = int(modulus)
 print("Printing out a list of all primitive roots modulo ", modulus)
 order_candidates = [] # initializing a list that will be used for candidates of the possible order
 phiOfModulus = phi(modulus)
 for exponent in range (1, phi(modulus)+1): # looping to store all possible candidates for the order of any base
  if (phiOfModulus%exponent == 0): # need the exponent to divide phi(modulus)
      order_candidates.append(exponent) # storing the exponent

 for base in range(1, modulus+1):
  if (GCD(base, modulus)!=1):  # need (base, modulus) = 1 for the base to be a candidate for a primitive root
     continue # skip to checking the next base
  for i in range (0, len(order_candidates)): # only need to check powers that divide b
   exponent = order_candidates[i] # checking each exponent to see if it is the order
   value = base**exponent # computing the base raised to the exponent 
   if (value%modulus == 1): # checking if our value is congruent to 1
      order = exponent # we found the order so we break out of the inner for loop
      break
  # out of the inner for loop now
  if (order == phiOfModulus): # if this condition is satisfied, our base is a primitive root
   primitiveRootList.append(base) # storing the root

 print("") 
 if (len(primitiveRootList)==0): # if we did not find any primitive roots
    print("There are no primitive roots modulo ", modulus)
 else:
     print(primitiveRootList) # printing a list of the primitive roots
 print("")    
 print("Type 'x' with no quotes if you want to exit. Otherwise, you may continue")
 return main() # getting the user to input another modulus or exit




def phi(n): # Euler Phi Function calculator
 if (n==1):
    
    return 1
 counter = 0
 for i in range (1, n):
    if (GCD(i, n) == 1):
        counter += 1
 
 return counter       




def GCD(x,y): # Greatest Common Divisor

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
