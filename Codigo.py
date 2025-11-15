
while True:
    print("\n=== Calculadora de Média Escolar ===")
    materia = input("Digite o nome da matéria: ")

    # Pede o período atual (de 1 a 4)
    periodo = int(input("Você está em qual período (1 a 4)? "))

    # Cria uma lista para guardar as notas já obtidas
    notas = []
    for i in range(1, periodo + 1):
        nota = float(input(f"Digite a nota do {i}º período: "))
        notas.append(nota)

    # Calcula os totais
    total = sum(notas)
    faltam = 24 - total

    print("\n=== Resultado ===")
    print(f"Matéria: {materia}")
    print(f"Período atual: {periodo}º")
    print(f"Total de pontos obtidos: {total:.1f}")

    if faltam <= 0:
        print(" Parabéns! Você já atingiu os 24 pontos e passou!")
    else:
        print(f" Ainda faltam {faltam:.1f} pontos para atingir os 24 necessários.")
        periodos_restantes = 4 - periodo
        if periodos_restantes > 0:
            media_necessaria = faltam / periodos_restantes
            print(f"Você precisa tirar em média {media_necessaria:.1f} pontos nos próximos {periodos_restantes} períodos.")
        else:
            print(" Todos os períodos já foram concluídos.")

    # Pergunta se deseja continuar
    repetir = input("\nDeseja calcular outra matéria? (s/n): ").strip().lower()
    if repetir != 's':
        print("\nEncerrando o programa... Até a próxima! ")
        break