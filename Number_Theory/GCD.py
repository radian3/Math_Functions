def main(): # Greatest Common Divisor calculator
 x = input("Put in the first value: ")
 if (x == "x"):
  return
 x = int(x)
 y = int(input("Put in the second value: "))
 if (x > y): # figuring out which value is bigger
    a = x
    b = y
 else:
     a = y
     b = x

 q = int(a/b)  # value
 r = a%b       # remainder	
 print(str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r)) # printing the step
 while (r !=0): # doing more iterations until we have the GCD
  a = b
  b = r
  q = int(a/b)
  r = a%b
  print(str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r)) # printing step
 print ("The GCD is", b)
 print ("Type 'x' without the quotes to quit. Otherwise, you may continue")
 print("")
 return main()
 
  
main()
