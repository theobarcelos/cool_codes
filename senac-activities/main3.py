class Livro:
    def __init__(self, titulo, autor, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.num_copias = num_copias

livro1 = Livro('Senhor dos Anéis', 'J. R. R. Tolkien', 14)
livro2 = Livro('A Sutil Arte de Ligar o F*da-se', 'Mark Manson', 0)
livro3 = Livro('Sobrevivendo no Inferno', "Racionais MC's", 1)

class Usuario:
    def __init__(self, nome, num_inscricao, livros_emprestados):
        self.nome = nome
        self.num_inscricao = int(num_inscricao)
        self.livros_emprestados = livros_emprestados

leitor1 = Usuario('Tiago', 4600, 1)
leitora1 = Usuario('Suzy', 1302, 0)
leitor2 = Usuario('João Vitor', 9301, 2)

class Emprestimo: 
    def __init__(self):
        ...
    def emprestar_livro():
        pergunta_num = input('Qual o seu número de inscrição? ')

        if pergunta_num == leitor1.num_inscricao:
            print(f'Bem-Vindo(a) de novo, {leitor1.nome}!')
            pergunta_livro = input('Qual livro você gostaria de pegar? ')
            if leitor1.livros_emprestados == 2:
                print('Você atingiu o limite de 2 livros por pessoa!')
            else: 
                if pergunta_livro == livro1.titulo:
                    if livro1.num_copias == 0:
                        print(f'Desculpe {leitor1.nome}, mas não possuímos nenhuma cópia de {livro1.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro1.num_copias} de unidades do livro {livro1.titulo}')
                        livro1.num_copias -= 1
                        leitor1.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitor1.nome}: {leitor1.livros_emprestados}')
                        print(f'Número de cópias de {livro1.titulo} restantes: {livro1.num_copias}')
                elif pergunta_livro == livro2.titulo:
                    if livro2.num_copias == 0:
                        print(f'Desculpe {leitor1.nome}, mas não possuímos nenhuma cópia de {livro2.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro2.num_copias} de unidades do livro {livro2.titulo}')
                        livro2.num_copias -= 1
                        leitor1.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitor1.nome}: {leitor1.livros_emprestados}')
                        print(f'Número de cópias de {livro2.titulo} restantes: {livro2.num_copias}')
                else:
                    if livro3.num_copias == 0:
                        print(f'Desculpe {leitor1.nome}, mas não possuímos nenhuma cópia de {livro3.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro3.num_copias} de unidades do livro {livro3.titulo}')
                        livro3.num_copias -= 1
                        leitor1.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitor1.nome}: {leitor1.livros_emprestados}')
                        print(f'Número de cópias de {livro3.titulo} restantes: {livro3.num_copias}')
        elif pergunta_num == leitor2.num_inscricao:
            print(f'Bem-Vindo(a) de novo, {leitor2.nome}!')
            pergunta_livro = input('Qual livro você gostaria de pegar? ')
            if leitor2.livros_emprestados == 2:
                print('Você atingiu o limite de 2 livros por pessoa!')
            else: 
                if pergunta_livro == livro1.titulo:
                    if livro1.num_copias == 0:
                        print(f'Desculpe {leitor2.nome}, mas não possuímos nenhuma cópia de {livro1.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro1.num_copias} de unidades do livro {livro1.titulo}')
                        livro1.num_copias -= 1
                        leitor2.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitor2.nome}: {leitor2.livros_emprestados}')
                        print(f'Número de cópias de {livro1.titulo} restantes: {livro1.num_copias}')
                elif pergunta_livro == livro2.titulo:
                    if livro2.num_copias == 0:
                        print(f'Desculpe {leitor2.nome}, mas não possuímos nenhuma cópia de {livro2.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro2.num_copias} de unidades do livro {livro2.titulo}')
                        livro2.num_copias -= 1
                        leitor2.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitor2.nome}: {leitor2.livros_emprestados}')
                        print(f'Número de cópias de {livro2.titulo} restantes: {livro2.num_copias}')
                else:
                    if livro3.num_copias == 0:
                        print(f'Desculpe {leitor2.nome}, mas não possuímos nenhuma cópia de {livro3.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro3.num_copias} de unidades do livro {livro3.titulo}')
                        livro3.num_copias -= 1
                        leitor2.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitor2.nome}: {leitor2.livros_emprestados}')
                        print(f'Número de cópias de {livro3.titulo} restantes: {livro3.num_copias}')
        elif pergunta_num == leitora1.num_inscricao:
            print(f'Bem-Vindo(a) {leitora1.nome}!')
            pergunta_livro = input('Qual livro você gostaria de pegar? ')
            if leitora1.livros_emprestados == 2:
                print('Você atingiu o limite de 2 livros por pessoa!')
            else: 
                if pergunta_livro == livro1.titulo:
                    if livro1.num_copias == 0:
                        print(f'Desculpe {leitora1.nome}, mas não possuímos nenhuma cópia de {livro1.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro1.num_copias} de unidades do livro {livro1.titulo}')
                        livro1.num_copias -= 1
                        leitora1.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitora1.nome}: {leitora1.livros_emprestados}')
                        print(f'Número de cópias de {livro1.titulo} restantes: {livro1.num_copias}')
                elif pergunta_livro == livro2.titulo:
                    if livro2.num_copias == 0:
                        print(f'Desculpe {leitora1.nome}, mas não possuímos nenhuma cópia de {livro2.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro2.num_copias} de unidades do livro {livro2.titulo}')
                        livro2.num_copias -= 1
                        leitora1.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitora1.nome}: {leitora1.livros_emprestados}')
                        print(f'Número de cópias de {livro2.titulo} restantes: {livro2.num_copias}')
                else:
                    if livro3.num_copias == 0:
                        print(f'Desculpe {leitora1.nome}, mas não possuímos nenhuma cópia de {livro3.titulo} no momento!')
                    else:
                        print(f'Possuímos {livro3.num_copias} de unidades do livro {livro3.titulo}')
                        livro3.num_copias -= 1
                        leitora1.livros_emprestados += 1
                        print(f'Número de livros pegos por {leitora1.nome}: {leitora1.livros_emprestados}')
                        print(f'Número de cópias de {livro3.titulo} restantes: {livro3.num_copias}')
        else:
            print(f'Não possuímos nenhum número de identificação {pergunta_num} em nosso banco de dados!')

print(Emprestimo.emprestar_livro())