
# m = number of rows
# n = number of columns
# This function makes an m x n checkered board.

def checkered (m, n):



    for i in range (m):

        if i % 2 == 0:
            print ("")
            for j in range (n):
                if j % 2 == 0:
                    print ("#", end=" ")
                if j % 2 > 0:
                    print ("*", end=" ")
        else: 
            print ("")
            for k in range (n):
                if k % 2 == 0:
                    print ("*", end=" ")
                if k % 2 > 0:
                    print ("#", end=" ")

checkered (5,10)