print('\033[34mOs números pares que estão no intervalo entre 1 e 50 são:\033[m ')
for n in range(2, 51, 2):
    print(n, end=' ')
# outra forma de escrever
#for n in range(1, 51):
  #  if n % 2 == 0:
   #    print(n, end=' ')