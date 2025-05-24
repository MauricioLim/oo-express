from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.0, 'o melhor pão da cidade')
restaurante_praca.adicionar_bebida_cardipio(bebida_suco)
restaurante_praca.adicionar_prato_cardipio(prato_paozinho)


def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()