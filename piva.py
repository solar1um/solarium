import random
data = {
    'а': 'A',
    'б': 'b',
    'в': 'B',
    'г': 'r',
    'д': 'g',
    'e': 'e',
    'ё': 'e',
    'ж': 'JIL',
    'з': '3',
    'и': 'u',
    'й': 'u',
    'к': 'K',
    'л': 'JL',
    'м': 'm',
    'н': 'H',
    'о': 'o',
    'п': 'n',
    'р': 'p',
    'с': 'c',
    'т': 'T',
    'у': 'y',
    'ф': 'F',
    'х': 'X',
    'ц': 'U',
    'ч': '4',
    'ш': 'LLl',
    'щ': 'LLL',
    'ъ': 'b',
    'ы': 'bl',
    'ь': 'b',
    'э': '3',
    'ю': 'iO',
    'я': 'R'
}
piv_prepiski = ['strelok_', 'TANK_', 'tank_', 'tankist_', 'xaker_', 'Pro100_', 'VIP', 'MAHb9K_','TPAKTOP_', 'TPAKTOPUCT_', 'Bejlukuy_', 'CTAJLuH_']
inp = input()
year = random.randint(1960, 1992)
for i in inp:
    nickname = (data.get(i, i))
    print(nickname.replace(' ', '_',), end = '')
print('_' + str(year))