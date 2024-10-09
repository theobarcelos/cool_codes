class Livro:
    def __init__(self, titulo, autor, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.num_copias = num_copias

livro1 = Livro('Senhor dos Anéis', 'J. R. R. Tolkien', 14)
livro2 = Livro('A Sutil Arte de Ligar o F*da-se', 'Mark Manson', 0)
livro3 = Livro("Sobrevivendo no Inferno', 'Racionais MC's", 1)

class Usuario:
    def __init__(self, nome, num_inscricao, livros_emprestados):
        self.nome = nome
        self.num_inscricao = num_inscricao
        self.livros_emprestados = livros_emprestados

leitor1 = Usuario('Tiago', 4600, 1)
leitora1 = Usuario('Suzy', 1302, 0)
leitor2 = Usuario('João Vitor', 9301, 2)

class Emprestimo: 
    def __init__(self):
        ...
    def emprestar_livro():
        pergunta_livro = input('Qual livro você gostaria de pegar? ')
        pergunta_num = input('Qual o seu número de inscrição? ')

        if pergunta_num == Usuario.num_inscricao:
            if pergunta_livro == Livro.titulo:
                if Livro.num_copias == 0:
                    print(f'Desculpe {Usuario.nome}, mas não possuímos nenhuma cópia de {Livro.titulo} no momento!')
                elif Usuario.livros_emprestados == 2:
                    print('Você atingiu o limite de 2 livros por pessoa!')
                else:
                    print(f'Possuímos {Livro.num_copias} de unidades do livro {Livro.titulo}')
                    Livro.num_copias -= 1
                    Usuario.livros_emprestados += 1
                    pergunta_crucial = input('Você gostaria de adquirir outro de nossos livros?')
                    if Usuario.livros_emprestados == 2:
                        print('Você atingiu o limite de 2 livros por pessoa!')
                    else:
                        if Livro.num_copias == 0:
                            print('Parabéns! Você pegou a última unidade do livro para alugar. Que sorte!')
                        else: 
                            print(f'Ainda resta(m) {Livro.num_copias} de unidades do livro. Gostaria de pegar mais uma?')
            else:
                print('Foi mal! Não possuímos este livro em nosso catálogo!')
        else:
            print(f'Não possuímos nenhum número de identificação {Usuario.num_inscricao} em nosso banco de dados!')

