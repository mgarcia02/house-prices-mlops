"""
Módulo: config_parser
Descripción: Carga de archivos de configuración YAML
"""

import yaml

def load_config(path):
    """Carga un archivo YAML y devuelve un diccionario"""
    with open(path, "r") as f:
        return yaml.safe_load(f)
