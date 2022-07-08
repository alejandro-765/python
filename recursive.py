## defining power function
def power(x,n):
    ## if n is 1 i.e same number power to 1
elif(n!=1):
        ## in return statment it is calling itself power() function
        return(x*power(x,n-1))

x=float(input("Enter base Number (x): "))
while True:
    ## loop runs until user enters positive number
    n=float(input("Enter exponential value (n): "))
    if n >= 1: