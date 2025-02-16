from crud import *
from crud_db import *

def menu():
  while True:
    print('Bem vindo ao sistema de agenda!\n ')
    print('1 - criar um contato')
    print('2 - atualizar um contato ')
    print('3 - apagar um contato ')
    print('4 - Buscar um contato ')
    print('5 - Buscar todos os contato ')
    print('6 - sair do programa')
    user = input('\nQual ação você deseja realizar? ')
    try:
      user = int(user)
    except ValueError:
      print("A escolha deve ser um número inteiro.")
      continue  # Retorna ao início do loop
    if user < 0 or user > 6:
      print("Escolha inválida, o número deve ser um inteiro de 1 a 6")
    else:
      match user:
        case 1:
          criar_contato()
        case 2:
          alterar_campo()
        case 3:
          apagar_contato()
        case 4:
          buscar_contato()
        case 5:
          buscar_todos_contatos()
        case 6:
          print('Finalizando o programa')
          return
            
        
menu()