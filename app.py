import requests

from modelos.restaurante import Restaurante
from modelos.cardapio.bebiba import Bebida
from modelos.cardapio.prato import Prato

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
reponse = requests.get(url)

if reponse.status_code == 200:
    dados_json = reponse.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f'O erro foi {reponse.status_code}')

print(dados_restaurante['McDonald’s'])

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 4.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pao de coco', 0.80, 'Pão de coco, o melhor da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    # restaurante_praca.exibir_cardapio
    print(reponse)

if __name__ == '__main__':
    main()