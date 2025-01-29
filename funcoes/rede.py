import subprocess
from tkinter import messagebox, simpledialog, Toplevel, Text, Scrollbar, END

import subprocess

def testar_conectividade(endereco, janela_log):
    """
    Testa a conectividade com um endereço IP ou hostname usando ping.

    :param endereco: Endereço IP ou hostname a ser testado.
    :param janela_log: Função para registrar mensagens no log da interface.
    """
    try:
        janela_log(f"Testando conectividade com {endereco}...\n")
        
        # Executa o comando de ping (ajuste '-n' para Windows e '-c' para Linux/Mac)
        comando = ["ping", "-n", "4", endereco]  # Para Linux/Mac, troque "-n" por "-c".
        processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Captura e exibe a saída do ping em tempo real
        for linha in processo.stdout:
            janela_log(linha.strip())

        # Aguarda o término do processo
        processo.wait()

        if processo.returncode == 0:
            janela_log("\nConectividade testada com sucesso!\n")
        else:
            janela_log("\nFalha ao testar conectividade.\n")
    except Exception as e:
        janela_log(f"Erro ao executar o ping: {e}\n")

def configurar_ip_fixo(ip, mascara, gateway, dns_primario, dns_secundario):
    """Configura o IP fixo e os servidores DNS."""
    try:
        # Comando para configurar o IP fixo
        subprocess.run(
            [
                "netsh", "interface", "ip", "set", "address", 
                "name=Ethernet", "static", ip, mascara, gateway
            ],
            check=True
        )

        # Comando para configurar os servidores DNS
        subprocess.run(
            [
                "netsh", "interface", "ip", "set", "dns", 
                "name=Ethernet", "static", dns_primario
            ],
            check=True
        )
        if dns_secundario:
            subprocess.run(
                [
                    "netsh", "interface", "ip", "add", "dns", 
                    "name=Ethernet", dns_secundario, "index=2"
                ],
                check=True
            )
        messagebox.showinfo("Sucesso", "Configuração de IP fixo e DNS realizada com sucesso!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Falha ao configurar IP ou DNS: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

def redefinir_para_dhcp():
    """Redefine a configuração de rede para usar DHCP e DNS automático."""
    try:
        # Configurar IP para DHCP
        subprocess.run(
            ["netsh", "interface", "ip", "set", "address", "name=Ethernet", "source=dhcp"],
            check=True
        )
        # Configurar DNS para automático
        subprocess.run(
            ["netsh", "interface", "ip", "set", "dns", "name=Ethernet", "source=dhcp"],
            check=True
        )
        messagebox.showinfo("Sucesso", "Configurações de rede redefinidas para DHCP!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Falha ao redefinir para DHCP: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")
