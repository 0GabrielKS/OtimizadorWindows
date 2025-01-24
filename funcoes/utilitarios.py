import subprocess
import os
import shutil
import psutil
import logging
from funcoes.logger import registrar_erro

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

@registrar_erro
def listar_apps():
    """
    Lista todos os aplicativos instalados usando o winget.
    """
    try:
        print("Listando todos os aplicativos instalados...")
        subprocess.run(["winget", "list"], shell=True, check=True)
    except Exception as e:
        print(f"Erro ao listar aplicativos: {e}")

@registrar_erro
def instalar_programas():
    """
    Instala programas úteis no Windows usando o winget.
    """
    programas = [
        "Google.Chrome",
        "Mozilla.Firefox",
        "RARLab.WinRAR",
        "Adobe.Acrobat.Reader.64-bit",
        "Avast.AvastFreeAntivirus"
    ]

    print("Iniciando a instalação dos programas...")
    for programa in programas:
        try:
            print(f"Tentando instalar: {programa}...")
            subprocess.run(["winget", "install", "-e", "--id", programa], shell=True, check=True)
            print(f"Instalado com sucesso: {programa}")
        except subprocess.CalledProcessError:
            print(f"Falha ao instalar: {programa}. Verifique o ID ou a conexão.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
    
    print("Processo de instalação concluído!")

@registrar_erro
def limpar_cache():
    """
    Limpa arquivos temporários e cache do sistema.
    """
    pastas_temp = [
        os.getenv('TEMP'),
        os.getenv('TMP'),
        os.path.expanduser("~\\AppData\\Local\\Temp")
    ]

    for pasta in pastas_temp:
        try:
            print(f"Limpando: {pasta}")
            shutil.rmtree(pasta, ignore_errors=True)
            print(f"Pasta {pasta} limpa com sucesso!")
        except Exception as e:
            print(f"Erro ao limpar {pasta}: {e}")

@registrar_erro
def monitorar_desempenho():
    """
    Mostra informações de desempenho do sistema.
    """
    try:
        cpu = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory().percent
        disco = psutil.disk_usage('/').percent

        print(f"Uso de CPU: {cpu}%")
        print(f"Uso de Memória: {memoria}%")
        print(f"Uso de Disco: {disco}%")
    except Exception as e:
        print(f"Erro ao monitorar desempenho: {e}")

@registrar_erro
def atualizar_sistema():
    """
    Verifica e instala atualizações do sistema usando o Windows Update.
    """
    try:
        print("Verificando atualizações do sistema...")
        subprocess.run(["wuauclt", "/detectnow"], shell=True, check=True)
        subprocess.run(["wuauclt", "/updatenow"], shell=True, check=True)
        print("Atualizações verificadas e instaladas (se disponíveis).")
    except Exception as e:
        print(f"Erro ao atualizar o sistema: {e}")

@registrar_erro
def atualizar_sistema():
    # (sem alterações)
    pass

@registrar_erro
def gerenciar_rede():
    """
    Mostra informações de rede, renova o DHCP e configura IP fixo (se necessário).
    """
    try:
        print("Informações de rede:")
        subprocess.run(["ipconfig"], shell=True, check=True)
        print("\nRenovando DHCP...")
        subprocess.run(["ipconfig", "/renew"], shell=True, check=True)
        print("DHCP renovado!")
    except Exception as e:
        print(f"Erro ao gerenciar a rede: {e}")

@registrar_erro
def realizar_ping(endereco):
    """
    Realiza um ping para um endereço de IP ou domínio.
    """
    try:
        print(f"Pingando {endereco}...")
        resultado = subprocess.run(["ping", "-n", "4", endereco], capture_output=True, text=True)
        print(resultado.stdout)  # Mostra o resultado do ping
    except Exception as e:
        print(f"Erro ao realizar o ping para {endereco}: {e}")

@registrar_erro
def configurar_ip_fixo(ip, mascara, gateway, dns_primario, dns_secundario=None):
    """
    Configura IP fixo para o adaptador de rede ativo.
    """
    try:
        print("Configurando IP fixo...")
        comandos = [
            f"netsh interface ip set address name=\"Ethernet\" static {ip} {mascara} {gateway}",
            f"netsh interface ip set dns name=\"Ethernet\" static {dns_primario}"
        ]

        if dns_secundario:
            comandos.append(f"netsh interface ip add dns name=\"Ethernet\" {dns_secundario} index=2")

        for comando in comandos:
            subprocess.run(comando, shell=True, check=True)

        print("IP fixo configurado com sucesso!")
    except Exception as e:
        print(f"Erro ao configurar IP fixo: {e}")

@registrar_erro
def testar_conectividade(endereco: str) -> str:
    """
    Testa a conectividade com um endereço (ping).
    :param endereco: Endereço a ser testado.
    :return: Resultado do ping como string.
    """
    try:
        resultado = subprocess.run(
            ["ping", "-n", "4", endereco],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if resultado.returncode == 0:
            return f"Ping bem-sucedido para {endereco}:\n{resultado.stdout}"
        else:
            return f"Falha ao pingar {endereco}:\n{resultado.stderr}"
    except Exception as e:
        return f"Erro ao realizar o ping: {str(e)}"