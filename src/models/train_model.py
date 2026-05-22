"""
Módulo: train_model
Descripción: Entrenamiento de modelos de machine learning
"""

def train(model, X, y):
    """Entrena un modelo con los datos proporcionados"""
    model.fit(X, y)
    return model
