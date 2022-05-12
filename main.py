from doc import Doc
from telefone import Telefone
from data import Data
from cep import Cep

#cpf = 15616987913
#cpf = Cpf("00975069403")

#cnpj = "35379838000112"
#cnpj = Cnpj(cnpj)

doc = "35379838000112"
telefone = "11999755675"
cep = "57035180"
doc = Doc.cria_doc(doc)
telefone = Telefone(telefone)

cadastro = Data()
cep = Cep(cep)

print(cep)
print(cep.busca_cep_api())
#print(a)
print(cadastro)

print(telefone)