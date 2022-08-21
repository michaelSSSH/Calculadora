def bemVindo():
    print('''Bem vindo a calculadora''')

def calculate():
    operation = input('''
Por favor selecione um dos operadores matemático:
+ para adição
- para subtração
* para multiplicação
/ para divisão
** para potência
''')

    number_1 = int(input('Por favor adicione o primeiro número: '))
    number_2 = int(input('Por favor adicione o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não selecionou um operador válido. Por favor comece de novo.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Você deseja calcular novamente?
Por favor escolha S para SIM ou N for NÃO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('ATÉ MAIS TARDE!')
    else:
        again()

bemVindo()
calculate()