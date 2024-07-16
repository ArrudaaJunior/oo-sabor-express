from modelos.restaurante import Restaurante
from modelos.cardapio.bebiba import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 4.0, 'grande')
prato_paozinho = Prato('Pao de coco', 0.80, 'Pão de coco, o melhor da cidade')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()