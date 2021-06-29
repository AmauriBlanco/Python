from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:
        try:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            sobrenome = input("Digite seu Sobrenome: ")
            usuario = Usuario(nome, idade, sobrenome)

            lista_usuarios.append(usuario)
            if usuario.idade ==99:
                break
            if usuario.idade == 98:
                continue
            print(f"olá {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade} anos")

            if usuario.idade <=17:
                print(f"{usuario.nome} é adolescente")
            elif usuario.idade >=18 and usuario.idade <=50:
                print(f"{usuario.nome} é adulto")
            else:
                print(f"{usuario.nome} é idoso")
            continuar = int(input("Deseja continuar cadastrando? 0- Sair  -1-Continuar"))
        except ValueError:
            print("Você deve informa um número válido! ")

else:
    print('Lista de usuários cadastrados: ')
    for x in lista_usuarios:
        print(f"Nome Completo: {x.nome} {x.sobrenome} - Idade {x.idade}")

    print("Loop encerrado com sucesso !")



