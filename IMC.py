def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3" 
def main():
    print("Calculadora de IMC")
    while True:
        nome = input("\nDigite seu nome (ou digite 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            print("Encerrando a calculadora. Até logo!")
            break

        try:
            peso_str = input("Digite seu peso (em kg) e press enter: ").replace(',', '.')
            altura_str = input("Digite sua altura (em metros) e press enter: ").replace(',', '.')

            peso = float(peso_str)
            altura = float(altura_str)

            if peso <= 0 or altura <= 0:
                print("Peso e altura devem ser valores maiores que zero. Tente novamente.")
                continue

            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)

            print(f"\n{nome}, seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}")

        except ValueError:
            print("Por favor, insira valores numéricos válidos para peso e altura em Kg e em metros.")

if _name_ == "_main_":
    main()
