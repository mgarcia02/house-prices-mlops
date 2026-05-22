"""
Módulo: logging_config
Descripción: Configuración del sistema de logging del proyecto
"""

import logging

def get_logger(name):
    """Devuelve un logger configurado"""
    return logging.getLogger(name)
