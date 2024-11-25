from flask import Flask, render_template, request
from .parser_module import parser
from .transformer_module import Calculadora
from .utils import visualizar_arbol
import logging

def create_app():
    app = Flask(__name__, static_folder='static')
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        resultado, imagen, expresion = None, None, ''
        tokens, token_counts = [], {}

        if request.method == 'POST':
            expresion = request.form.get('expresion', '')
            if expresion:
                try:
                    tree = parser.parse(expresion)
                    imagen = visualizar_arbol(tree)
                    resultado = Calculadora().transform(tree)
                    tokens = Calculadora().get_tokens()
                    token_counts = {
                        'números': sum(1 for t in tokens if t[0] == 'numero'),
                        'operadores': sum(1 for t in tokens if 'operador' in t[0])
                    }
                except Exception as e:
                    logger.error("Error: %s", e)
                    resultado = "Error en la expresión. Verifica la sintaxis."

        return render_template('index.html', resultado=resultado, imagen=imagen, expresion=expresion, tokens=tokens, token_counts=token_counts)

    return app
