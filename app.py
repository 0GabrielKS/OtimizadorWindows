import logging
from interface import criar_interface
import subprocess
from funcoes.logger import registrar_erro
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "funcoes"))


# Configuração do logger
logging.basicConfig(
    filename="erro.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)

def registrar_erro(func):
    """Decorator para capturar erros e registrá-los no log."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Erro na função {func.__name__}: {e}", exc_info=True)
            raise e
    return wrapper

if __name__ == "__main__":
    try:
        criar_interface()
    except Exception as e:
        print(f"Erro ao iniciar o programa: {e}")
