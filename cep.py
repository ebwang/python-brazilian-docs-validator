import requests

class Cep:
    def __init__(self, cep):
        cep = str(cep)
        if self.validate(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def validate(self, cep):
        if len(cep) == 8:
            return True
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def format(self):
        cep_formatado = self.cep[:5]+'-'+self.cep[5:]
        return cep_formatado

    def __str__(self):
        return self.format()

    def busca_cep_api(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        return {
            r.json()['localidade'],
            r.json()['uf'],
            r.json()['bairro']
        }
        