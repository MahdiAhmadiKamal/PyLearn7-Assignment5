# This function draws a rhombus with the rows of star.
# n = number of star rows

def rhombus (n):
    n=n-1

    for i in range (n+1):

        if i <= (n/2):
            print (end=(n-i)*" ")
            print ((2*i+1)*"*")
        if i > (n/2):
            print (end=i*" ")
            print ((2*(n-i)+1)*"*")

rhombus (11)