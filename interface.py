import tkinter as tk
from tkinter import messagebox, simpledialog
from funcoes.desinstalador import desinstalar_apps_padrao
from funcoes.utilitarios import instalar_programas
from funcoes.rede import testar_conectividade, configurar_ip_fixo, redefinir_para_dhcp
from funcoes.configuracoes import aplicar_configuracoes_windows


def criar_interface():
    """Função principal para criar a interface gráfica."""
    # Configurar a janela principal
    root = tk.Tk()
    root.title("Otimizador do Windows")
    root.geometry("400x480")
    root.resizable(False, False)
    root.configure(bg="#f5f5f5")

    # Criar o título
    titulo = tk.Label(
        root, text="Otimizador do Windows", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333"
    )
    titulo.pack(pady=20)

    # Criar os botões de funcionalidade
    def opcao_desinstalar():
        try:
            desinstalar_apps_padrao()
            messagebox.showinfo("Sucesso", "Aplicativos padrão desinstalados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def opcao_instalar():
        try:
            instalar_programas()
            messagebox.showinfo("Sucesso", "Programas instalados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def opcao_rede():
        """Submenu de configurações de rede."""
        submenu_rede = tk.Toplevel(root)
        submenu_rede.title("Opções de Rede")
        submenu_rede.geometry("350x400")
        submenu_rede.resizable(False, False)
        submenu_rede.configure(bg="#f0f0f0")

        tk.Label(
            submenu_rede,
            text="Configurações de Rede",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#333",
        ).pack(pady=10)

        def testar_ping():
            endereco = simpledialog.askstring("Ping", "Digite o endereço IP ou hostname para testar:")
            if endereco:
                testar_conectividade(endereco, submenu_rede)
            else:
                messagebox.showwarning("Atenção", "Você precisa informar um endereço IP ou hostname!")

        btn_testar_ping = tk.Button(
            submenu_rede, text="Testar Conectividade (Ping)", command=testar_ping, width=30
        )
        btn_testar_ping.pack(pady=10)

        def configurar_ip():
            """Coleta os dados do usuário para configurar o IP fixo."""
            ip = simpledialog.askstring("IP Fixo", "Digite o IP (ex.: 192.168.1.100):")
            mascara = simpledialog.askstring("Máscara de Sub-rede", "Digite a máscara (ex.: 255.255.255.0):")
            gateway = simpledialog.askstring("Gateway", "Digite o gateway (ex.: 192.168.1.1):")
            dns_primario = simpledialog.askstring("DNS Primário", "Digite o servidor DNS primário (ex.: 8.8.8.8):")
            dns_secundario = simpledialog.askstring(
                "DNS Secundário", "Digite o servidor DNS secundário (opcional):"
            )

            if ip and mascara and gateway and dns_primario:
                try:
                    configurar_ip_fixo(ip, mascara, gateway, dns_primario, dns_secundario)
                    messagebox.showinfo("Sucesso", "Configuração de IP fixo realizada com sucesso!")
                except Exception as e:
                    messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
            else:
                messagebox.showwarning("Atenção", "Todos os campos obrigatórios devem ser preenchidos!")

        btn_configurar_ip = tk.Button(
            submenu_rede, text="Configurar IP Fixo", command=configurar_ip, width=30
        )
        btn_configurar_ip.pack(pady=10)

        def redefinir_dhcp():
            try:
                redefinir_para_dhcp()
                messagebox.showinfo("Sucesso", "Configuração de rede redefinida para DHCP automático!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

        btn_redefinir_dhcp = tk.Button(
            submenu_rede,
            text="Redefinir para DHCP Automático",
            command=redefinir_dhcp,
            width=30,
        )
        btn_redefinir_dhcp.pack(pady=10)

    def opcao_customizacoes():
        try:
            aplicar_configuracoes_windows()
            messagebox.showinfo("Sucesso", "Configurações do Windows aplicadas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def grande_botao_vermelho():
        """Executa as três funções principais ao ser clicado."""
        try:
            desinstalar_apps_padrao()
            instalar_programas()
            aplicar_configuracoes_windows()
            messagebox.showinfo("Sucesso", "Todas as operações foram concluídas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao executar o botão: {e}")

    # Adicionar botões à interface principal
    btn_desinstalar = tk.Button(
        root, text="Desinstalar Aplicativos Padrão", command=opcao_desinstalar, width=30, bg="#d9534f", fg="white"
    )
    btn_desinstalar.pack(pady=10)

    btn_instalar = tk.Button(
        root, text="Instalar Programas Úteis", command=opcao_instalar, width=30, bg="#5bc0de", fg="white"
    )
    btn_instalar.pack(pady=10)

    btn_rede = tk.Button(
        root, text="Configurações de Rede", command=opcao_rede, width=30, bg="#5cb85c", fg="white"
    )
    btn_rede.pack(pady=10)

    btn_customizacoes = tk.Button(
        root,
        text="Customizações do Windows",
        command=opcao_customizacoes,
        width=30,
        bg="#f0ad4e",
        fg="white",
    )
    btn_customizacoes.pack(pady=10)

    # Adicionar o Grande Botão Vermelho
    btn_grande_vermelho = tk.Button(
        root,
        text="O GRANDE BOTÃO VERMELHO",
        command=grande_botao_vermelho,
        width=30,
        height=2,
        bg="#ff0000",
        fg="white",
        font=("Arial", 14, "bold"),
    )
    btn_grande_vermelho.pack(pady=20)

    # Botão de Sair
    btn_sair = tk.Button(
        root,
        text="Sair",
        command=root.quit,
        width=15,
        bg="#343a40",
        fg="white",
        font=("Arial", 10),
    )
    btn_sair.pack(pady=10)

    # Rodar o loop principal
    root.mainloop()
