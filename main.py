import definicoes

while True:
    try:
        opcoes = int(input('Selecione a opção desejada:\n[1] Adicionar aluno:\n[2] Adicionar nota do aluno:\n[3] Editar Nota do Aluno\n[4] Ver média do aluno:\n[5] Ver médias de Todos os alunos:\n[6] Lista de Alunos\n[7] Lista de Alunos com Notas\n[8] Excluir aluno\n[9] Limpas Lista de Alunos\n[0] Sair\n'))
        if opcoes == 1:
            definicoes.add_aluno()
        elif opcoes == 2:
            definicoes.add_nota()
        elif opcoes == 3:
            definicoes.alterNota()
        elif opcoes == 4:
            definicoes.mediaAluno()
        elif opcoes == 5:
            definicoes.medias_todos_alunos()
        elif opcoes == 6:
            definicoes.lista_alunos()
        elif opcoes == 7:
            definicoes.lista_alunos_e_notas()
        elif opcoes == 8:
            definicoes.excluirAluno()
        elif opcoes == 9:
            definicoes.limpar_lista()
        elif opcoes == 0:
            break
    except ValueError as error:
        print(f'Opção Inválida! Erro: {error}')