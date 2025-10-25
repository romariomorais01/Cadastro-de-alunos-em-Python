import textwrap

# Dicionário para armazenar os alunos
alunos = {}

# Função do menu
def menu():
    menu = """\n
=============== TELA INICIAL ============
[1] \tNovo Aluno
[2] \tConsultar alunos
[3] \tAdicionar notas
[4] \tConsultar notas
[5] \tRemover Aluno
[6] \tSair
==>"""
    return input(textwrap.dedent(menu))

# Função para cadastrar novo aluno
def novo_aluno():
    nome = input("Nome do aluno: ")
    turma = input("Turma: ")
    if nome in alunos:
        print("Aluno já cadastrado! Verifique se digitou corretamente.")
    else:
        alunos[nome] = {"turma": turma, "notas": []}
        print(f"Aluno {nome} cadastrado com sucesso!")

# Função para consultar alunos
def consultar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLista de alunos:")
        for nome, dados in alunos.items():
            print(f"- {nome} (Turma: {dados['turma']})")

# Função para adicionar notas
def adicionar_notas():
    nome = input("Nome do aluno: ")
    if nome in alunos:
        try:
            nota = float(input("Nota a adicionar: "))
            alunos[nome]["notas"].append(nota)
            print("Nota adicionada.")
        except ValueError:
            print("Digite uma nota válida.")
    else:
        print("Aluno não encontrado.")

# Função para consultar notas
def consultar_notas():
    nome = input("Nome do aluno: ")
    if nome in alunos:
        notas = alunos[nome]["notas"]
        if notas:
            print(f"\nNotas de {nome}: {notas}")
            print(f"Média: {sum(notas)/len(notas):.2f}")
        else:
            print("Nenhuma nota cadastrada.")
    else:
        print("Aluno não encontrado.")

# Função para remover aluno
def remover_aluno():
    nome = input("Nome do aluno: ")
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno {nome} removido.")
    else:
        print("Aluno não encontrado.")

# Loop principal
def main():
    while True:
        opcao = menu()
        if opcao == "1":
            novo_aluno()
        elif opcao == "2":
            consultar_alunos()
        elif opcao == "3":
            adicionar_notas()
        elif opcao == "4":
            consultar_notas()
        elif opcao == "5":
            remover_aluno()
        elif opcao == "6":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()