cor = input("Digite a cor do semáforo (vermelho, amarelo ou verde): ").lower()

if cor == "vermelho":
    print("Pare!")
elif cor == "amarelo":
    print("Atenção!")
elif cor == "verde":
    print("Siga!")
else:
    print("Cor inválida. Digite vermelho, amarelo ou verde.")
