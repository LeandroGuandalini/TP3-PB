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
  
criar_contato()