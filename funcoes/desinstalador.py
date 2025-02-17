"""
==========================
Arquivo: desinstalador.py
Descrição: Módulo para desinstalar aplicativos indesejados e pré-instalados do Windows.
Utiliza Winget (e PowerShell, se necessário) para remover os aplicativos.
==========================
"""

import subprocess

def desinstalar_apps_padrao():
    """
    Desinstala os aplicativos indesejados utilizando comandos Winget.
    A lista inclui os aplicativos originais e adicionais (como Outlook e apps de fabricantes).
    """
    try:
        # Lista de comandos Winget para remover aplicativos indesejados
        comandos_winget = [
            "winget uninstall Cortana",
            "winget uninstall Microsoft.GetHelp_8wekyb3d8bbwe",
            "winget uninstall Microsoft.YourPhone_8wekyb3d8bbwe",
            "winget uninstall {7B1FCD52-8F6B-4F12-A143-361EA39F5E7C}",
            "winget uninstall Microsoft.People_8wekyb3d8bbwe",
            "winget uninstall Microsoft.XboxGameOverlay_8wekyb3d8bbwe",
            "winget uninstall Microsoft.Xbox.TCUI_8wekyb3d8bbwe",
            "winget uninstall Microsoft.XboxIdentityProvider_8wekyb3d8bbwe",
            "winget uninstall Microsoft.WindowsMaps_8wekyb3d8bbwe",
            "winget uninstall Microsoft.XboxSpeechToTextOverlay_8wekyb3d8bbwe",
            "winget uninstall Microsoft.XboxGamingOverlay_8wekyb3d8bbwe",
            "winget uninstall Disney.37853FC22B2CE_6rarf9sa4v8jt",
            "winget uninstall Microsoft.BingWeather_8wekyb3d8bbwe",
            "winget uninstall Microsoft.Getstarted_8wekyb3d8bbwe",
            "winget uninstall Microsoft.MicrosoftOfficeHub_8wekyb3d8bbwe",
            "winget uninstall Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe",
            "winget uninstall Microsoft.Office.OneNote_8wekyb3d8bbwe",
            "winget uninstall Microsoft.SkypeApp_kzf8qxf38zg5c",
            "winget uninstall Microsoft.Wallet_8wekyb3d8bbwe",
            "winget uninstall Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe",
            "winget uninstall Microsoft.XboxApp_8wekyb3d8bbwe",
            "winget uninstall SpotifyAB.SpotifyMusic_zpdnekdrzrea0",
            "winget uninstall Microsoft.OneDrive",
            "winget uninstall C27EB4BA.DropboxOEM_xbfy0k16fey96",
            "winget uninstall Evernote.Evernote_q4d96b2w5wcc2",
            "winget uninstall FACEBOOK.317180B0BB486_8xx8rvfyw5nnt",
            "winget uninstall GoTrust ID Plugin",
            "winget uninstall Host App Service",
            "winget uninstall Microsoft.Edge",
            "winget uninstall Microsoft Edge Update",
            "winget uninstall Microsoft.BingWeather_8wekyb3d8bbwe",
            "winget uninstall Microsoft.MicrosoftEdge.Stable_8wekyb3d8bbwe",
            "winget uninstall Microsoft.MicrosoftSolitaireCollection_8wekyb3d8bbwe",
            "winget uninstall Microsoft.MixedReality.Portal_8wekyb3d8bbwe",
            "winget uninstall Microsoft.People_8wekyb3d8bbwe",
            "winget uninstall Opera.Opera",
            "winget uninstall SpotifyAB.SpotifyMusic_zpdnekdrzrea0"
        ]
        # Comandos adicionais para remover apps indesejados (incluindo Outlook e apps de fabricantes)
        comandos_adicionais = [
            "winget uninstall Microsoft.Outlook",
            "winget uninstall Acer.Sense",           # Exemplo para Acer – ajuste conforme necessário
            "winget uninstall Acer.Purified",         # Exemplo para Acer – ajuste conforme necessário
            "winget uninstall Dell.AppManager",       # Exemplo para Dell – ajuste conforme necessário
            "winget uninstall Samsung.AppSuite"       # Exemplo para Samsung – ajuste conforme necessário
        ]
        comandos = comandos_winget + comandos_adicionais
        for cmd in comandos:
            try:
                print(f"Executando: {cmd}")
                subprocess.run(cmd, shell=True, check=True)
                print(f"Executado com sucesso: {cmd}")
            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar {cmd}: {e}")
    except Exception as e:
        print(f"Erro geral em remover aplicativos indesejados: {e}")
