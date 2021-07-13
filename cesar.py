rus_alphabet = [1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088,
                1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103]

# 32 букв
def shifr():
    string_1 = input('Введите предложение для зашифровки\n')
    string_2 = ''
    key_1 = int(input('Введите ключ\n'))

    for i in range(len(string_1)):
        key_2 = ord(string_1[i]) + key_1
        if string_1[i] == ' ' or string_1[i] == '!' or string_1[i] == '.' or string_1[i] == ',':
            string_2 += string_1[i]
            continue
        word_1 = chr(key_2)
        string_2 += word_1

    print(string_2)

    question_1 = input('Если хотите продолжить, напишите "да"\n').lower()

    if question_1 == 'да':
        your_target = input(
            'Если хотите шифровать текст, нажмите "Ш", если хотите дешифровать текст, нажмите "Д"\n').lower()

        if your_target == 'ш':
            shifr()
        else:
            deshifr()

def deshifr():
    string_1 = input('Введите предложение для дешифровки\n')
    string_2 = ''
    key_1 = int(input('Введите ключ\n'))

    for i in range(len(string_1)):
        key_2 = ord(string_1[i]) - key_1
        if string_1[i] == ' ' or string_1[i] == '!' or string_1[i] == '.' or string_1[i] == ',':
            string_2 += string_1[i]
            continue
        word_1 = chr(key_2)
        string_2 += word_1

    print(string_2)

    question_1 = input('Если хотите продолжить, напишите "да"\n').lower()

    if question_1 == 'да':
        your_target = input(
            'Если хотите шифровать текст, нажмите "Ш", если хотите дешифровать текст, нажмите "Д"\n').lower()

        if your_target == 'ш':
            shifr()
        else:
            deshifr()

your_target = input('Если хотите шифровать текст, нажмите "Ш", если хотите дешифровать текст, нажмите "Д"\n').lower()

if your_target == 'ш':
    shifr()
else:
    deshifr()


