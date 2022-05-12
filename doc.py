from cnpj import Cnpj
from cpf import Cpf

class Doc:

    # Esse cara e uma factory e por isso ele precisa que as classes cnpj e cpf possuam o mesmo nomes de metodos
    @staticmethod
    def cria_doc(doc):
        if len(doc) == 11:
            return Cpf(doc)
        elif len(doc) == 14:
            return Cnpj(doc)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")