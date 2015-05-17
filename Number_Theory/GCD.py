<<<<<<< HEAD
def main(): # Greatest Common Divisor calculator
 x = input("Put in the first value: ")
 if (x == "x"):
  return
 x = int(x)
 y = int(input("Put in the second value: "))
 if (x > y): # figuring out which value is bigger
=======
def main():
 x = int(input("Put in x: "))
 y = int(input("Put in y: "))
 if (x > y):
>>>>>>> 7449b180171681983dfba1af58b9c7e51c709f1e
    a = x
    b = y
 else:
     a = y
     b = x

<<<<<<< HEAD
 q = int(a/b)  # value
 r = a%b       # remainder	
 print(str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r)) # printing the step
 while (r !=0): # doing more iterations until we have the GCD
=======
 q = int(a/b)
 r = a%b
 print(str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r))
 while (r !=0):
>>>>>>> 7449b180171681983dfba1af58b9c7e51c709f1e
  a = b
  b = r
  q = int(a/b)
  r = a%b
<<<<<<< HEAD
  print(str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r)) # printing step
 print ("The GCD is", b)
 print ("Type 'x' without the quotes to quit. Otherwise, you may continue")
 print("")
 return main()
=======
  print(str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r))
 print ("The GCD is ", b)
>>>>>>> 7449b180171681983dfba1af58b9c7e51c709f1e
 
  
main()
