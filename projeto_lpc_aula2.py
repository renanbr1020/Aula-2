class Projeto ():
    descricao = ""
    nome =""
    def __init__ (descricao="",nome=""):
        self.descricao = descricao
        self.nome = nome

    
class Tarefa ():
    descricao = ""
    dataInicio = None
    dataFim = None
    prioridade =""
    def __init__ (self, descricao="", dataInicio=None, dataFim=None, prioridade =""):
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.prioridade = prioridade
        self.projeto = Projeto ()
        self.pessoaF = pessoaFisica()
        self.pessoaJ = pessoaJuridica()

class Pessoa(object):
    nome = ""
    data_nascimento = None

    def __init__(self,nome= "",data_nascimento=None):
        self.nome =nome
        self.data_nascimento = data_nascimento
        

class PessoaFisica(Pessoa):
    cpf = ""
    def __init__ (self, cpf=None, nome="", data_nascimento=None):
        Pessoa.__init__(self,nome,data_nascimento)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    CNPJ = None
    def __init__ (self,CNPJ=None,nome="", data_nascimento=None):
        Pessoa.__init__(self,nome,data_nascimento)
        self.CNPJ = CNPJ
