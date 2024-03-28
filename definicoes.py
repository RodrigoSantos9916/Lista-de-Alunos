notas = {} # dicionário para armazenar as notas dos alunos
def add_aluno(): #adiciiona nota do aluno
    nome = input('Digite o Nome do Aluno:\n').title()
    notas[nome] = []


def add_nota(): #adiciona a nota do aluno
    nome = input("Digite o nome do aluno:\n").title()

    if nome in notas:
        nota = float(input("Nota do Aluno:\n"))
        notas[nome].append(nota)

    else:
        print("Aluno não encontrado")
        op = input("Deseja adicioná-lo(a)? (S/N)\n").upper()

        if op == 'S':
            add_aluno()
            nota = float(input("Nota do Aluno:\n"))
            notas[nome].append(nota)


def alterNota():
    nome = input("Nome do aluno:\n").title()
    if nome in notas:
        nova_nota = float(input("Digite a nova nota:\n"))
        notas[nome] = [nova_nota]
        print(f"Nota do aluno {nome} alterada para {nova_nota}")
    else:
        print('aluno não existente!')
    

def mediaAluno(): #calcula a média de um aluno
    nome = input('\nDigite o Nome do Aluno para ver a Média:\n').title()

    if nome in notas:
        nt = sum(notas[nome]) / len(notas[nome])
        print(f'\nA média de {nome} é: {nt:.2f}')

    else:
        print("\nAluno não cadastrado!")


def medias_todos_alunos():  #mostra a média de todos os alunos
    soma = 0
    total_alunos = len(notas)

    for aluno, notas_aluno in notas.items():
        soma += sum(notas_aluno)

    if total_alunos > 0:
        media_geral = soma / total_alunos
        print(f"\nMédia Geral das Notas dos Alunos Cadastrados: {media_geral:.2f}")

    else:
        print("\nNenhum aluno cadastrado!")


def excluirAluno(): #exclui um aluno
    nome = input("Digite o nome do alunos que deseja excluir:\n").title()

    if nome in notas:
        del notas[nome]
        print(notas.keys())

    else:
        print('Aluno não encontrado!')


def lista_alunos(): #lista todos os alunos cadastrados
    print(list(notas.keys()))


def lista_alunos_e_notas(): #lista todos os alunos e suas respectivas notas
    print(notas)


def limpar_lista():  #limpa a lista de alunos e as notas
    notas.clear()
    print('lista apagada com sucesso')