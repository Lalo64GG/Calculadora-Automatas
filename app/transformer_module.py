from lark import Transformer, v_args

@v_args(inline=True)
class Calculadora(Transformer):
    from operator import add as sumar, sub as restar, mul as multiplicar, truediv as dividir
    numero = float

    def negativo(self, numero):
        return -numero
