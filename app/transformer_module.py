import math
from lark import Transformer, v_args

@v_args(inline=True)
class Calculadora(Transformer):
    from operator import add as sumar, sub as restar, mul as multiplicar, truediv as dividir
    numero = float

    def negativo(self, numero):
        return -numero

    def funcion(self, nombre, valor):
        funciones = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "csc": lambda x: 1 / math.sin(x) if math.sin(x) != 0 else float('inf'),
            "sec": lambda x: 1 / math.cos(x) if math.cos(x) != 0 else float('inf'),
            "cot": lambda x: math.cos(x) / math.sin(x) if math.sin(x) != 0 else float('inf'),
            "floor": math.floor
        }
        if nombre in funciones:
            if nombre in ["sin", "cos", "tan", "csc", "sec", "cot"]:
                valor_radianes = math.radians(valor)  # Convertir grados a radianes
                return funciones[nombre](valor_radianes)
            return funciones[nombre](valor)
        raise ValueError(f"Función desconocida: {nombre}")
