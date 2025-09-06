from time import sleep

def calculadora(a,b,operacao):
    if operacao == 1:
        return a + b
    elif operacao == 2:
        return a - b
    elif operacao == 3:
        return a * b
    elif operacao == 4:
        if b != 0:
            return a / b
        else:
            return '\033[31mERRO:DIVISÃO POR ZERO\033[m'
        
print(f"\033[33m{'CALCULADORA':*^40}\033[m")
opcao = 0
while opcao != 5:
    print("""[ 1 ] SOMAR
[ 2 ] SUBTRAIR
[ 3 ] MULTIPLICAR
[ 4 ] DIVIDIR
[ 5 ] SAIR""")
    opcao = int(input('\033[1;4mEscolha uma opção: \033[m'))

    if 1 <= opcao <= 4:
        a = int(input('\033[33mDigite o 1º valor: \033[m'))
        b = int(input('\033[33mDigite o 2º valor: \033[m'))
        resultado = calculadora(a,b,opcao)
        print(f'RESULTADO: \033[35m{resultado}\033[m')
        print('-='*15)
    elif opcao == 5:
        print('\033[36mFINALIZANDO...\033[m')
        sleep(1.5)
    else:
        print('\033[31mOpção inválida. Tente novamente!\033[m')
        print('-='*15)
print('\033[36mFIM! VOLTE SEMPRE!\033[m')






    