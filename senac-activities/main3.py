class Livro:
    def __init__(self, titulo, autor, numcop):
        titulo = input("Insira o título do livro: ")
        autor = input("Insira o nome do(a) autor(a): ")
        numcop = int(input("Insira o número de cópias: "))

        self.titulo = titulo
        self.autor = autor
        self.numcop = numcop
