import subprocess
from tkinter import messagebox, simpledialog, Toplevel, Text, Scrollbar, END

import subprocess

import subprocess

def testar_conectividade(endereco, log_widget):
    try:
        log_widget.insert("end", f"Testando conectividade com {endereco}...\n")
        log_widget.see("end")

        resultado = subprocess.run(
            ["ping", "-n", "4", endereco], capture_output=True, text=True, check=True
        )

        log_widget.insert("end", f"{resultado.stdout}\n")
        log_widget.see("end")

    except subprocess.CalledProcessError as e:
        log_widget.insert("end", f"Erro ao executar o ping: {e}\n")
        log_widget.see("end")


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
