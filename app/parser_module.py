from lark import Lark

gramatica = """
    ?start: expr

    ?expr: expr "+" term   -> sumar
         | expr "-" term   -> restar
         | term

    ?term: term "*" factor -> multiplicar
         | term "/" factor -> dividir
         | factor

    ?factor: "(" expr ")"              // Expresión entre paréntesis
           | "-" factor                -> negativo // Negativo explícito
           | NUMBER                    -> numero

    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

parser = Lark(gramatica, parser='lalr', debug=False)
