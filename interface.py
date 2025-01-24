from tkinter import messagebox
import tkinter as tk
from funcoes.utilitarios import (
    listar_apps, instalar_programas, limpar_cache,
    monitorar_desempenho, atualizar_sistema, gerenciar_rede
)
from funcoes.desinstalador import desinstalar_apps_padrao

def criar_interface():
    # Janela principal
    janela = tk.Tk()
    janela.title("Gerenciador de Funções")
    janela.geometry("400x500")

    # Títulos e botões
    tk.Label(janela, text="Escolha uma opção:", font=("Arial", 14)).pack(pady=10)

    tk.Button(janela, text="Listar aplicativos instalados", command=listar_apps, width=30).pack(pady=5)
    tk.Button(janela, text="Desinstalar aplicativos padrão", command=desinstalar_apps_padrao, width=30).pack(pady=5)
    tk.Button(janela, text="Instalar programas úteis", command=instalar_programas, width=30).pack(pady=5)
    tk.Button(janela, text="Limpar cache e arquivos temporários", command=limpar_cache, width=30).pack(pady=5)
    tk.Button(janela, text="Monitorar desempenho do sistema", command=monitorar_desempenho, width=30).pack(pady=5)
    tk.Button(janela, text="Atualizar sistema", command=atualizar_sistema, width=30).pack(pady=5)
    tk.Button(janela, text="Gerenciar rede", command=gerenciar_rede, width=30).pack(pady=5)

    tk.Button(janela, text="Sair", command=janela.quit, width=30, bg="red", fg="white").pack(pady=10)

    # Executar interface
    janela.mainloop()
