from time import sleep
import emoji
print('A contagem começa em...')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks:'*40, language = 'alias'))
