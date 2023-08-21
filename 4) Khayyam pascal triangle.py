
n = int (input("enter the number of Khayyam pascal triangle rows: "))

arr = [[1]]

for i in range (n+1):
    
    if i > 1:
        arr.append(i*[1])

        for j in range (len(arr)):
            
            if j > 1:
        
                arr [i-1][j-1] =arr [i-2][j-2] + arr [i-2][j-1]

for row in arr:
    print(row)
