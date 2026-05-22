"""
Módulo: evaluate_model
Descripción: Funciones para evaluar el rendimiento de los modelos
"""

from sklearn.metrics import mean_squared_error

def rmse(y_true, y_pred):
    """Calcula el RMSE"""
    return mean_squared_error(y_true, y_pred, squared=False)
