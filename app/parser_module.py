from lark import Lark

gramatica = """
    ?inicio: expresion
    ?expresion: expresion "+" termino   -> suma
              | expresion "-" termino   -> resta
              | termino
    ?termino: termino "*" factor        -> multiplicacion
            | termino "/" factor        -> division
            | factor
    ?factor: "(" expresion ")"
           | NUMERO                     -> numero
    %import common.NUMBER -> NUMERO
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

parser = Lark(gramatica, parser='earley', debug=False)
