from conectar_db import *
from models import *
import sqlite3

def criar_contato_db(nome, data_nascimento):
    comando = "INSERT INTO contato (nome, data_nascimento) VALUES (?, ?)"
    
    try:
        # Conectando ao banco de dados
        with sqlite3.connect('agenda.db') as conn:
            cursor = conn.cursor()
            cursor.execute(comando, (nome, data_nascimento))
            conn.commit()  # Certifique-se de salvar a transação
    except Exception as ex:
        print(ex)
    finally:
      desconectar(conn)
    return cursor.lastrowid
      
def criar_endereco_db(rua,numero,complemento,bairro,municipio,estado,cep,contato_id):
  comando = 'insert into endereco (rua,numero,complemento,bairro,municipio,estado,cep,contato_id) values (?,?,?,?,?,?,?,?)'
  
  try:
    with sqlite3.connect('agenda.db') as conn:
      cursor = conn.cursor()
      cursor.execute(comando, (rua,numero,complemento,bairro,municipio,estado,cep,contato_id))
      conn.commit()
  except Exception as ex:
    print(ex)
  finally:
    desconectar(conn)
    
def criar_telefone_db(numero,contato_id):
  comando = "INSERT INTO telefone (numero,contato_id) VALUES (?, ?)"
  
  try:
    with sqlite3.connect('agenda.db') as conn:
      cursor = conn.cursor()
      cursor.execute(comando, (numero,contato_id))
      conn.commit()
  except Exception as ex:
    print(ex)
  finally:
    desconectar(conn)
    
def criar_email_db(email, contato_id):
  comando = "INSERT INTO email (email,contato_id) VALUES (?, ?)"
  
  try:
    with sqlite3.connect('agenda.db') as conn:
      cursor = conn.cursor()
      cursor.execute(comando, (email,contato_id))
      conn.commit()
  except Exception as ex:
    print(ex)
  finally:
    desconectar(conn)

# def consultar_todos_contato_db():
#   comando = "select * from contato"
#   contatos = []
#   try:
#     with sqlite3.connect('agenda.db') as conn:
#       cursor = conn.cursor()
#       cursor.execute(comando)
#       registros = cursor.fetchall()
#       for registro in registros:
#         contato = Contato(registro[0],registro[1], registro[2])
#         contatos.append(contato)
#       conn.commit()
      
#   except Exception as ex:
#     print(ex)
#   finally:
#     desconectar(conn)
#   return contatos

# def consultar_todos_endereco_db():
#   comando = "select * from endereco"
#   enderecos = []
#   try:
#     with sqlite3.connect('agenda.db') as conn:
#       cursor = conn.cursor()
#       cursor.execute(comando)
#       registros = cursor.fetchall()
#       for registro in registros:
#         endereco = Endereco(registro[0],registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
#         enderecos.append(endereco)
#       conn.commit()
      
#   except Exception as ex:
#     print(ex)
#   finally:
#     desconectar(conn)
#   return enderecos

# def consultar_todos_telefone_db():
#   comando = "select * from telefone"
#   telefones = []
#   try:
#     with sqlite3.connect('agenda.db') as conn:
#       cursor = conn.cursor()
#       cursor.execute(comando)
#       registros = cursor.fetchall()
#       for registro in registros:
#         telefone = Telefone(registro[0],registro[1], registro[2])
#         telefones.append(telefone)
      
#   except Exception as ex:
#     print(ex)
#   finally:
#     desconectar(conn)
#   return telefones

# def consultar_todos_email_db():
#   comando = "select * from email"
#   emails = []
#   try:
#     with sqlite3.connect('agenda.db') as conn:
#       cursor = conn.cursor()
#       cursor.execute(comando)
#       registros = cursor.fetchall()
#       for registro in registros:
#         email = Email(registro[0],registro[1], registro[2])
#         emails.append(email)
      
#   except Exception as ex:
#     print(ex)
#   finally:
#     desconectar(conn)
#   return emails

def buscar_contatos_por_nome(nome):
  comando = """
    SELECT c.id, c.nome, c.data_nascimento, 
    e.rua, e.numero, e.complemento, e.bairro, e.municipio, e.estado, e.cep,
    t.numero AS telefone, 
    em.email
    FROM contato c
    LEFT JOIN endereco e ON c.id = e.contato_id
    LEFT JOIN telefone t ON c.id = t.contato_id
    LEFT JOIN email em ON c.id = em.contato_id
    WHERE c.nome = ?
    """
  
  try:
    with sqlite3.connect('agenda.db') as conn:
      cursor = conn.cursor()
      cursor.execute(comando, (nome,))
      resultados = cursor.fetchall()  # Pega todos os contatos encontrados
      return resultados if resultados else None  # Retorna os dados se existirem
  except Exception as ex:
    print(ex)
    return None
  finally:
    desconectar(conn)




