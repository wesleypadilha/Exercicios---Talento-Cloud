def calculadora():
    while True:
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação desejada: ")

        if opcao == '0':
            print("Saindo da calculadora. Até logo!")
            break
        elif opcao in {'1', '2', '3', '4'}:
            try:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue

            if opcao == '1':
                resultado = num1 + num2
                print(f"Resultado: {resultado}")
            elif opcao == '2':
                resultado = num1 - num2
                print(f"Resultado: {resultado}")
            elif opcao == '3':
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
            elif opcao == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")
                else:
                    print("Não é possível dividir por zero. Tente novamente.")
        else:
            print("Essa opção não existe. Tente novamente.")

if __name__ == "__main__":
    calculadora()
