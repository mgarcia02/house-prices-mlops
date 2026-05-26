import os
import yaml
import logging
import logging.config

# Flag para evitar inicializar el logging más de una vez
_LOGGING_INITIALIZED = False


def setup_logging(config_path: str = "config/logging.yaml") -> None:
    """
    Carga la configuración de logging desde un archivo YAML y la aplica
    """
    global _LOGGING_INITIALIZED

    if _LOGGING_INITIALIZED:
        return  # Evita doble inicialización

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"No se encontró el archivo de logging: {config_path}")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)
    _LOGGING_INITIALIZED = True


def get_logger(name: str) -> logging.Logger:
    """
    Devuelve un logger con el nombre indicado
    Si el sistema de logging no está inicializado, lo inicializa automáticamente
    """
    if not _LOGGING_INITIALIZED:
        setup_logging()

    return logging.getLogger(name)
