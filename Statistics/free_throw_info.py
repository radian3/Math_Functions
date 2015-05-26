def main():

 p = int(input("Enter free-throw percentage (ex: 83): "))
 p = p/100
 q = 1-p
 print("For two free-throw shots:")
 print("Expectation = " + str((p)*2) + " points")
 print("Probability of making both free-throws = " + str(round(p**2, 2))) # p(y=2) = probability of making a FT * probability of making a FT
 print("Probability of missing both free-throws = " + str(round((q)**2, 2))) # p(y=0) = prob of missing a FT * prob of missing a FT
 print("Probability of making at least one free-throw = " + str(round(1-(q**2), 2))) #p(y>=1) = 1-p(0)
 print("Probability of making exactly one free-throw = " + str(round(2*p*q, 2))) # p*q + q*p with two ways to get it
 print("Equivalent 2 point FG% needed for same expectation: " + str(round(p, 2)))
 print("Equivalent 3 point FG% needed for same expectation: " + str(round(2*p/3, 2)))

 
 




main()
