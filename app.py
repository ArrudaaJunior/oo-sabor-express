from modelos.restaurante import Restaurante
from modelos.cardapio.bebiba import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 4.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pao de coco', 0.80, 'Pão de coco, o melhor da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()