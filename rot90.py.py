
input_matrix = [[1,2,3,],[4,5,6,]  ,[7,8,9,]]
# n=nt(input("number of rows"))
l=len(input_matrix)
n = len(input_matrix)
def rot90():
    input_matrix.reverse()
    for i in range(n):
        for j in range(i):
            input_matrix[i][j], input_matrix[j][i] = input_matrix[j][i],input_matrix[i][j]
    return input_matrix
#print(input_matrix)
print(rot90())



