def perevod_v_desyatichnuy_iz_luboi():
    chislo = input('Пожалуйста укажите число\n')
    chislo = list(chislo)
    sistema_scheta = int(input('Пожалуйста укажите систему в которой находится число\n'))
    znak = len(chislo) - 1
    resultat = 0
    for i in range(len(chislo)):
        if chislo[i] == 'A':
            chislo[i] = '10'
        elif chislo[i] == 'B':
            chislo[i] = '11'
        elif chislo[i] == 'C':
            chislo[i] = '12'
        elif chislo[i] == 'D':
            chislo[i] = '13'
        elif chislo[i] == 'E':
            chislo[i] = '14'
        elif chislo[i] == 'F':
            chislo[i] = '15'
        resultat += int(chislo[i]) * (sistema_scheta ** znak)
        znak -= 1
    print(resultat)


def perevod_iz_desyatichnoi_v_lubuiy():
    chislo = int(input('Пожалуйста укажите число\n'))
    perevod = int(input('пожалуйста укажите в какую систему счисления хотите перевести\n'))
    alf = 'ABCDEF'
    resultat = ''
    while chislo != 0:
        res = chislo % perevod
        if res < 10:
            resultat += str(res)
        else:
            resultat += alf[res - 10]
        chislo //= perevod
    print(resultat[::-1])


question = input('Добро пожаловать в перевод чисел.Пожалуйста выберете'
                 ' что вы хотите сделать(1-перевод в десятичную из '
                 'любой,2-перевод из десятичной в любую)\n')
if question == '1':
    perevod_v_desyatichnuy_iz_luboi()
elif question == '2':
    perevod_iz_desyatichnoi_v_lubuiy()
