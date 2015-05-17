# ax = b mod m
# m | ax - b or ax-b%m = 0


# this function finds all solutions to a linear congruence
def main():
 print("ax = b mod m") # showing the user the format
 a = input("Put in a: ") # getting input
 if (a == "x"): # seeing if the user wants to quit
    return
 a = int(a)
 b = int(input("Put in b: "))
 m = int(input("Put in m: "))
 b = b%m # simplifying input
 a = a%m # simplifying input
 numberOfSolutions = GCD(a, m) # computing the number of solutions
 if (b%numberOfSolutions!=0): # if b does not divide GCD(a, m) then there's no solutions
    print ("No Solutions.")
    return
 solutions = [] # list for the solutions
 for x0 in range (1, m): # checking each number in the modulus
     if ((a*x0-b)%m==0): # checking if the integer x = x0 is a solution
      solutions.append(x0)
      if (len(solutions) == numberOfSolutions): # checking to see if we found all of our solutions
        break
 print ("The list of solutions for" , str(a) + "x=" + str(b) + "mod" + str(m) + " are:")
 print (solutions) # printing out the list of solutions
 print ("Type 'x' without quotes if you would like to quit. Otherwise, you may continue.")
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
