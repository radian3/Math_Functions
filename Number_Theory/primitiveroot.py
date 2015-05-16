

def main():
 primlist = []
 x = -1   
# a = int(input("Checking numbers 1-"))
 modulus = input("Please enter the modulus: ")
 if (modulus == "x"):
    return
 modulus = int(modulus)
 print("Printing out a list of all primitive roots modulo ", modulus)
 for base in range(1, modulus+1): # j will be the base
  if (GCD(base, modulus)!=1):  # need (j, modulus) = 1
     continue
  for i in range (1, modulus+1): # only need to check powers that divide b
   val = base**i
   reducedval = (val-(val//modulus)*modulus) 
   if (reducedval == 1):
      x = i
      break
  r = phi(modulus)
  if (x == r):
   primlist.append(base)
 print("") 
 if (len(primlist)==0):
    print("There are no primitive roots modulo ", modulo)
 else:
     print(primlist)
 print("")    
 print("Type 'x' with no quotes if you want to exit. Otherwise, you may continue")
 return main()




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
main()
