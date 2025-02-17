"""
==========================
Arquivo: configuracoes.py
Descrição: Módulo para aplicar customizações do Windows.
Inclui funções para:
  - Alterar a barra de tarefas para mostrar somente o ícone de pesquisa e desfixar itens indesejados.
  - Configurar o menu Iniciar (desativar apps recentes e recomendações).
  - Configurar a personalização (fundo, tela de bloqueio, transparência).
  - Adicionar ícones à área de trabalho (Computador, Arquivos de Usuário, Painel de Controle).
  - Limpar as pastas TEMP e %TEMP%.
  - Aplicar todas as configurações de uma vez.
==========================
"""

import subprocess
import os
import shutil

# ===========================
# Função: alterar_barra_tarefas
# Descrição: Configura a barra de tarefas para exibir somente o ícone de pesquisa (lupa)
# e desfixa itens indesejados.
# ===========================
def alterar_barra_tarefas():
    try:
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Search',
             '/v', 'SearchboxTaskbarMode', '/t', 'REG_DWORD', '/d', '1', '/f'],
            check=True
        )
        subprocess.run(
            ['powershell', '-Command',
             r"$apps = Get-StartApps; $apps | Where-Object { $_.Name -notlike '*Explorer*' -and $_.Name -notlike '*Chrome*' -and $_.Name -notlike '*Firefox*' } | ForEach-Object { Unpin-App $_.Name }"],
            shell=True,
            check=True
        )
        print("Barra de tarefas configurada com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar a barra de tarefas: {e}")

# ===========================
# Função: configurar_menu_iniciar
# Descrição: Desativa a exibição de aplicativos adicionados recentemente e recomendações no menu Iniciar.
# ===========================
def configurar_menu_iniciar():
    try:
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced',
             '/v', 'Start_TrackProgs', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
             '/v', 'SystemPaneSuggestionsEnabled', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        print("Menu Iniciar configurado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar o menu Iniciar: {e}")

# ===========================
# Função: configurar_personalizacao
# Descrição: Configura a personalização do Windows, ajustando fundo, tela de bloqueio e desativando efeitos de transparência.
# ===========================
def configurar_personalizacao():
    try:
        subprocess.run(
            ['reg', 'add', r'HKCU\Control Panel\Desktop', '/v', 'WallpaperStyle', '/t', 'REG_SZ', '/d', '10', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Control Panel\Desktop', '/v', 'Slideshow', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager',
             '/v', 'RotatingLockScreenEnabled', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize',
             '/v', 'EnableTransparency', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        print("Personalização configurada com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar personalização: {e}")

# ===========================
# Função: adicionar_icones_area_de_trabalho
# Descrição: Adiciona os ícones de Computador, Arquivos de Usuário e Painel de Controle à área de trabalho.
# ===========================
def adicionar_icones_area_de_trabalho():
    try:
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\\HideDesktopIcons\\NewStartPanel',
             '/v', '{20D04FE0-3AEA-1069-A2D8-08002B30309D}', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\\HideDesktopIcons\\NewStartPanel',
             '/v', '{59031a47-3f72-44a7-89c5-5595fe6b30ee}', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\\HideDesktopIcons\\NewStartPanel',
             '/v', '{5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        print("Ícones adicionados à área de trabalho com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao adicionar ícones à área de trabalho: {e}")

# ===========================
# Função: limpar_pastas_temp
# Descrição: Remove todos os arquivos e pastas dentro das pastas TEMP e %TEMP%.
# ===========================
def limpar_pastas_temp():
    try:
        temp_paths = [os.environ.get("TEMP"), os.environ.get("TMP")]
        for path in temp_paths:
            if path and os.path.exists(path):
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    try:
                        if os.path.isfile(item_path) or os.path.islink(item_path):
                            os.unlink(item_path)
                        elif os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                    except Exception as e:
                        print(f"Erro ao excluir {item_path}: {e}")
            else:
                print(f"Pasta {path} não encontrada.")
        print("Pastas TEMP limpas com sucesso!")
    except Exception as e:
        print(f"Erro em limpar_pastas_temp: {e}")

# ===========================
# Função: aplicar_configuracoes_windows
# Descrição: Aplica todas as configurações do Windows, chamando as funções:
#    - alterar_barra_tarefas
#    - configurar_menu_iniciar
#    - configurar_personalizacao
#    - adicionar_icones_area_de_trabalho
#    - limpar_pastas_temp
#    - remover_aplicativos_indesejados
# ===========================
def aplicar_configuracoes_windows():
    try:
        alterar_barra_tarefas()
        configurar_menu_iniciar()
        configurar_personalizacao()
        adicionar_icones_area_de_trabalho()
        limpar_pastas_temp()
        print("Todas as configurações do Windows foram aplicadas com sucesso.")
    except Exception as e:
        print(f"Erro ao aplicar configurações do Windows: {e}")

if __name__ == "__main__":
    aplicar_configuracoes_windows()
