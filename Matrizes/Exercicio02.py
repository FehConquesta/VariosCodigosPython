# Criando a lista A com 10 elementos
A = []
for i in range(10):
  elemento = int(input(f"Digite o {i+1}º elemento da lista A: "))
  A.append(elemento)

# Criando a matriz C com três colunas
C = []
for i in range(len(A)):
  C.append([A[i]+5, 3*A[i], A[i]**2])

# Mostrando os elementos da matriz C
print("Matriz C:")
for i in range(len(C)):
  print(C[i])
