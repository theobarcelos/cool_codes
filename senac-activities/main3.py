class Livro:
    def __init__(self, titulo, autor, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.num_copias = num_copias

livro1 = Livro('Senhor dos Anéis', 'J. R. R. Tolkien', 14)
livro2 = Livro('A Sutil Arte de Ligar o F*da-se', 'Mark Manson', 0 )
livro3 = Livro()

class Usuario:
    def __init__(self, nome, num_inscricao, livros_emprestados):
        self.nome = nome
        self.num_inscricao = num_inscricao
        self.livros_emprestados = livros_emprestados

class Emprestimo: 
    def __init__(self, nome_emprest, livro_emprest):
        self.nome_emprest = nome_emprest
        self.livro_emprest = livro_emprest

    def emprestar_livro(self):
        nome