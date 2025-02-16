# from util import *
from models import *
from crud_db import *

def criar_contato():
  nome = input('Informe o nome do contato: ')
  data_nas = input('Informe a data de nascimento do contato: ')
  id = int(criar_contato_db(nome,data_nas))
  
  rua = input(f'Informe a rua do(a) {nome}(obrigatório): ')
  numero = input(f'Informe o número do(a) {nome}(obrigatório): ')
  complemento = input(f'Informe o complemento (se não tiver, deixar em branco): ')
  bairro = input(f'Informe o bairro do(a) {nome}(obrigatório): ')
  municipio = input(f'Informe o municipio do(a) {nome}(obrigatório): ')
  estado = input(f'Informe o estado do(a) {nome}(obrigatório): ')
  cep = input(f'Informe o cep do(a) {nome}(obrigatório): ')
  if not complemento:
    complemento = None
  criar_endereco_db(rua,numero,complemento,bairro,municipio,estado,cep,id)
  
  numero_tel = input(f'Informe o número de telefone do(a) {nome}: ')
  criar_telefone_db(numero_tel,id)
  
  email = input(f'Informe o email do(a) {nome}: ')
  criar_email_db(email,id)
  
def buscar_contato():
  nome_pesquisa = input("Digite o nome do contato: ")
  contatos_encontrados = buscar_contatos_por_nome(nome_pesquisa)

  if contatos_encontrados:
    print("\nContatos encontrados:")
    for index, contato in enumerate(contatos_encontrados):
      print(f"""
      {index + 1}. ID: {contato[0]}, Nome: {contato[1]}, Data de Nascimento: {contato[2]}
      Endereço: {contato[3]}, {contato[4]}, {contato[5] or 'Sem complemento'}, {contato[6]}, {contato[7]}, {contato[8]}, {contato[9]}
      Telefone: {contato[10] or 'Não informado'}
      Email: {contato[11] or 'Não informado'}
      """)
      
      escolha = int(input("\nDigite o número do contato desejado: ")) - 1

      if 0 <= escolha < len(contatos_encontrados):
        print(f"\nVocê escolheu: ID: {contato[0]}, Nome: {contato[1]}, Data de Nascimento: {contato[2]}, Endereço: {contato[3]}, {contato[4]}, {contato[5] or 'Sem complemento'}, {contato[6]}, {contato[7]}, {contato[8]}, {contato[9]} Telefone: {contato[10] or 'Não informado'} Email: {contato[11] or 'Não informado'}")
      else:
        print("Escolha inválida.")
  else:
    print(f"Nenhum contato com o nome '{nome_pesquisa}' foi encontrado.")

