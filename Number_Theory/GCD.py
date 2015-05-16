def main():
 x = int(input("Put in x: "))
 y = int(input("Put in y: "))
 if (x > y):
    a = x
    b = y
 else:
     a = y
     b = x

 q = int(a/b)
 r = a%b
 print(str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r))
 while (r !=0):
  a = b
  b = r
  q = int(a/b)
  r = a%b
  print(str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r))
 print ("The GCD is ", b)
 
  
main()
