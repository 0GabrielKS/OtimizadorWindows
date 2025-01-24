import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from threading import Thread
import subprocess
import sys
import io
from contextlib import redirect_stdout
from funcoes.desinstalador import desinstalar_apps_padrao
from funcoes.utilitarios import instalar_programas
from funcoes.rede import testar_conectividade, configurar_ip_fixo, redefinir_para_dhcp
from funcoes.configuracoes import aplicar_configuracoes_windows


class StdoutRedirector(io.StringIO):
    """Classe para redirecionar o stdout para uma StringIO."""

    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, s):
        self.text_widget.insert(tk.END, s)
        self.text_widget.see(tk.END)  # Scroll automático para o final
        self.text_widget.update()


def criar_interface():
    """Função principal para criar a interface gráfica."""
    # Configurar a janela principal
    root = tk.Tk()
    root.title("Otimizador do Windows")
    root.geometry("400x500")
    root.resizable(False, False)
    root.configure(bg="#f5f5f5")

    # Criar o título
    titulo = tk.Label(
        root, text="Otimizador do Windows", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333"
    )
    titulo.pack(pady=20)

    # Função para mostrar progresso
    def mostrar_progresso(tarefas):
        """Exibe uma janela de progresso enquanto as tarefas são executadas."""
        progresso_janela = tk.Toplevel(root)
        progresso_janela.title("Progresso")
        progresso_janela.geometry("500x400")
        progresso_janela.resizable(False, False)
        progresso_janela.configure(bg="#f5f5f5")

        # Barra de progresso
        barra = ttk.Progressbar(progresso_janela, orient="horizontal", length=400, mode="determinate")
        barra.pack(pady=10)

        # Label para exibir mensagens
        status_label = tk.Label(progresso_janela, text="Iniciando...", bg="#f5f5f5", font=("Arial", 12))
        status_label.pack(pady=10)

        # Widget de texto para exibir logs
        log_text = tk.Text(progresso_janela, wrap="word", width=60, height=15, bg="#eaeaea", fg="#333")
        log_text.pack(padx=10, pady=10)

        progresso_janela.update()

        def executar_tarefas():
            progresso = 0
            incremento = 100 // len(tarefas)
            stdout_redirector = StdoutRedirector(log_text)
            with redirect_stdout(stdout_redirector):
                for tarefa, descricao in tarefas:
                    try:
                        status_label.config(text=descricao)
                        progresso_janela.update()
                        tarefa()  # Executa a tarefa
                        progresso += incremento
                        barra["value"] = progresso
                        progresso_janela.update()
                    except Exception as e:
                        print(f"Erro: {e}")
                        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
                        progresso_janela.destroy()
                        return

            status_label.config(text="Concluído!")
            print("Todas as tarefas foram concluídas com sucesso!")
            messagebox.showinfo("Sucesso", "Todas as tarefas foram concluídas com sucesso!")
            progresso_janela.destroy()

        # Criar uma thread para executar as tarefas
        thread = Thread(target=executar_tarefas)
        thread.start()

    # Criar os botões de funcionalidade
    def opcao_desinstalar():
        mostrar_progresso([(desinstalar_apps_padrao, "Desinstalando aplicativos padrão...")])

    def opcao_instalar():
        mostrar_progresso([(instalar_programas, "Instalando programas úteis...")])

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
                mostrar_progresso([(lambda: testar_conectividade(endereco, submenu_rede), f"Testando conectividade com {endereco}...")])
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
                mostrar_progresso([
                    (lambda: configurar_ip_fixo(ip, mascara, gateway, dns_primario, dns_secundario), "Configurando IP fixo...")
                ])
            else:
                messagebox.showwarning("Atenção", "Todos os campos obrigatórios devem ser preenchidos!")

        btn_configurar_ip = tk.Button(
            submenu_rede, text="Configurar IP Fixo", command=configurar_ip, width=30
        )
        btn_configurar_ip.pack(pady=10)

        def redefinir_dhcp():
            mostrar_progresso([(redefinir_para_dhcp, "Redefinindo para DHCP automático...")])

        btn_redefinir_dhcp = tk.Button(
            submenu_rede,
            text="Redefinir para DHCP Automático",
            command=redefinir_dhcp,
            width=30,
        )
        btn_redefinir_dhcp.pack(pady=10)

    def opcao_customizacoes():
        mostrar_progresso([(aplicar_configuracoes_windows, "Aplicando customizações do Windows...")])

    def grande_botao_vermelho():
        """Executa as três funções principais ao ser clicado."""
        tarefas = [
            (desinstalar_apps_padrao, "Desinstalando aplicativos padrão..."),
            (instalar_programas, "Instalando programas úteis..."),
            (aplicar_configuracoes_windows, "Aplicando customizações do Windows...")
        ]
        mostrar_progresso(tarefas)

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
