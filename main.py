import random
from casos import casos


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

    for caso in casos:
        print(f"\n📩 Mensagem {numero}:")
        print(f"> {caso['texto']}")

        resposta_usuario = obter_resposta()
        print()

        if resposta_usuario == caso["resposta"]:
            print("✅ Resposta correta!")
            pontuacao += 1
        else:
            print("❌ Resposta incorreta.")

        print("Explicação:", caso["explicacao"])
        print("-" * 50)

        numero += 1
        
    return pontuacao


def mostrar_resultado(pontuacao, total):
    print("\n=== Resultado Final ===")
    print(f"Você acertou {pontuacao} de {total} perguntas.")

    if pontuacao == total:
        print("Excelente! Você identificou todos os sinais corretamente.")
    elif pontuacao >= 3:
        print("Muito bem! Você tem boa percepção de golpes digitais.")
    else:
        print("Atenção! Vale revisar os principais sinais de fraude digital.")

def main():
    while True:
        random.shuffle(casos)

        mostrar_titulo()
        pontuacao = jogar_rodada(casos)
        mostrar_resultado(pontuacao, len(casos))

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != "s":
            print("Até a próxima!")
            break


if __name__ == "__main__":
    main()
 
