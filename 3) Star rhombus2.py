# This function draws a rhombus with the rows of star.
# n = number of star rows

def rhombus (n):
    n=n+1

    for i in range (n):

        if i <= (n/2):
            print (end=(n-i)*" ")
            print (i*"* ")
        if i > (n/2):
            print (end=i*" ")
            print ((n-i)*"* ")

rhombus(11)