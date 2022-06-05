# Nome: Esther Rocha Lima
# Matrícula: 04029733
# Turno: Manhã
# Turma: 3NMA

from time import sleep
import queue
import random

fila_atend = queue.Queue(5)

banner = '''
+-------------------------------+
| Bem vindo à Galaxy Store BR! |
| Sistema versão: 1.0           |
+-------------------------------+
'''

produtos = {1000: ["Mouse Redragon Cobra", 129.99, 0],
            1001: ["Teclado mecânico Reddragon Kumara", 230.00, 50],
            1002: ["RTX 3090", 13870.00, 24], 1003: ["Intel Core i5-11400", 1259.90, 35],
            1004: ["Headset Logitech", 549.90, 120], 1005: ["Cadeira Gamer", 1029.90, 15],
            1006: ["Monitor FHD 43 Polegadas", 1099.90, 13],
            1007: ["Memoria RAM 16GB 2666Mhz", 369.90, 60],
            1008: ["SSD Nvme M.2 250GB", 640.00, 16],
            1009: ["HDD 1TB", 560.00, 12],
            1010: ["Placa mãe gamer", 1200.90, 17]}


def listarProdutos():
    for i in produtos:
        print("Item no {0}: Nome: {1}, Preco: R${2}, Quantidade: {3}\n".format(i, produtos[i][0], produtos[i][1], produtos[i][2]))

def removerProduto(codigo):
    try:
        produtos.pop(codigo)
        print("Produto código {0} removido com sucesso!\n".format(codigo))
    except:
        print("Produto não encontrado.\n")

def inserirProduto(codigo, quantidade):
    print("Estoque do produto {0} atualizado com sucesso! Quantidade atual do estoque deste produto: {1}\n".format(codigo, quantidade))

def registrarItemCliente():
    carrinho = []
    nomecliente = str(input("Digite o nome do cliente: "))
    codProd = int(input("Digite o código do produto: "))

    if codProd in produtos:
        if produtos[codProd][2] > 0:
            quantidade = int(input("Digite a quantidade desejada: "))
            print("Cliente {} entrou na fila!".format(nomecliente))
            sleep(2)
            print("\n")
            preço = produtos[codProd][1] * quantidade
            preçof = ("{:.2f}".format(preço))
            nomeprod = produtos[codProd][0]

            if produtos[codProd][2] >= quantidade:
                carrinho.append(codProd)
                carrinho.append(nomeprod)
                carrinho.append(preçof)
                carrinho.append(quantidade)
                produtos[codProd][2] -= quantidade

        else:
            print("Sem estoque para esse produto!\n")
            adicionarOutro = str(input("Deseja adicionar outro produto? [S/N]: "))

            if adicionarOutro != 'S':
                main_menu()
            else:
                registrarItemCliente()

    else:
        print("Produto não encontrado!\n")
        adicionarOutro = str(input("Deseja adicionar outro produto? [S/N]: "))

        if adicionarOutro != 'S':
            main_menu()
        else:
            registrarItemCliente()

    ficha = (nomecliente, carrinho)
    fila_atend.put(ficha)


def main_menu():
    print('''
+---- OPÇÕES DE ATENDIMENTO ----+
[1] Listar produtos em estoque.
[2] Adicionar um novo produto.
[3] Remover um produto existente.
[4] Adicionar itens ao carrinho.

[0] Sair.
    ''')

    choice = int(input("Por favor selecione a opção desejada: "))
    print("\n")

    if choice == 1:
        listarProdutos()
        sleep(3)
        main_menu()

    elif choice == 2:

        codigo = int(input("Digite o código do produto: "))

        if codigo in produtos:
            if produtos[codigo][2] > 0:
                print("Este produto ainda possui estoque!")
                sleep(3)
                main_menu()

            elif produtos[codigo][2] < 1:
                quantidade = int(input("Digite a quantidade que deseja adicionar: "))

                produtos[codigo][2] = quantidade
                inserirProduto(codigo, quantidade)
                sleep(3)
                main_menu()

        else:
            print("Produto não encontrado no sistema.\n")
            sleep(3)
            main_menu()

    elif choice == 3:
        codigo = int(input("Por favor, digite o código do produto que deseja excluir: "))
        removerProduto(codigo)
        sleep(3)
        main_menu()

    elif choice == 4:
        while True:
            if fila_atend.empty():
                while fila_atend.full() != True:
                    registrarItemCliente()
            else:
                while fila_atend.empty() != True:
                    print('\n')
                    caixa_id = random.randint(1, 3)
                    print("--- Caixa Livre: {} ---\n".format(caixa_id))
                    atendeCliente(caixa_id)
                    sleep(5)
                    if fila_atend.empty() == True:
                        main_menu()

    elif choice == 0:
        print("Obrigado por utilizar nosso sistema!\n")
        sleep(3)
        exit(0)
    else:
        print("Opção inválida!\n")
        sleep(3)
        main_menu()


def atendeCliente(caixa):
    nome, carrinho = fila_atend.get()
    print("- Atendimento: caixa {}".format(caixa))
    print("- Cliente: {}".format(nome))
    print("- Código do produto, nome, quantidade e preço: {}".format(carrinho))


if __name__ == "__main__":
    print(banner)
    main_menu()