def alterar_campo():
  nome_pesquisa = input("Digite o nome do contato: ")
  contatos_encontrados = buscar_contatos_por_nome(nome_pesquisa)

  if contatos_encontrados:
    print("\nContatos encontrados:")
    for index, contato in enumerate(contatos_encontrados):
      print(f"""
      {index + 1}. ID: {contato[0]}, Nome: {contato[1]}, Data de Nascimento: {contato[2]}
      Endereço: {contato[3]}, {contato[4]}, {contato[5] or 'Sem complemento'}, {contato[6]}, {contato[7]}, {contato[8]}, {contato[9]}
      Telefone: {contato[10] or 'Não informado'}
      Email: {contato[11] or 'Não informado'}
      """)
    
    escolha = int(input("\nDigite o número do contato desejado: ")) - 1

    if 0 <= escolha < len(contatos_encontrados):
      print('1 - Alterar o nome')
      print('2 - Alterar a data de nascimento')
      print('3 - Alterar a rua')
      print('4 - Alterar o número da rua')
      print('5 - Alterar o complemento')
      print('6 - Alterar o bairro')
      print('7 - Alterar o município')
      print('8 - Alterar o estado')
      print('9 - Alterar o cep')
      print('10 - Alterar o número do telefone')
      print('11 - Alterar o email')
      escolha = int(input("Qual deseja alterar? "))
      match escolha:
        case 1:
          comando = "update contato set nome = ? where id = ?"
          novo_nome = input('Informe o nome atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (novo_nome, contato[0]))
              conn.commit()
              print(f"Nome do contato {contato[1]} atualizada para '{novo_nome}'!")
          except Exception as ex:
            print(f"Erro ao atualizar nome: {ex}")
          finally:
            desconectar(conn)
        case 2:
          comando = "update contato set data_nascimento = ? where id = ?"
          nova_data = input('Informe a data de nascimento atualizada (ano-mes-dia) ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (nova_data, contato[0]))
              conn.commit()
              print(f"Data de nascimento do contato {contato[1]} atualizada para '{nova_data}'!")
          except Exception as ex:
            print(f"Erro ao atualizar data de nascimento: {ex}")
          finally:
            desconectar(conn)
        case 3:
          comando = "update endereco set rua = ? where contato_id = ?"
          nova_rua = input('Informe a rua atualizada ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (nova_rua, contato[0]))
              conn.commit()
              print(f"Rua do contato {contato[1]} atualizada para '{nova_rua}'!")
          except Exception as ex:
            print(f"Erro ao atualizar rua: {ex}")
          finally:
            desconectar(conn)
        case 4:
          comando = "update endereco set numero = ? where contato_id = ?"
          nova_num_rua = input('Informe o número da rua atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (nova_num_rua, contato[0]))
              conn.commit()
              print(f"Número da rua do contato {contato[1]} atualizada para '{nova_num_rua}'!")
          except Exception as ex:
            print(f"Erro ao atualizar número da rua: {ex}")
          finally:
            desconectar(conn)
        case 5:
          comando = "update endereco set complemento = ? where contato_id = ?"
          nova_comp = input('Informe o complemento da residência atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (nova_comp, contato[0]))
              conn.commit()
              print(f"Complemento da residência do contato {contato[1]} atualizada para '{nova_comp}'!")
          except Exception as ex:
            print(f"Erro ao atualizar complemento da residência: {ex}")
          finally:
            desconectar(conn)
        case 6:
          comando = "update endereco set bairro = ? where contato_id = ?"
          nova_bairro = input('Informe o bairro atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (nova_bairro, contato[0]))
              conn.commit()
              print(f"Bairro do contato {contato[1]} atualizada para '{nova_bairro}'!")
          except Exception as ex:
            print(f"Erro ao atualizar Bairro: {ex}")
          finally:
            desconectar(conn)
        case 7:
          comando = "update endereco set municipio = ? where contato_id = ?"
          nova_municipio = input('Informe o município atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (nova_municipio, contato[0]))
              conn.commit()
              print(f"Município do contato {contato[1]} atualizada para '{nova_municipio}'!")
          except Exception as ex:
            print(f"Erro ao atualizar município: {ex}")
          finally:
            desconectar(conn)
        case 8:
          comando = "update endereco set estado = ? where contato_id = ?"
          nova_estado = input('Informe o estado atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (nova_estado, contato[0]))
              conn.commit()
              print(f"Estado do contato {contato[1]} atualizada para '{nova_estado}'!")
          except Exception as ex:
            print(f"Erro ao atualizar Estado: {ex}")
          finally:
            desconectar(conn)
        case 9:
          comando = "update endereco set cep = ? where contato_id = ?"
          nova_cep = input('Informe o cep atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (nova_cep, contato[0]))
              conn.commit()
              print(f"cep do contato {contato[1]} atualizada para '{nova_cep}'!")
          except Exception as ex:
            print(f"Erro ao atualizar cep: {ex}")
          finally:
            desconectar(conn)
        case 10:
          comando = "update telefone set numero = ? where contato_id = ?"
          novo_tel = input('Informe o número de telefone atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (novo_tel, contato[0]))
              conn.commit()
              print(f"Telefone do contato {contato[1]} atualizada para '{novo_tel}'!")
          except Exception as ex:
            print(f"Erro ao atualizar telefone: {ex}")
          finally:
            desconectar(conn)
        case 11:
          comando = "update telefone set email = ? where contato_id = ?"
          novo_email = input('Informe o email atualizado ')
          try: 
            with sqlite3.connect('agenda.db') as conn:
              cursor = conn.cursor()
              cursor.execute(comando, (novo_email, contato[0]))
              conn.commit()
              print(f"email do contato {contato[1]} atualizada para '{novo_email}'!")
          except Exception as ex:
            print(f"Erro ao atualizar email: {ex}")
          finally:
            desconectar(conn)
        case _: 
          print('Opção inválda')
          return
    else:
      print("Escolha inválida.")
      return
  else:
    print(f"Nenhum contato com o nome '{nome_pesquisa}' foi encontrado.")
    return
  
def apagar_contato():
  nome_pesquisa = input("Digite o nome do contato: ")
  contatos_encontrados = buscar_contatos_por_nome(nome_pesquisa)

  if contatos_encontrados:
    print("\nContatos encontrados:")
    for index, contato in enumerate(contatos_encontrados):
      print(f"""
      {index + 1}. ID: {contato[0]}, Nome: {contato[1]}, Data de Nascimento: {contato[2]}
      Endereço: {contato[3]}, {contato[4]}, {contato[5] or 'Sem complemento'}, {contato[6]}, {contato[7]}, {contato[8]}, {contato[9]}
      Telefone: {contato[10] or 'Não informado'}
      Email: {contato[11] or 'Não informado'}
      """)
      
      escolha = int(input("\nDigite o número do contato desejado: ")) - 1

      if 0 <= escolha < len(contatos_encontrados):
        comando = 'delete from contato where id = ?'
        with sqlite3.connect('agenda.db') as conn:
          try:
            cursor = conn.cursor()
            cursor.execute(comando, (contato[0],))
            conn.commit()
          except Exception as ex:
            print(ex)
      else:
        print("Escolha inválida.")
  else:
    print(f"Nenhum contato com o nome '{nome_pesquisa}' foi encontrado.")
    
def buscar_todos_contatos():
  pesq_contato = buscar_todos_contatos_db()
  
  if pesq_contato:
    print("\nContatos encontrados:")
    for index, contato in enumerate(pesq_contato):
      print(f"""
      {index + 1}. ID: {contato[0]}, Nome: {contato[1]}, Data de Nascimento: {contato[2]}
      Endereço: {contato[3]}, {contato[4]}, {contato[5] or 'Sem complemento'}, {contato[6]}, {contato[7]}, {contato[8]}, {contato[9]}
      Telefone: {contato[10] or 'Não informado'}
      Email: {contato[11] or 'Não informado'}
      """)
  else:
    print(f"Nenhum contato foi encontrado.")
    
buscar_todos_contatos()