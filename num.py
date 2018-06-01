import numpy

a = numpy.array([10, 20, 30, 40])
mat1 = numpy.array([[1,2],[3,4]])
mat2 = numpy.array([[5,6],[7,8]])
mat3 = numpy.array([1,2,3,4])

print(mat1[1][1])
print(mat1[1,:]) # Exibe a segunda linha da matriz
print(mat1[:,0]) # Exibe a primeira coluna da matriz
print(mat1.transpose()) #transforma linhas em colunas

print(mat1+mat2)
print(mat1-mat2)
print(mat1*mat2)

print(mat3.sum())
print(mat3.argmax())
print(mat3.argmin())

l = [20, 30, 10, 40]

print(l[1:3]) # Intervaloe entre 1 e 3

print(l[::2]) # somente o inicial e o 2

l2 = l[:] # Faz uma cópia de l para l2
l2[0] = 1000 # Atribui o valor 1000

print(l)
print(l2)

b = a.copy() # Para copiar o array a para o b