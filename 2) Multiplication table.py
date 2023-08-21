# m = number of rows
# n = number of columns
# This function makes an m x n multiplication table.
            
def multi_table (m, n):

    count = 1

    for i in range (n+1):
        print ('\033[2m' + str(i) + '\033[0m', end=" ")

    while count <= m:
        print ("")
        for i in range (n+1):
            if i==0:
                print ('\033[2m' + str(count) + '\033[0m', end=" ")
            else:
                ans = i * (count)
                print (ans, end=" ")
                
        count = count+1

multi_table (10, 10)