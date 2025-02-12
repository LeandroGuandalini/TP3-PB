import sqlite3
import os.path

BANCO ='agenda.db'
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
DIR_BANCO = os.path.join(BASE_DIR, BANCO)

def verificar_db():
  if (not os.path.exists(DIR_BANCO)):
    print('Erro: banco não existe')
    exit()

def conectar():
  conn = None
  try:
    conn = sqlite3.connect(DIR_BANCO)
  except Exception as ex:
    print(ex)
  return conn

def desconectar(conn):
  if (conn is not None):
    conn.close()


conn = conectar()
desconectar(conn)
    