main <- function(p){
  a = dbinom(2, 2, p) # making 2 free throws after 2 attempts
  b = dbinom(1, 2, p) # making exactly 1 free throw
  c = dbinom(2, 2, p) + dbinom(1, 2, p) # at least 1 free throw
  d = dbinom(0, 2, p) #missing both
  print(paste("Statistics for two free-throws with free-throw probability", as.character(p)))
  print(paste("The probability of making both free-throws is", as.character(a)))
  print(paste("The probability of making exactly 1 free-throw is", as.character(b)))
  print(paste("The probability of making at least 1 free-throw is", as.character(c)))
  print(paste("The probability of missing both free-throws is", as.character(d)))
  print(paste("The expected points is", as.character(2*p)))
  print(paste("Equivalent 2 point FG probability needed for same expectation is", as.character(p)))
  print(paste("Equivalent 3 point FG probability needed for same expectation is", as.character(2*p/3)))
}