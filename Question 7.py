print("Anas Ahmed")
print("18B-116-CS(A)")
print("Lab - 04")
print("Programming Ex: 7")
print("Matrix Multiplication")

matrix1 = [[row*col for col in range(1,4)] for row in range(1,4)]
matrix2 = [[row+col for col in range(1,4)] for row in range(1,4)]
mul     = [[0 for col in range(1,4)] for row in range(1,4)]
print("\nMatrix1",end=":")    
for row in range(3):
    print("\n",end="")
    for col in range(3):
        print(matrix1[row][col],end=" ")           
print("\nMatrix2",end=":")        
for row in range(3):
    print("\n",end="")
    for col in range(3):
        print(matrix2[row][col],end=" ")                          
for row in range(3):
    for col in range(3):
        for r in range(3):
            x= matrix1[row][r]*matrix2[col][r]
            mul[row][col] = mul[row][col]+x            
print("\n\nMultiplaction of Matrix1 and Matrix2",end=":")        
for row in range(3):
    print("\n",end="")
    for col in range(3):
        print(mul[row][col],end=" ")            
