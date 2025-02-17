"""
==========================
Arquivo: interface.py
Descrição: Interface gráfica do Otimizador do Windows.
Esta interface possui botões para:
  - Desinstalar aplicativos padrão (função definida em funcoes/desinstalador.py)
  - Instalar programas úteis
  - Configurações de rede (testar ping, configurar IP, redefinir DHCP)
  - Customizar o Windows (aplicar configurações, limpar TEMP, remover apps indesejados)
  - Executar todas as funções com o "GRANDE BOTÃO VERMELHO"
  - Sair do programa
==========================
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, ttk
import threading
import subprocess
from funcoes.desinstalador import desinstalar_apps_padrao  # Função definida no módulo desinstalador.py
from funcoes.utilitarios import instalar_programas
from funcoes.rede import testar_conectividade, configurar_ip_fixo, redefinir_para_dhcp
from funcoes.configuracoes import aplicar_configuracoes_windows

# ===========================
# Função: abrir_janela_log
# Descrição: Cria e retorna uma janela de log com um widget ScrolledText para exibir os detalhes da execução.
# ===========================
def abrir_janela_log():
    janela = tk.Toplevel()
    janela.title("Detalhes da Execução")
    janela.geometry("600x400")
    janela.resizable(False, False)
    janela.configure(bg="#ffffff")
    
    log_text = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=60, height=20, font=("Arial", 10))
    log_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    log_text.config(state=tk.DISABLED)
    return log_text

# ===========================
# Função: atualizar_log
# Descrição: Atualiza o widget de log com a mensagem fornecida.
# ===========================
def atualizar_log(widget, mensagem):
    widget.config(state=tk.NORMAL)
    widget.insert(tk.END, mensagem + "\n")
    widget.config(state=tk.DISABLED)
    widget.see(tk.END)

# ===========================
# Função: executar_funcao_com_progresso
# Descrição: Executa uma função (sem argumentos) em uma thread separada,
# atualizando o log e utilizando uma barra de progresso indeterminada.
# ===========================
def executar_funcao_com_progresso(func, descricao, log_widget, barra):
    def tarefa():
        try:
            atualizar_log(log_widget, f"Iniciando: {descricao}...")
            func()  # Chama a função sem argumentos
            atualizar_log(log_widget, f"Concluído: {descricao}!")
        except Exception as e:
            atualizar_log(log_widget, f"Erro em {descricao}: {e}")
        finally:
            barra.stop()
    threading.Thread(target=tarefa, daemon=True).start()

# ===========================
# Função: criar_interface
# Descrição: Cria a janela principal com os botões para cada operação.
# ===========================
def criar_interface():
    root = tk.Tk()
    root.title("Otimizador do Windows")
    root.geometry("400x500")
    root.resizable(False, False)
    root.configure(bg="#f5f5f5")
    
    tk.Label(root, text="Otimizador do Windows", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)
    
    # Botão: Desinstalar Apps Padrão
    def opcao_desinstalar():
        log_widget = abrir_janela_log()
        barra = ttk.Progressbar(log_widget.master, mode="indeterminate", length=400)
        barra.pack(pady=5)
        barra.start()
        executar_funcao_com_progresso(desinstalar_apps_padrao, "Desinstalação de aplicativos padrão", log_widget, barra)
    
    # Botão: Instalar Programas Úteis
    def opcao_instalar():
        log_widget = abrir_janela_log()
        barra = ttk.Progressbar(log_widget.master, mode="indeterminate", length=400)
        barra.pack(pady=5)
        barra.start()
        executar_funcao_com_progresso(instalar_programas, "Instalação de programas úteis", log_widget, barra)
    
    # Botão: Configurações de Rede
    def opcao_rede():
        submenu = tk.Toplevel(root)
        submenu.title("Opções de Rede")
        submenu.geometry("350x300")
        submenu.resizable(False, False)
        submenu.configure(bg="#f0f0f0")
        
        tk.Label(submenu, text="Configurações de Rede", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)
        
        def testar_ping():
            endereco = simpledialog.askstring("Ping", "Digite o IP ou hostname para testar:")
            if endereco:
                log_widget = abrir_janela_log()
                barra = ttk.Progressbar(log_widget.master, mode="indeterminate", length=400)
                barra.pack(pady=5)
                barra.start()
                try:
                    atualizar_log(log_widget, f"Testando conectividade com {endereco}...")
                    processo = subprocess.Popen(["ping", "-n", "4", endereco],
                                                  stdout=subprocess.PIPE,
                                                  stderr=subprocess.STDOUT,
                                                  text=True,
                                                  shell=True)
                    for linha in processo.stdout:
                        atualizar_log(log_widget, linha.strip())
                    processo.wait()
                    atualizar_log(log_widget, "Teste concluído.")
                except Exception as e:
                    atualizar_log(log_widget, f"Erro: {e}")
                finally:
                    barra.stop()
            else:
                messagebox.showwarning("Atenção", "Informe um endereço válido!")
        
        def configurar_ip():
            ip = simpledialog.askstring("IP Fixo", "Digite o IP (ex.: 192.168.1.100):")
            mascara = simpledialog.askstring("Máscara", "Digite a máscara (ex.: 255.255.255.0):")
            gateway = simpledialog.askstring("Gateway", "Digite o gateway (ex.: 192.168.1.1):")
            dns1 = simpledialog.askstring("DNS Primário", "Digite o DNS primário (ex.: 8.8.8.8):")
            dns2 = simpledialog.askstring("DNS Secundário", "Digite o DNS secundário (opcional):")
            if ip and mascara and gateway and dns1:
                log_widget = abrir_janela_log()
                barra = ttk.Progressbar(log_widget.master, mode="indeterminate", length=400)
                barra.pack(pady=5)
                barra.start()
                executar_funcao_com_progresso(lambda: configurar_ip_fixo(ip, mascara, gateway, dns1, dns2),
                                              f"Configuração de IP fixo ({ip})", log_widget, barra)
            else:
                messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios!")
        
        def redefinir_dhcp():
            log_widget = abrir_janela_log()
            barra = ttk.Progressbar(log_widget.master, mode="indeterminate", length=400)
            barra.pack(pady=5)
            barra.start()
            executar_funcao_com_progresso(redefinir_para_dhcp, "Redefinição para DHCP", log_widget, barra)
        
        tk.Button(submenu, text="Testar Ping", command=testar_ping, width=30).pack(pady=10)
        tk.Button(submenu, text="Configurar IP Fixo", command=configurar_ip, width=30).pack(pady=10)
        tk.Button(submenu, text="Redefinir para DHCP", command=redefinir_dhcp, width=30).pack(pady=10)
    
    # Botão: Customizar Windows
    def opcao_customizacoes():
        log_widget = abrir_janela_log()
        barra = ttk.Progressbar(log_widget.master, mode="indeterminate", length=400)
        barra.pack(pady=5)
        barra.start()
        executar_funcao_com_progresso(aplicar_configuracoes_windows, "Aplicar customizações do Windows", log_widget, barra)
    
    # Botão: O GRANDE BOTÃO VERMELHO (executa todas as funções principais)
    def grande_botao_vermelho():
        log_widget = abrir_janela_log()
        barra = ttk.Progressbar(log_widget.master, mode="indeterminate", length=400)
        barra.pack(pady=5)
        barra.start()
        def executar_todas():
            desinstalar_apps_padrao()
            instalar_programas()
            aplicar_configuracoes_windows()
        executar_funcao_com_progresso(executar_todas, "Executando otimização completa", log_widget, barra)
    
    # Botões da interface principal
    tk.Button(root, text="Desinstalar Apps Padrão", command=opcao_desinstalar, width=30, bg="#d9534f", fg="white").pack(pady=10)
    tk.Button(root, text="Instalar Programas Úteis", command=opcao_instalar, width=30, bg="#5bc0de", fg="white").pack(pady=10)
    tk.Button(root, text="Configurações de Rede", command=opcao_rede, width=30, bg="#5cb85c", fg="white").pack(pady=10)
    tk.Button(root, text="Customizar Windows", command=opcao_customizacoes, width=30, bg="#f0ad4e", fg="white").pack(pady=10)
    tk.Button(root, text="O GRANDE BOTÃO VERMELHO", command=grande_botao_vermelho, width=30, height=2, bg="#ff0000", fg="white", font=("Arial", 14, "bold")).pack(pady=20)
    tk.Button(root, text="Sair", command=root.quit, width=15, bg="#343a40", fg="white", font=("Arial", 10)).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    criar_interface()
