'Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário.'
'Leia os dados de todos os contatos do usuário de forma que a agenda fique completa e por fim imprima todos os contatos.'

'Nome e telefone'
dict = {}
tam = int(input("Digite o tamanho da agenda: "))

for i in range(tam):
    nome = input("Digite o nome do contato {}: ".format(i+1))
    telefone = input("Digite o telefone do contato {}: ".format(i+1))
    dict[nome] = {"Telefone": telefone}

print("\nContatos:")
for nome, dados in dict.items():
    print(nome)
    print("\tTelefone: {}".format(dados["Telefone"]))
