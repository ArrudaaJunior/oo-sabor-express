class Avaliacao:

    """Representa a avaliação de um restaurante e suas características."""

    def __init__(self, cliente, nota):

        """
        Inicializa uma instância da Avaliação.

        Parâmetros:
        - Cliente: O cliente do restaurante.
        - Nota: A nota que o cliente dar para o restaurante.
        """

        self._cliente = cliente
        self._nota = nota

    