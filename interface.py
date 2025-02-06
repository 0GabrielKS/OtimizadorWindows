import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from funcoes.desinstalador import desinstalar_apps_padrao
from funcoes.utilitarios import instalar_programas
from funcoes.rede import testar_conectividade, configurar_ip_fixo, redefinir_para_dhcp
from funcoes.configuracoes import aplicar_configuracoes_windows

# Criar janela de log para exibir os detalhes da execução
def abrir_janela_log():
    janela_detalhes = tk.Toplevel()
    janela_detalhes.title("Detalhes da Execução")
    janela_detalhes.geometry("500x400")

    log_text = scrolledtext.ScrolledText(janela_detalhes, wrap=tk.WORD, width=60, height=20)
    log_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    return log_text

def criar_interface():
    """Função principal para criar a interface gráfica."""
    root = tk.Tk()
    root.title("Otimizador do Windows")
    root.geometry("400x500")
    root.resizable(False, False)
    root.configure(bg="#f5f5f5")

    # Criar título
    tk.Label(root, text="Otimizador do Windows", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)

    # Funções associadas aos botões
    def opcao_desinstalar():
        log_text = abrir_janela_log()
        try:
            log_text.insert("end", "Iniciando desinstalação de aplicativos padrão...\n")
            desinstalar_apps_padrao(log_text)
            log_text.insert("end", "Desinstalação concluída!\n")
        except Exception as e:
            log_text.insert("end", f"Erro: {e}\n")
        log_text.see("end")

    def opcao_instalar():
        log_text = abrir_janela_log()
        try:
            log_text.insert("end", "Iniciando instalação de programas...\n")
            instalar_programas(log_text)
            log_text.insert("end", "Instalação concluída!\n")
        except Exception as e:
            log_text.insert("end", f"Erro: {e}\n")
        log_text.see("end")

    def opcao_rede():
        """Criação da janela de configurações de rede."""
        submenu_rede = tk.Toplevel(root)
        submenu_rede.title("Opções de Rede")
        submenu_rede.geometry("350x400")
        submenu_rede.resizable(False, False)
        submenu_rede.configure(bg="#f0f0f0")

        tk.Label(submenu_rede, text="Configurações de Rede", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

        def testar_ping():
            endereco = simpledialog.askstring("Ping", "Digite o IP ou hostname para testar:")
            if endereco:
                log_text = abrir_janela_log()
                testar_conectividade(endereco, log_text)
            else:
                messagebox.showwarning("Atenção", "Você precisa informar um endereço IP ou hostname!")

        def configurar_ip():
            ip = simpledialog.askstring("IP Fixo", "Digite o IP (ex.: 192.168.1.100):")
            mascara = simpledialog.askstring("Máscara", "Digite a máscara (ex.: 255.255.255.0):")
            gateway = simpledialog.askstring("Gateway", "Digite o gateway (ex.: 192.168.1.1):")
            dns_primario = simpledialog.askstring("DNS Primário", "Digite o DNS primário (ex.: 8.8.8.8):")
            dns_secundario = simpledialog.askstring("DNS Secundário", "Digite o DNS secundário (opcional):")

            if ip and mascara and gateway and dns_primario:
                log_text = abrir_janela_log()
                try:
                    configurar_ip_fixo(ip, mascara, gateway, dns_primario, dns_secundario, log_text)
                    log_text.insert("end", "Configuração de IP fixo aplicada!\n")
                except Exception as e:
                    log_text.insert("end", f"Erro: {e}\n")
                log_text.see("end")
            else:
                messagebox.showwarning("Atenção", "Todos os campos obrigatórios devem ser preenchidos!")

        def redefinir_dhcp():
            log_text = abrir_janela_log()
            try:
                log_text.insert("end", "Redefinindo configuração de rede para DHCP...\n")
                redefinir_para_dhcp(log_text)
                log_text.insert("end", "Rede redefinida para DHCP automático!\n")
            except Exception as e:
                log_text.insert("end", f"Erro: {e}\n")
            log_text.see("end")

        tk.Button(submenu_rede, text="Testar Ping", command=testar_ping, width=30).pack(pady=10)
        tk.Button(submenu_rede, text="Configurar IP Fixo", command=configurar_ip, width=30).pack(pady=10)
        tk.Button(submenu_rede, text="Redefinir para DHCP", command=redefinir_dhcp, width=30).pack(pady=10)

    def opcao_customizacoes():
        log_text = abrir_janela_log()
        try:
            log_text.insert("end", "Aplicando customizações do Windows...\n")
            aplicar_configuracoes_windows(log_text)
            log_text.insert("end", "Customizações aplicadas!\n")
        except Exception as e:
            log_text.insert("end", f"Erro: {e}\n")
        log_text.see("end")

    def grande_botao_vermelho():
        log_text = abrir_janela_log()
        try:
            log_text.insert("end", "Executando otimização completa...\n")
            desinstalar_apps_padrao(log_text)
            instalar_programas(log_text)
            aplicar_configuracoes_windows(log_text)
            log_text.insert("end", "Todas as operações concluídas!\n")
        except Exception as e:
            log_text.insert("end", f"Erro: {e}\n")
        log_text.see("end")

    # Botões principais
    tk.Button(root, text="Desinstalar Apps Padrão", command=opcao_desinstalar, width=30, bg="#d9534f", fg="white").pack(pady=10)
    tk.Button(root, text="Instalar Programas", command=opcao_instalar, width=30, bg="#5bc0de", fg="white").pack(pady=10)
    tk.Button(root, text="Configurações de Rede", command=opcao_rede, width=30, bg="#5cb85c", fg="white").pack(pady=10)
    tk.Button(root, text="Customizar Windows", command=opcao_customizacoes, width=30, bg="#f0ad4e", fg="white").pack(pady=10)

    # Grande Botão Vermelho
    tk.Button(root, text="O GRANDE BOTÃO VERMELHO", command=grande_botao_vermelho, width=30, height=2, bg="#ff0000", fg="white", font=("Arial", 14, "bold")).pack(pady=20)

    # Botão de Sair
    tk.Button(root, text="Sair", command=root.quit, width=15, bg="#343a40", fg="white", font=("Arial", 10)).pack(pady=10)

    root.mainloop()

# Iniciar interface
criar_interface()
