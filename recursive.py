## defining power function
def power(x,n):
    ## if n is 1 i.e same number power to 1
    if(n==1):
        ## so returns base value
        return(x)
    ## if n is other than one
    elif(n!=1):
        ## in return statment it is calling itself power() function
        return(x*power(x,n-1))

x=float(input("Enter base Number (x): "))
while True:
    ## loop runs until user enters positive number
    n=float(input("Enter exponential value (n): "))
    if n >= 1:
        ## once positive number is received loop breaks value sent to power() function
        break
result = power(x,n)
## using round function result number will round to 4 digits
print("Result:",round(result,4))