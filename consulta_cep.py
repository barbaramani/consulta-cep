import requests

print('{:*^30}'.format('\033[33mCONSULTA CEP\033[m'))

cep = input('Digite o CEP:')

while len(cep) != 8:
    print('Digitos inválidos.')
    cep = input('Digite o CEP novamente:')


requerer = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

resultado_cep = requerer.json()

if 'erro' in resultado_cep:
    print(f'Cep {cep} inválido.')
else:
    print(requerer.json())
