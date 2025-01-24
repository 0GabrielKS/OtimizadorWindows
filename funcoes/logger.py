import logging

# Configuração do logger
logging.basicConfig(
    filename="erro_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def registrar_erro(func):
    """
    Decorador para registrar erros de funções no log.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Erro na função {func.__name__}: {e}")
            raise
    return wrapper
