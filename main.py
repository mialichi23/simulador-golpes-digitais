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


casos = [
    {
        "texto": "Seu banco detectou atividade suspeita. Clique no link para desbloquear sua conta: bit.ly/seguranca123",
        "resposta": "golpe",
        "explicacao": "Links encurtados, urgência e pedido de ação imediata são sinais comuns de golpe."
    },
    {
        "texto": "Olá, Maria. Sua consulta está confirmada para amanhã às 14h. Clínica Vida. Em caso de dúvidas, ligue para nosso número oficial.",
        "resposta": "seguro",
        "explicacao": "A mensagem informa dados objetivos, sem pedir senha, clique em link suspeito ou transferência."
    },
    {
        "texto": "Parabéns! Você ganhou um prêmio de R$ 5.000. Para receber, envie seu CPF e dados bancários agora.",
        "resposta": "golpe",
        "explicacao": "Promessa de prêmio, urgência e solicitação de dados pessoais são sinais clássicos de fraude."
    },
    {
        "texto": "Seu código de verificação é 482913. Não compartilhe esse código com ninguém.",
        "resposta": "seguro",
        "explicacao": "É uma mensagem comum de autenticação, sem link suspeito e com aviso de segurança."
    },
    {
        "texto": "Mãe, troquei de número. Me chama aqui urgente e faz um PIX para mim porque estou sem acesso ao banco.",
        "resposta": "golpe",
        "explicacao": "Golpistas usam urgência, vínculo emocional e pedido de dinheiro imediato para enganar."
    }
]


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

