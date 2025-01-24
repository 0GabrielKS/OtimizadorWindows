import subprocess
from tkinter import messagebox, simpledialog, Toplevel, Text, Scrollbar, END

def testar_conectividade(endereco, parent_window):
    """Testa a conectividade via ping para um endereço especificado e exibe o resultado completo."""
    try:
        resultado = subprocess.run(
            ["ping", "-n", "4", endereco],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Criar uma nova janela para exibir o resultado completo
        janela_resultado = Toplevel(parent_window)
        janela_resultado.title(f"Resultado do Ping: {endereco}")
        janela_resultado.geometry("500x400")

        # Área de texto para exibir a saída do ping
        text_area = Text(janela_resultado, wrap="word", font=("Courier", 10))
        text_area.insert(END, resultado.stdout if resultado.returncode == 0 else resultado.stderr)
        text_area.config(state="disabled")
        text_area.pack(side="left", fill="both", expand=True)

        # Barra de rolagem
        scroll_bar = Scrollbar(janela_resultado, command=text_area.yview)
        text_area.config(yscrollcommand=scroll_bar.set)
        scroll_bar.pack(side="right", fill="y")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao testar conectividade: {e}")

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
