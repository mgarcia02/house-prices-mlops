"""
Módulo: load_data
Descripción: Funciones para cargar datasets desde la carpeta data/raw
"""

import pandas as pd
from pathlib import Path

def load_csv(path: str) -> pd.DataFrame:
    """Carga un archivo CSV y devuelve un DataFrame."""
    return pd.read_csv(Path(path))
