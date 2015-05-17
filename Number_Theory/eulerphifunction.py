def main(): # function for outputing the numbers relatively prime to the input as well as how many numbers are relatively prie to the input
 n = input("Euler Phi Function input: ") # storing the number we will compute phi(n) of
 if (str(n) == "x"): # seeing if user wants to end the session
  return
 n = int(n)
 print ("List of integers relatively prime to the input: ")
 relativelyPrimeNums = [] # this list will show all numbers relatively prime to the input
 if (n==1): 
    print([1])
    return main()
 for i in range (1, n): # checking all integers up to n
    if (GCD(i, n) == 1): # checking if the current integer is relatively prime
        relativelyPrimeNums.append(i) # appending to our list of relatively prime numbers
 
 print(relativelyPrimeNums) # printing out the list of relatively prime numbers
 print("Amount of numbers relatively prime to the input:", len(relativelyPrimeNums)) 
 print ("Type 'x' without the quotes to end, otherwise you may continue.")
 print("")
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

 
