from bprettytale import PrettyTable
# Informações necessárias para a criação do boletim
print("\033[34m>>>>>>>>>>>CRIADOR DE BOLETIM<<<<<<<<<<\033[m")
print("Digite seus dados abaixo para ter acesso ao seu boletim:")
# SEQUÊNCIA
nome = str(input('Digite seu nome completo: '))
matricula = str(input('Digite sua matrícula: '))
turma = str(input('Digite sua turma: '))
# VARIÁVEIS DE SOMA
soma = 0
somap = 0
somah = 0
somag = 0
somab = 0
somaq = 0
somaf = 0
# VARIÁVEIS DE SITUAÇÃO
sit1 = ''
sit2 = ''
sit3 = ''
sit4 = ''
sit5 = ''
sit6 = ''
sit7 = ''
sitf = 'APROVADO'
# VARIÁVEIS DE MATÉRIAS
m1 = 'Matemática'
m2 = 'Portugues'
m3 = 'História'
m4 = 'Geografia'
m5 = 'Biologia'
m6 = 'Química'
m7 = 'Fisica'
listadm = [m1, m2, m3, m4, m5, m6, m7]
print('_' * 10)
# Começo das iterações que perguntarão a nota dos 4 bimestres de cada uma das matérias
# matemática
print(m1, '|')
print('_' * 40)
for b in range(1, 5):
   notasm = float(input('Nota do {}°bimestre: '.format(b)))
   soma += notasm
   media = soma/4
print(media)
print('_' * 10)
# portugues
print(m2, '|')
for c in range(1, 5):
    notasp = float(input('Nota do {}°bimestre: '.format(c)))
    somap += notasp
    mediap = somap / 4
print(mediap)
print('_' * 10)
# historia
print(m3, '|')
for di in range(1, 5):
    notash = float(input('Nota do {}°bimestre: '.format(di)))
    somah += notash
    mediah = somah / 4
print(mediah)
print('_' * 10)
# geografia
print(m4, '|')
for e in range(1, 5):
    notasg = float(input('Nota do {}°bimestre: '.format(e)))
    somag += notasg
    mediag = somag / 4
print(mediag)
print('_' * 10)
# biologia
print(m5, '|')
for f in range(1, 5):
    notasb = float(input('Nota do {}°bimestre: '.format(f)))
    somab += notasb
    mediab = somab / 4
print(mediab)
print('_' * 10)
# quimica
print(m6, '|')
for g in range(1, 5):
    notasq = float(input('Nota do {}°bimestre: '.format(g)))
    somaq += notasq
    mediaq = somaq / 4
print(mediaq)
print('_' * 10)
# fisica
print(m7, '|')
for i in range(1, 5):
    notasf = float(input('Nota do {}°bimestre: '.format(i)))
    somaf += notasf
    mediaf = somaf / 4
print(mediaf)
# FIM DAS ITERAÇÕES
print('Aqui está o seu boletim: ')
# matérias
# COMEÇO DAS SELEÇÕES DE CADA MATÉRIA
# Situação de Matematica
# Essa Seleção é responsável por decidir a situação de cada matéria, de acordo com as três condições abaixo:
if media >= 7:
    sit1 = 'APROVADO'
elif media == 0:
    sit1 = 'REPROVADO'
elif media < 7:
    sit1 = 'RECUPERAÇÃO'
# Situação de Portugues
# Seleção
if mediap >= 7:
    sit2 = 'APROVADO'
elif mediap == 0:
    sit2 = 'REPROVADO'
elif mediap < 7:
    sit2 = 'RECUPERAÇÃO'
# Situação de História
# Seleção
if mediah >= 7:
    sit3 = 'APROVADO'
elif mediah == 0:
    sit3 = 'REPROVADO'
elif mediah < 7:
    sit3 = 'RECUPERAÇÃO'
# Situação de Geografia
# Seleção
if mediag >= 7:
    sit4 = 'APROVADO'
elif mediag == 0:
    sit4 = 'REPROVADO'
elif mediag < 7:
    sit4 = 'RECUPERAÇÃO'
# Situação de Biologia
# Seleção
if mediab >= 7:
    sit5 = 'APROVADO'
elif mediab == 0:
    sit5 = 'REPROVADO'
elif mediab < 7:
    sit5 = 'RECUPERAÇÃO'
# Situação de Quimica
# Seleção
if mediaq >= 7:
    sit6 = 'APROVADO'
elif mediaq == 0:
    sit6 = 'REPROVADO'
elif mediaq < 7:
    sit6 = 'RECUPERAÇÃO'
# Situação de Física
# Seleção
if mediaf >= 7:
    sit7 = 'APROVADO'
elif mediaf == 0:
    sit7 = 'REPROVADO'
elif mediaf < 7:
    sit7 = 'RECUPERAÇÃO'
# RESULTADO f
# Seleção, essa sequência de decisões escolhe o resultado final do aluno, considerando os resultados das outras matérias
if media == 0:
    sitf = 'REPROVADO'
elif mediap == 0:
    sitf = 'REPROVADO'
elif mediah == 0:
    sitf = 'REPROVADO'
elif mediag == 0:
    sitf = 'REPROVADO'
elif mediab == 0:
    sitf = 'REPROVADO'
elif mediaq == 0:
    sitf = 'REPROVADO'
elif mediaf == 0:
    sitf = 'REPROVADO'
elif media < 7:
    sitf = 'RECUPERAÇÃO'
elif mediap < 7:
    sitf = 'RECUPERAÇÃO'
elif mediah < 7:
    sitf = 'RECUPERAÇÃO'
elif mediag < 7:
    sitf = 'RECUPERAÇÃO'
elif mediab < 7:
    sitf = 'RECUPERAÇÃO'
elif mediaq < 7:
    sitf = 'RECUPERAÇÃO'
#FIM DAS SELEÇÕES
#Criação da tabela para o boletim com a bibloteca Pretty Table
x = PrettyTable(["\033[31mMATRÍCULA", "NOME", "TURMA", "VERIFICAÇÃO\033[m"])
x.add_row([matricula, nome, turma, "4 bim"])
x.add_row(["\033[34mDisciplinas", "Média final", "TOTAL", "SITUAÇÃO\033[m"])
x.add_row([listadm[0], media, soma, sit1])
x.add_row([listadm[1], mediap, somap, sit2])
x.add_row([listadm[2], mediah, somah, sit3])
x.add_row([listadm[3], mediag, somag, sit4])
x.add_row([listadm[4], mediab, somab, sit5])
x.add_row([listadm[5], mediaq, somaq, sit6])
x.add_row([listadm[6], mediaf, somaf, sit7])
x.add_row(["Resultado final:", sitf, " ", " "])
print(x)




