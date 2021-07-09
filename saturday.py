import random
import sys



file = open('fox.txt').read().strip()
text = file.split()



def logic():
    for i in text:
        if len(i) > 4:
            short = (i[1:-1:1])
            l = list(short)
            random.shuffle(l)
            result = ''.join(l)
            replaced = i.replace(short, result)
            #генерирую рандомный порядок и вставляю вместо обыкновенного порядка
            print(replaced, end = ' ')
        else:
            print(i, end = ' ')
            #применение к словам состоящим из 4-х и меньше букв
    return logic


#вывод в другой файл
# with open('output.txt', 'w') as outfile:
#     outfile.write(f'{logic()}')
#блок кода сверху выводит <function logic at 0x7fb3229a2ee0>
sys.stdout = open('output.txt', 'w')
logic()
sys.stdout.close()
