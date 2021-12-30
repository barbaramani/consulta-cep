import requests

print('CONSULTA CEP')

cep = input('Digite o CEP:')

if len(cep) != 8:
    print('Digitos inválidos.')
    exit()

requerer = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

resultado_cep = requerer.json()

if 'erro' in resultado_cep:
    print(f'Cep {cep} inválido.')
else:
    print(requerer.json())