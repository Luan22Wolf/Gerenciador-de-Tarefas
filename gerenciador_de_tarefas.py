lista_de_tarefas = [{"nome":"limpar casa","status":False},
                    {"nome":"1 hora de video game","status":True}]


def nome_app():
    print("*" * 30)
    print("G̶e̶r̶e̶n̶c̶i̶a̶d̶o̶r̶ D̶e̶ T̶a̶r̶e̶f̶a̶s̶")
    print("*" * 30)

def menu():
    print("1-Adicionar tarefa")
    print("2-Editar Tarefa")
    print("3-Listar Tarefas")
    print("4-Remover Tarefa")
    print("5-Sair")
    #UM POSSIVEL EDITAR TAREFA

def finalizar_app():
    print("Aplicativo encerrado")

def voltar_ao_menu():
    input("\nDigite qualquer tecla para voltar ao menu: ")
    main()

def adicionar_tarefas():#NÃO ESTA ADICIONANDO
    adicionar_tarefa = input("Qual tarefa deseja adcionar? ")
    dados_do_gerenciador = {"nome":"Caminhar","Status":False}
    lista_de_tarefas.append[dados_do_gerenciador]
    print(lista_de_tarefas)
    voltar_ao_menu()

#def editar_tarefa():
    
def listar_tarefas():
    for tarefa in lista_de_tarefas:
        nome_tarefa = tarefa["nome"]
        ativo = "Realizada" if tarefa["status"] else "Não Realizada"
        print(f"A tarefa {nome_tarefa}, com o Status {ativo} ")
    voltar_ao_menu()

def remover_tarefa(): #FALTA ESSA
    remover = input("Digite a tarefa que deseja excluir:  ")
    if lista_de_tarefas == remover:
        lista_de_tarefas.remove[remover]
    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            adicionar_tarefas()
        elif opcao_escolhida == 2:
            print("Editar tarefa")
            #editar_tarefa()
        elif opcao_escolhida == 3:
            listar_tarefas()
        elif opcao_escolhida == 4:
            remover_tarefa()
        else:
            finalizar_app()

    except:
        print("Opção inválida")

        voltar_ao_menu()

def main():
    nome_app()
    menu()
    escolher_opcao()

if __name__ == "__main__":
    main()