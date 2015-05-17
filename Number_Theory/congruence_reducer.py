def reducer():
 a = int(input("Put in your result: "))
 b = int(input("Put in modulus: "))

 print (a-(a//b)*b)

 return reducer()
reducer()
