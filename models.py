class Contato():
  def __init__(self,id,nome,data_nascimento):
    self.id = id
    self.nome = nome
    self.data_nascimento = data_nascimento
    
  def __str__(self):
      return f"ID: {self.id}, Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}"
  
class Endereco():
    def __init__(self, id, rua, numero, complemento, bairro, estado, cep, contato_id):
        self.id = id
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.estado = estado
        self.cep = cep
        self.contato_id = contato_id
    
    def __str__(self):
        return f"ID: {self.id}, Rua: {self.rua}, Número: {self.numero}, Bairro: {self.bairro}, Estado: {self.estado}"

class Telefone():
    def __init__(self, id, numero, contato_id):
        self.id = id
        self.numero = numero
        self.contato_id = contato_id
    
    def __str__(self):
        return f"ID: {self.id}, Número: {self.numero}"

class Email():
    def __init__(self, id, email, contato_id):
        self.id = id
        self.email = email
        self.contato_id = contato_id
    
    def __str__(self):
        return f"ID: {self.id}, Email: {self.email}"