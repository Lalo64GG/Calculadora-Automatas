from lark import Transformer, v_args

@v_args(inline=True)
class Evaluador(Transformer):  # Renombrado a 'Evaluador' para variar el estilo
    from operator import add as suma, sub as resta, mul as producto, truediv as cociente
    numero = float

    def __init__(self):
        super().__init__()
        self.lista_tokens = []  # Cambiado el nombre de 'tokens' a 'lista_tokens'
    
    def suma(self, a, b):
        self.lista_tokens.append(('operador', '+'))  # Agregar operador a la lista
        return a + b

    def resta(self, a, b):
        self.lista_tokens.append(('operador', '-'))
        return a - b

    def producto(self, a, b):
        self.lista_tokens.append(('operador', '*'))
        return a * b

    def cociente(self, a, b):
        self.lista_tokens.append(('operador', '/'))
       
