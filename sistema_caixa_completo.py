continuar = "s"

while continuar.lower().startswith("s"):
    valor = float(input("\nValor da Compra: R$ "))
    forma = input("Escolha a forma de Pagamento (1 - Pix, 2 - Débito, 3 - Crédito): ")

    if forma == "1":
        valor_final = valor * 0.85
        print(f"Sua compra teve 15% de desconto.")
        print(f"Valor Total: R$ {valor_final:.2f}")

    elif forma == "2":
        valor_final = valor * 0.95
        print(f"Sua compra teve 5% de desconto.")
        print(f"Valor Total: R$ {valor_final:.2f}")

    elif forma == "3":
        parcelas = int(input("Quantas parcelas? "))

        if parcelas == 1:
            print(f"Pagamento no crédito à vista.")
            print(f"Valor Total: R$ {valor:.2f}")

        elif parcelas > 1:
            total_com_juros = valor * 1.10
            valor_parcela = total_com_juros / parcelas

            print(f"Compra parcelada com 10% de juros.")
            print(f"Total com juros: R$ {total_com_juros:.2f}")
            print(f"{parcelas}x de R$ {valor_parcela:.2f}")

        else:
            print("Número de parcelas inválido.")

    else:
        print("Opção inválida.")

    continuar = input("\nDeseja realizar outra venda? (s/n) ")

print("Caixa fechado. Até amanhã!")