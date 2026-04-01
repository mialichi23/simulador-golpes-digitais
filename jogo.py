import random


def mostrar_titulo():
    print("\n=== Simulador de Golpes Digitais ===")
    print("Leia cada mensagem e responda se ela é 'golpe' ou 'seguro'.")


def obter_resposta():
    while True:
        resposta = input("Essa mensagem é 'golpe' ou 'seguro'? ").strip().lower()
        if resposta in ["golpe", "seguro"]:
            return resposta
        print("Digite apenas 'golpe' ou 'seguro'.")


def jogar_rodada(casos):
    pontuacao = 0
    numero = 1
    casos_embaralhados = casos[:]
    random.shuffle(casos_embaralhados)

    for caso in casos_embaralhados:
        print(f"\nMensagem {numero}:")
        print(caso["texto"])

        resposta_usuario = obter_resposta()
        print()

        if resposta_usuario == caso["resposta"]:
            print("Resposta correta.")
            pontuacao += 1
        else:
            print("Resposta incorreta.")

        print("Explicação:", caso["explicacao"])
        print("-" * 50)

        numero += 1

    return pontuacao


def mostrar_resultado(pontuacao, total):
    print("\n=== Resultado Final ===")
    print(f"Você acertou {pontuacao} de {total} perguntas.")

    if pontuacao == total:
        print("Excelente desempenho.")
    elif pontuacao >= total / 2:
        print("Bom desempenho. Você demonstrou boa percepção de golpes digitais.")
    else:
        print("É recomendável revisar os principais sinais de fraude digital.")


def perguntar_novamente():
    while True:
        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if resposta in ["s", "n"]:
            return resposta
        print("Digite apenas 's' ou 'n'.")