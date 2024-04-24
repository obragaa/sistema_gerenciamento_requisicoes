# tests/__init__.py
import os
import sys

# Calculando o caminho absoluto para o diretório 'app'
path_to_app = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print("Path to app:", path_to_app)  # Imprime o caminho para verificação

# Inserindo o caminho no início do sys.path
sys.path.insert(0, path_to_app)
