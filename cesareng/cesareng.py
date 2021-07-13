
def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()

def shifr():
    string_1 = input('Введите текст для зашифровки\n')
    # Day, mice. "Year" is a mistake!
    list_1 = string_1.split(' ')
    string_2 = ''
    for i in range(len(list_1)):
        count = 0
        for j in range(len(list_1[i])):
            if list_1[i][j].lower() in 'abcdefghijklmnopqrstuvwxyz':
                count += 1
        for j in range(len(list_1[i])):
            symbol_1 = list_1[i][j] # пробегаемся по каждой букве слова
            if symbol_1.lower() not in 'abcdefghijklmnopqrstuvwxyz':
                string_2 += symbol_1
                continue
            string_2 += sdvig(symbol_1, count)
        string_2 += ' '

    print(string_2)

shifr()



