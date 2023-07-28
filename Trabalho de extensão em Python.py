print('Bem vindo ao programa de serviço de limpeza da Thais!')
print('*************************************************************************************')
print('--------------------------Menu 1 de 3 - Metragem e Limpeza---------------------------')


def metragem_limpeza():
    metragem = input("Entre com a metragem da casa: ")

    try:
        metragem = int(metragem)
        if metragem >= 30 and metragem < 300:
            print('Será necessário contratar um funcionário(a)')
        elif metragem >= 300 and metragem < 700:
            print('Será necessário contratar dois funcionários(as)')
        else:
            print('!!Não aceitamos metragem abaixo 30m² ou maior que 700m². Insira uma metragem válida!!')
            return metragem_limpeza()

        metragem = int(metragem)

        if 30 <= metragem < 300:
            valor_metragem = 60 + 0.3 * metragem
        else:
            valor_metragem = 120 + 0.5 * metragem
        return valor_metragem
    except:
        metragem_limpeza()

# função tipo de limpeza
def limpeza():
    multiplicador = 0

    while True:
        print('--------------------------Menu 2 de 3 - Tipo de Limpeza---------------------------')
        tipo = input('Qual o tipo de limpeza será feita?\n'
                    'B - Básica - Indicada para sujeiras semanais ou quinzenais\n'
                    'C - Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras')

    # determina o tipo de limpeza de forma que selecione tanto em maísculo quanto em minúsculo
        if tipo == "B".lower():
            multiplicador = 1.00
            print('Você selecionou a limpeza básica')
            break
        elif tipo == "C".lower():
            print('Você selecionou a lempeza completa')
            multiplicador = 1.30
            break
        else:
            print('!!Opção Inválida!!')

    return multiplicador


# tabela adicionais
tipos_adicional = {0: "Não desejo mais nada (encerrar)",
                   1: "Passar 10 peças de roupas - R$ 10.00",
                   2: "Limpeza de 1 Forno/Micro-ondas - R$ 12,00",
                   3: "Limpeza de 1 Geladeira/Freezer - R$ 20,00"}

valor_adicional = [0, 10.00, 12.00, 20.00]

# função adicional da limpeza
def adicional_limpeza():
    print('--------------------------Menu 1 de 3 - Adicional de Limpeza---------------------------')
    print("Digite o número do adicional que deseja. ")

    for key in tipos_adicional:
        print("{}- {}".format(key, tipos_adicional[key]))
    adicional = int(input())

    if adicional == 0:
        return 0
    elif adicional in tipos_adicional and adicional <= len(valor_adicional):
        return valor_adicional[adicional]
    else:
        return -1

# programa

total = 0

valor = metragem_limpeza()
tipo_limpeza = limpeza()
adicionais = 0
total_adicionais = 0
while True:
    adicionais = adicional_limpeza()

    if adicionais == 0:
        break

    if adicionais >= 0:
        total_adicionais += adicionais

total = (valor * tipo_limpeza) + total_adicionais

print(f"R$ {total:,.2f}")
