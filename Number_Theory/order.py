def main(): # this function computes the order of an integer
 base = input("Put in your base: ")
 if (base == "x"):
     return
 base = int(base)
 modulus = int(input("Put in modulus: "))
 if (GCD(base, modulus) != 1):
    print ("There is no order because the GCD of", base, "and", modulus, "is not 1")
    print ("Type 'x' without quotes to quit. Otherwise, you may continue")
    return main()
 for exponent in range (1, modulus+1):
  val = base**exponent
  reducedval = (val-(val//modulus)*modulus) 
  if (reducedval == 1):
      index = exponent
      break

 print ("The order is ", index)
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
