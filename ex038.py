num1 = int(input(' Primeiro número: '))
num2 = int(input(' Segundo número: '))
if num1 > num2:
    print('O \033[34mPRIMEIRO\033[m valor é maior.')
elif num2 > num1:
    print('O \033[31mSEGUNDO\033[m valor é maior.')
elif num1 == num2:
    print('Não existe valor maior, os dois são \033[33mIGUAIS\033[m.')