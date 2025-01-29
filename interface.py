import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from funcoes.desinstalador import desinstalar_apps_padrao
from funcoes.utilitarios import instalar_programas
from funcoes.rede import testar_conectividade, configurar_ip_fixo, redefinir_para_dhcp
from funcoes.configuracoes import aplicar_configuracoes_windows
import threading


def criar_interface():
    """Função principal para criar a interface gráfica."""
    # Configurar a janela principal
    root = tk.Tk()
    root.title("Otimizador do Windows")
    root.geometry("500x500")
    root.resizable(False, False)
    root.configure(bg="#f5f5f5")

    # Criar o título
    titulo = tk.Label(
        root, text="Otimizador do Windows", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333"
    )
    titulo.pack(pady=20)

    # Criar uma janela separada para exibir logs e progresso
    def abrir_tela_log():
        tela_log = tk.Toplevel(root)
        tela_log.title("Detalhes da Execução")
        tela_log.geometry("600x400")
        tela_log.resizable(False, False)
        tela_log.configure(bg="#f5f5f5")

        # Log de execução
        log_text = ScrolledText(tela_log, height=20, state="disabled", wrap="word", bg="#fff", fg="#333", font=("Arial", 10))
        log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Função para atualizar os logs
        def logar(mensagem):
            log_text.config(state="normal")
            log_text.insert(tk.END, mensagem + "\n")
            log_text.config(state="disabled")
            log_text.see(tk.END)

        return logar

    # Inicializar a função de log
    logar = abrir_tela_log()

    # Funções de ação
    def executar_tarefa(funcao, descricao):
        """Executa uma função em uma thread separada."""
        logar(f"Iniciando: {descricao}...\n")

        def tarefa():
            try:
                funcao()
                logar(f"Concluído: {descricao}!\n")
            except Exception as e:
                logar(f"Erro ao executar {descricao}: {e}\n")

        threading.Thread(target=tarefa, daemon=True).start()

    def opcao_desinstalar():
        executar_tarefa(desinstalar_apps_padrao, "Desinstalação de Aplicativos Padrão")

    def opcao_instalar():
        executar_tarefa(instalar_programas, "Instalação de Programas Úteis")

    def opcao_rede():
        """Submenu de configurações de rede."""
        submenu_rede = tk.Toplevel(root)
        submenu_rede.title("Opções de Rede")
        submenu_rede.geometry("400x400")
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
                executar_tarefa(lambda: testar_conectividade(endereco, logar), f"Testando conectividade com {endereco}")
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
                executar_tarefa(
                    lambda: configurar_ip_fixo(ip, mascara, gateway, dns_primario, dns_secundario),
                    "Configuração de IP Fixo"
                )
            else:
                messagebox.showwarning("Atenção", "Todos os campos obrigatórios devem ser preenchidos!")

        btn_configurar_ip = tk.Button(
            submenu_rede, text="Configurar IP Fixo", command=configurar_ip, width=30
        )
        btn_configurar_ip.pack(pady=10)

        def redefinir_dhcp():
            executar_tarefa(redefinir_para_dhcp, "Redefinir para DHCP Automático")

        btn_redefinir_dhcp = tk.Button(
            submenu_rede,
            text="Redefinir para DHCP Automático",
            command=redefinir_dhcp,
            width=30,
        )
        btn_redefinir_dhcp.pack(pady=10)

    def opcao_customizacoes():
        executar_tarefa(aplicar_configuracoes_windows, "Aplicar Configurações do Windows")

    def grande_botao_vermelho():
        """Executa as três funções principais ao ser clicado."""
        def executar_todas():
            desinstalar_apps_padrao()
            instalar_programas()
            aplicar_configuracoes_windows()

        executar_tarefa(executar_todas, "Grande Botão Vermelho")

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
