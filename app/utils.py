import os
import logging
from lark.tree import Tree
import pydot

logger = logging.getLogger(__name__)

# Directorio para guardar imágenes
IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/images')
os.makedirs(IMAGE_DIR, exist_ok=True)

def tree_to_pydot(tree: Tree) -> pydot.Dot:
    graph = pydot.Dot(graph_type='graph')
    node_id = 0

    def add_nodes_edges(node, parent=None):
        nonlocal node_id
        current_id = node_id
        if isinstance(node, Tree):
            node_label = node.data
            graph.add_node(pydot.Node(str(current_id), label=node_label))
            if parent is not None:
                graph.add_edge(pydot.Edge(str(parent), str(current_id)))
            node_id += 1
            for child in node.children:
                add_nodes_edges(child, current_id)
        else:
            node_label = str(node)
            graph.add_node(pydot.Node(str(current_id), label=node_label, shape='ellipse'))
            if parent is not None:
                graph.add_edge(pydot.Edge(str(parent), str(current_id)))
            node_id += 1

    add_nodes_edges(tree)
    return graph

def visualizar_arbol(tree: Tree, nombre_archivo: str = "arbol_expresion.png") -> str:
    try:
        graph = tree_to_pydot(tree)
        filename = "arbol.png"
        image_path = os.path.join(IMAGE_DIR, filename)
        graph.write_png(image_path)
        return f"images/{filename}"
    except Exception as e:
        logger.error("Error al generar la imagen: %s", e)
        return None
