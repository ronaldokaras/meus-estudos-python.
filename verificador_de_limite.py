valor_compra = float(input("Digite o valor de sua compra: R$ "))

limite = 2500

if valor_compra <=limite:
    print(f"Compra Aprovado!\nLimite Restante: R$ {limite - valor_compra:.2f}")
else:
    print("Compra Negada por falta de Limite!")
    opcao = input(f"Deseja parcelar a compra com 5% de juros ? (sim ou não): ")

    if opcao.lower() == "sim":
        valor_final = valor_compra * 1.05
        print(f"Compra parcelada aprovada!\nValor com juros: R$ {valor_final:.2f}")
    else:
        print("Operação Cancelada!")
   