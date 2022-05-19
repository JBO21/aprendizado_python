import random

desenho_forca = ["""
|=====
|     +
|
|
|
|________
""", """
|=====
|     +
|     0  
|
|
|________
""", """
|=====
|     +
|     0
|     |
|
|________
""", """
|=====
|     +
|     0
|    /|
|
|________
""", """
|=====
|     +
|     0
|    /|\\
|
|________
""", """
|=====
|     +
|     0
|    /|\\
|    /
|________
""","""
|=====
|     +
|     0
|    /|\\
|    / \\
|________
"""]

class Forca:

    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []

    def advinhar(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    def fimdejogo(self):
        return self.vitoria_forca() or (len(self.letras_erradas) == 6)

    def vitoria_forca(self):
        if '_' not in self.palavra_escondida():
            return True
        return False

    def palavra_escondida(self):
        word = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                word += '_'
            else:
                word += letra
        return word

    def statusgame (self):
        print(desenho_forca[len(self.letras_erradas)])
        print(f'\nPalavra: {self.palavra_escondida()}')
        print('\nLetras erradas: ',)
        for letra in self.letras_erradas:
            print(letra,)
        print()
        print('Letras certas: ',)
        for letra in self.letras_certas:
            print(letra,)
        print()

def busca_palavra():
    with open('basedados.txt', 'rt') as w:
        banco = w.readlines()
    return banco[random.randint(0, len(banco))].strip()

def main():
    game = Forca(busca_palavra())

    while not game.fimdejogo():
        game.statusgame()
        entrada_usuario = input('\nDigite uma letra: ')
        game.advinhar(entrada_usuario)

    game.statusgame()

    if game.vitoria_forca():
        print('\n\033[32mBoua! Você venceu!!!\033[m')
    else:
        print('\n\033[31mGanhou um ovo! Você perdeu!\033[m')
        print(f'A palavra correta é {game.palavra}')

    print('\nValeu!')

if __name__ == "__main__":
    main()
