def main(): # this function computes the order of an integer
 # the order is the lowest such integer, x, that satisfies
 # the congruence a^x = 1modn with (a, n) = 1
 # note: a is the base, x is the exponent, n is the modulus
 base = input("Put in your base: ")
 if (base == "x"): # checking if user wants to exit
     return
 base = int(base)
 modulus = int(input("Put in modulus: "))
 if (GCD(base, modulus) != 1): # if this GCD is not one, then there is no order
    print ("There is no order because the GCD of", base, "and", modulus, "is not 1")
    print ("Type 'x' without quotes to quit. Otherwise, you may continue")
    return main()
 for exponent in range (1, modulus+1):
  value = base**exponent
  
  if (value%modulus == 1): # checking if our value is congruent to 1
      index = exponent # if so, then we found the order and break out of the loop
      break

 print ("The order is ", index) # printing results
 print ("Type 'x' without quotes to quit. Otherwise, you may continue")
 print ("")
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
