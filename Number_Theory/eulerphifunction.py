def main():
 n = input("Euler Phi Function input: ")
 if (str(n) == "x"):
  return
 n = int(n)
 print ("List of integers relatively prime to the input: ")
 relativelyPrimeNums = []
 if (n==1):
    print([1])
    return main()
 for i in range (1, n):
    if (GCD(i, n) == 1):
        relativelyPrimeNums.append(i)
 
 print(relativelyPrimeNums)
 print("Amount of numbers relatively prime to the input:", len(relativelyPrimeNums))
 print ("Type 'x' without the quotes to end, otherwise you may continue.")
 print("")
 return main()       




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

 
