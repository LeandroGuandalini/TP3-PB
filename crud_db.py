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

def consultar_contato_db():
  comando = "select * from contato"
  contatos = []
  try:
    with sqlite3.connect('agenda.db') as conn:
      cursor = conn.cursor()
      cursor.execute(comando)
      registros = cursor.fetchall()
      for registro in registros:
        contato = Contato(registro[0],registro[1], registro[2])
        contatos.append(contato)
      conn.commit()
      
  except Exception as ex:
    print(ex)
  finally:
    desconectar(conn)
  return contatos

def consultar_endereco_db():
  comando = "select * from endereco"
  enderecos = []
  try:
    with sqlite3.connect('agenda.db') as conn:
      cursor = conn.cursor()
      cursor.execute(comando)
      registros = cursor.fetchall()
      for registro in registros:
        endereco = Endereco(registro[0],registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
        enderecos.append(endereco)
      conn.commit()
      
  except Exception as ex:
    print(ex)
  finally:
    desconectar(conn)
  return enderecos

def consultar_contato_db():
  comando = "select * from contato"
  contatos = []
  try:
    with sqlite3.connect('agenda.db') as conn:
      cursor = conn.cursor()
      cursor.execute(comando)
      registros = cursor.fetchall()
      for registro in registros:
        contato = Contato(registro[0],registro[1], registro[2])
        contatos.append(contato)
      conn.commit()
      
  except Exception as ex:
    print(ex)
  finally:
    desconectar(conn)
  return contatos

def consultar_contato_db():
  comando = "select * from contato"
  contatos = []
  try:
    with sqlite3.connect('agenda.db') as conn:
      cursor = conn.cursor()
      cursor.execute(comando)
      registros = cursor.fetchall()
      for registro in registros:
        contato = Contato(registro[0],registro[1], registro[2])
        contatos.append(contato)
      conn.commit()
      
  except Exception as ex:
    print(ex)
  finally:
    desconectar(conn)
  return contatos



