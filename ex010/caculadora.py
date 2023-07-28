def calcular_percentual_gordura():
    idade = float(input("Digite sua idade em anos: "))
    subescapular = float(input("Digite o valor da dobra cutânea subescapular: "))
    triceps = float(input("Digite o valor da dobra cutânea tríceps: "))
    suprailiaca = float(input("Digite o valor da dobra cutânea suprailíaca: "))
    panturrilha_medial = float(input("Digite o valor da dobra cutânea panturrilha medial: "))

    D = 1.10726863 - 0.00081201 * (subescapular + triceps + suprailiaca + panturrilha_medial) + 0.00000212 * (subescapular + triceps + suprailiaca + panturrilha_medial) - 0.00041761 * idade

    percentual_gordura = (18 - (61 * D)) / 100
    return percentual_gordura

resultado_final = calcular_percentual_gordura()
print("Seu percentual de gordura corporal é:", resultado_final)