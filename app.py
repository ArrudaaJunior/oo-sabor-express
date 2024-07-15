from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_praca.receber_avaliacao('Arruda', 10)
restaurante_praca.receber_avaliacao('Thais', 8)
restaurante_praca.receber_avaliacao('Sandra', 4)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()