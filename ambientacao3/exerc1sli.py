'Crie um dicionário e armazene nele os seus dados: '
'nome, idade, telefone, endereço. Imprima todos os dados usando o padrão chave: valor.'

Dict1 = {
    "Nome": "Huanan Canova",
    "Idade": 23,
    "Telefone": "999484950",
    "Endereco": "Tv. Fagundes Varella",
}
'imprime a chave e o valor'
for i in Dict1.items():
    print(i[0], " ", i[1])

'imprime apenas os valores'
for valor in Dict1.values():
    print(valor)
