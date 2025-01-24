import subprocess

def alterar_barra_tarefas():
    """Configura a barra de tarefas para mostrar apenas a lupa e desfixa itens indesejados."""
    try:
        # Configurar o campo de pesquisa para "Ícone de lupa"
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Search', 
             '/v', 'SearchboxTaskbarMode', '/t', 'REG_DWORD', '/d', '1', '/f'],
            check=True
        )
        # Desfixar itens da barra de tarefas, exceto os especificados
        subprocess.run(
            ['powershell', '-Command', 
             r"$apps = Get-StartApps; $apps | Where-Object {$_.Name -notlike '*Explorer*' -and $_.Name -notlike '*Chrome*' -and $_.Name -notlike '*Firefox*'} | ForEach-Object {Invoke-Command -ScriptBlock {Unpin-App $args[0]} -ArgumentList $_.Name}"],
            shell=True
        )
        print("Configurações da barra de tarefas alteradas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar a barra de tarefas: {e}")

def configurar_menu_iniciar():
    """Desativa opções desnecessárias do menu Iniciar."""
    try:
        # Desativar apps adicionados recentemente
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 
             '/v', 'Start_TrackProgs', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        # Desativar recomendações
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 
             '/v', 'SystemPaneSuggestionsEnabled', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        print("Configurações do menu Iniciar alteradas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar o menu Iniciar: {e}")

def configurar_personalizacao():
    """Configura a área de trabalho, tela de fundo e tela de bloqueio."""
    try:
        # Desativar apresentação de slides e definir imagem padrão na área de trabalho
        subprocess.run(
            ['reg', 'add', r'HKCU\Control Panel\Desktop', '/v', 'WallpaperStyle', '/t', 'REG_SZ', '/d', '10', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Control Panel\Desktop', '/v', 'Slideshow', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        # Definir imagem padrão na tela de bloqueio
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager', 
             '/v', 'RotatingLockScreenEnabled', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        # Desativar efeitos de transparência
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', 
             '/v', 'EnableTransparency', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        print("Configurações de personalização alteradas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar personalização: {e}")

def adicionar_icones_area_de_trabalho():
    """Adiciona ícones de Computador, Arquivos de Usuário e Painel de Controle à área de trabalho."""
    try:
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel', 
             '/v', '{20D04FE0-3AEA-1069-A2D8-08002B30309D}', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel', 
             '/v', '{59031a47-3f72-44a7-89c5-5595fe6b30ee}', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        subprocess.run(
            ['reg', 'add', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel', 
             '/v', '{5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}', '/t', 'REG_DWORD', '/d', '0', '/f'],
            check=True
        )
        print("Ícones adicionados à área de trabalho com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao adicionar ícones à área de trabalho: {e}")

def aplicar_configuracoes_windows():
    """Aplica todas as configurações de uma vez."""
    alterar_barra_tarefas()
    configurar_menu_iniciar()
    configurar_personalizacao()
    adicionar_icones_area_de_trabalho()
    print("Todas as configurações do Windows foram aplicadas com sucesso!")
