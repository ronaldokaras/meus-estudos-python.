valor = float(input("Valor da Compra: R$ "))
forma = input("Escolha a forma de Pagamento (1 - Pix, 2 - Débito, 3 - Crédito):")

if forma == "1":
    valor_final = valor * 0.85
    print(f"Sua compra teve um desconto de 15%\nValor Total: {valor_final:.2f}")

elif forma == "2":
    valor_final = valor * 0.95 
    print(f"Sua compra teve um desconto de 5%\nValor Total: {valor_final:.2f}")

elif forma == "3":
    parcelas = int(input("Quantas parcelas? "))
    if parcelas == 1:
       print(f"Sua compra ficou: R$ {valor:.2f}")
    else:
        total_com_juros = valor * 1.10
        valor_da_parcela = total_com_juros / parcelas
        print(f"Compra parcelada com 10% de juros.\nVocê parcelou sua compra em {parcelas}x e cada parcela ficou: R$ {valor_da_parcela:.2f} por parcela")

else:
    print("Opção Invalida") 
