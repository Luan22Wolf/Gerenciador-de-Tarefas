import os

lista_de_tarefas = [{"nome":"limpar casa","status":False},
                    {"nome":"1 hora de video game","status":True}]


def nome_app():
    print("*" * 30)
    print("G̶e̶r̶e̶n̶c̶i̶a̶d̶o̶r̶ D̶e̶ T̶a̶r̶e̶f̶a̶s̶")
    print("*" * 30)

def menu():
    print("1- Adicionar tarefa")
    print("2- Editar Tarefa")
    print("3- Alterar status da tarefa")
    print("4- Mostrar Tarefas")
    print("5- Remover uma Tarefa")
    print("6- Sair")
    

def finalizar_app():
    print("Aplicativo encerrado")

def voltar_ao_menu():
    input("\nDigite qualquer tecla para voltar ao menu: ")
    main()

def subtitulo(texto):
    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    input(texto)
    print(linha)
    print()

def adicionar_tarefas():
    subtitulo("ADICIONAR UMA TAREFA")
    adicionarTarefa = input("Digite a tarefa que deseja adicionar: ")
    dados_gerenciador = {"nome":adicionarTarefa,"status": False}
    lista_de_tarefas.append(dados_gerenciador)
    voltar_ao_menu()

def alterar_nome_tarefa():
    subtitulo("ALTERAR NOME DE UMA TAREFA")
    nome_da_tarefa = input("Infome o nome da tarefa que deseja modificar: ")
    tarefa_encontrada = False

    for i,tarefa in enumerate(lista_de_tarefas):
        if nome_da_tarefa == tarefa["nome"]:
            tarefa_encontrada = True
            novo_nome_da_tarefa = input("Informe o nome atualizado da tarefa: ")
            lista_de_tarefas[i]["nome"] = novo_nome_da_tarefa
            print("Nome alterado com sucesso!")
            break

        if not tarefa_encontrada:
            print("Tarefa não encontrada!")
        voltar_ao_menu()

def status_da_tarefa():
    subtitulo("STATUS DA TAREFA")
    nome_tarefa = input("Digite o nome da terefa: ")
    tarefa_encontrada = False

    for tarefa in lista_de_tarefas:
        if nome_tarefa == tarefa["nome"]:
            tarefa_encontrada =True
            tarefa["status"] = not tarefa["status"]
            mensagem = f"Tarefa realizada" if tarefa["status"] else "Não realizada"
            print(mensagem)
        voltar_ao_menu()
    
def listar_tarefas():
    subtitulo("LISTANDO TAREFAS")
    print(f"{'Nome da Tarefa'.ljust(30)} | {'Status'.ljust(30)}")
    for tarefa in lista_de_tarefas:
        nome_tarefa = tarefa["nome"]
        ativo = "Realizada" if tarefa["status"] else "Não Realizada"
        print(f"- {nome_tarefa.ljust(30)} | {ativo} ")
    voltar_ao_menu()

def remover_tarefa():
    subtitulo("REMOVER TAREFAS")
    remover = input("Digite a tarefa que deseja excluir:  ")
    for tarefa in lista_de_tarefas:
        if tarefa["nome"] == remover:
            lista_de_tarefas.remove(tarefa)
            break
    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            adicionar_tarefas()
        elif opcao_escolhida == 2:
            alterar_nome_tarefa()
        elif opcao_escolhida == 3:
            status_da_tarefa()           
        elif opcao_escolhida == 4:
            listar_tarefas()
        elif opcao_escolhida == 5:
            remover_tarefa()
        else:
            finalizar_app()

    except:
        print("Opção inválida")

        voltar_ao_menu()

def main():
    os.system("cls")
    nome_app()
    menu()
    escolher_opcao()

if __name__ == "__main__":
    main()