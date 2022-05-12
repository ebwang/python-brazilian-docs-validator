import re

class Telefone():
    def __init__(self, telefone):
        #Procura padrao de de telefone com 2 digitos ddd inicial de 4 a 5 de tamanho e final com 4
        self.padrao = "([0-9]{3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        self.resposta = re.search(self.padrao,telefone)
        if self.validate():
            self.numero = telefone
        else:
            raise ValueError("Numero de telefone errado")                 

    def __str__(self):
        return self.format()     

    def validate(self):
        if self.resposta:
            return True
        else:
            return False

    def format(self):
        formated = "+{}({}){}-{}".format(self.resposta.group(1),  self.resposta.group(2), self.resposta.group(3), self.resposta.group(4))
        return formated