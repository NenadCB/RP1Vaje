from random import randint

while True:
    faktorA = randint(1, 10)
    faktorB = randint(1, 10)  

    pravilenRezultat = faktorA * faktorB

    mojOdgovor = input(f'koliko je {faktorA} * {faktorB} = ')

    if mojOdgovor.upper() == 'Q' or mojOdgovor == '':
        break
        
    if pravilenRezultat == int(mojOdgovor):
        print('ODLIČNO! Le tako naprej.')
    else:
        print(f'Pravilen odgovor je {pravilenRezultat}.')
