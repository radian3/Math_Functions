

def simp():
 x = -1   
 a = int(input("Put in your constant: "))
 b = int(input("Put in modulus: "))
 for i in range (1, 1000):
  val = a**i
  reducedval = (val-(val//b)*b) 
  if (reducedval == 1):
      x = i
      break
 print ("The order is ", x)
 return simp()
simp()
