#Informações necessárias para a criação do boletim
nome = str(input('Digite seu nome completo:  '))
matricula = str(input('Digite sua matrícula: '))
turma = str(input('Digite sua turma: ' ))
mf = 0
soma = 0
m1 = 'Matemática'
m2 = 'Portugues'
m3 = 'História'
m4 = 'Geografia'
m5 = 'Biologia'
m6 = 'Química'
m7 = 'Ingles'
m8 = 'Fisica'
listadm = [m1, m2, m3, m4, m5, m6, m7, m8]
print('_' *10)
print(m1, '|')
print('_'*40)
for b in range (1, 5):
    notasm = float(input('Nota do {}°bimestre: '.format(b)))
soma += notasm
mf = soma / 4  
print(mf)
print('_' *10)
print(m2, '|')       
for c in range (1, 5):
    notasp = float(input('Nota do {}°bimestre: '.format( c)))
print('_' *10)
print(m3, '|')  
for di in range (1, 5):
    notash = float(input('Nota do {}°bimestre: '.format(di)))
print('_' *10)
print(m4, '|')    
for e in range (1, 5):
    notasg = float(input('Nota do {}°bimestre: '.format(e)))
print('_' *10)
print(m5, '|')    
for f in range (1, 5):
    notasb = float(input('Nota do {}°bimestre: '.format(f)))
print('_' *10)
print(m6, '|')      
for g in range (1, 5):
    notasq = float(input('Nota do {}°bimestre: '.format(g)))
print('_' *10)
print(m7, '|')  
for h in range (1, 5):
    notasi = float(input('Nota do {}°bimestre: '.format(h)))
print('_' *10)
print(m8, '|')  
for i in range (1, 5):
    notasf = float(input('Nota do {}°bimestre: '.format(i))) 
print('Aqui está o seu boletim: ')    
print('_' * 67)
#Informações do aluno
print ('  MATRÍCULA     |       NOME      |     TURMA   |    VERIFICAÇÃO' ) 
print('_' * 67)
print ('    ', matricula    ,       '  |',   nome              , '    |', turma   ,          '|    4bim     ' ) 
print('_' * 67)
#matérias
print ('  DISCIPLINAS  |  1° Bim |   2° Bim  |  3° Bim  |  4° Bim | Total  ' ) 
print('_' * 67)
#Notas de Matematica
print ('   ',listadm[0], '|')
print ('_' * 67)
#Notas de Portugues
print ('   ',listadm[1], ' |')
print ('_' * 67)
#Notas de História
print ('   ',listadm[2], '  |')
print ('_' * 67)
#Notas de Geografia
print ('   ',listadm[3], ' |')
print ('_' * 67)
#Notas de Biologia
print ('   ',listadm[4], '  |')
print ('_' * 67)
#Notas de Quimica
print ('   ',listadm[5], '   |')
print ('_' * 67)
#Notas de Ingles
print ('   ',listadm[6], '    |')
print ('_' * 67)
#Notas de Física
print ('   ',listadm[7], '    |')
print ('_' * 67)