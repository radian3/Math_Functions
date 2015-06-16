def main():
 totalPercent = 0
 totalPoints = 0
 assignmentType = 1
 assignmentValue = 0
 assignmentNumber = 0
 assignmentPoints = 0
 while (totalPercent < 100):
  percent = int(input("Put in the percent value of assignments of type " + str(assignmentType) + ": "))
  assignmentType += 1
  totalPercent+=percent              
  while (True):
    assignmentValue = int(input("Put in your grade on assignment " + str(assignmentNumber+1) + ": "))
    if (assignmentValue == -1):
        break
    assignmentPoints += assignmentValue
    assignmentNumber += 1
  totalPoints += percent*(assignmentPoints/assignmentNumber)/100
  assignmentNumber = 0
  assignmentValue = 0
  assignmentPoints = 0
 print("Your final grade is " + str(totalPoints))                         
                          
 






main()
