from casos import casos
from jogo import (
    mostrar_titulo,
    jogar_rodada,
    mostrar_resultado,
    perguntar_novamente,
)


def main():
    while True:
        mostrar_titulo()
        pontuacao = jogar_rodada(casos)
        mostrar_resultado(pontuacao, len(casos))

        jogar_novamente = perguntar_novamente()
        if jogar_novamente != "s":
            print("Até a próxima.")
            break


if __name__ == "__main__":
    main()
 
