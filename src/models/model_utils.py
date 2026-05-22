"""
Módulo: model_utils
Descripción: Guardado y carga de modelos entrenados
"""

import joblib

def save_model(model, path):
    """Guarda un modelo"""
    joblib.dump(model, path)

def load_model(path):
    """Carga un modelo"""
    return joblib.load(path)
