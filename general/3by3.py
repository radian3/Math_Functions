a = int(input("Put in a: "))
b = int(input("Put in b: "))
c = int(input("Put in c: "))
j = int(input("Put in j: "))
d = int(input("Put in d: "))
e = int(input("Put in e: "))
f = int(input("Put in f: "))
k = int(input("Put in k: "))
g = int(input("Put in g: "))
h = int(input("Put in h: "))
i = int(input("Put in i: "))
m = int(input("Put in m: "))



r = e-(d*b/a)
s = f-(d*c/a)
A = k-(d*j/a)
B = h-(g*b/a)
R = i-(g*c/a)
Q = m-(g*j/a)
z = (Q-(B*A/r))/(R-(B*s/r))
y = (A/r)-(s*z/r)
x = (j/a)-(b*y/a)-(c*z/a)

print(x, y, z)
flag = 0
if (abs((a*x+b*y+c*z)-j)<0.1):
 if (abs((d*x+e*y+f*z)-k)<0.1):
  if (abs((g*x+h*y+i*z)-m)<0.1):
   flag = 1
if (flag == 1):
 print("Worked")
else:
 print("Didn't work")
   
