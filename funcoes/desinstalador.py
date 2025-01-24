import subprocess

def desinstalar_apps_padrao():
    """
    Desinstala aplicativos pré-instalados ou desnecessários do Windows usando o winget.
    """
    apps_padrao = [
        # Lista fornecida
        "Cortana",
        "Microsoft.GetHelp_8wekyb3d8bbwe",
        "Microsoft.YourPhone_8wekyb3d8bbwe",
        "Microsoft.People_8wekyb3d8bbwe",
        "Microsoft.XboxGameOverlay_8wekyb3d8bbwe",
        "Microsoft.Xbox.TCUI_8wekyb3d8bbwe",
        "Microsoft.XboxIdentityProvider_8wekyb3d8bbwe",
        "Microsoft.WindowsMaps_8wekyb3d8bbwe",
        "Microsoft.XboxSpeechToTextOverlay_8wekyb3d8bbwe",
        "Microsoft.XboxGamingOverlay_8wekyb3d8bbwe",
        "Disney.37853FC22B2CE_6rarf9sa4v8jt",
        "Microsoft.BingWeather_8wekyb3d8bbwe",
        "Microsoft.Getstarted_8wekyb3d8bbwe",
        "Microsoft.MicrosoftOfficeHub_8wekyb3d8bbwe",
        "Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe",
        "Microsoft.Office.OneNote_8wekyb3d8bbwe",
        "Microsoft.SkypeApp_kzf8qxf38zg5c",
        "Microsoft.Wallet_8wekyb3d8bbwe",
        "Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe",
        "Microsoft.XboxApp_8wekyb3d8bbwe",
        "SpotifyAB.SpotifyMusic_zpdnekdrzrea0",
        "Microsoft.OneDrive",
        "C27EB4BA.DropboxOEM_xbfy0k16fey96",
        "Evernote.Evernote_q4d96b2w5wcc2",
        "FACEBOOK.317180B0BB486_8xx8rvfyw5nnt",
        "GoTrust ID Plugin",
        "Host App Service",
        "Microsoft.MicrosoftSolitaireCollection_8wekyb3d8bbwe",
        "Microsoft.MixedReality.Portal_8wekyb3d8bbwe",
        "Opera.Opera",
        "Microsoft.PowerAutomateDesktop_8wekyb3d8bbwe",
        "Microsoft.OutlookForWindows_8wekyb3d8bbwe",
        "Microsoft.Todos_8wekyb3d8bbwe",
        "Microsoft.DevHome",
        "MicrosoftCorporationII.MicrosoftFamily_8wekyb3d8bbwe",
        "MicrosoftCorporationII.QuickAssist_8wekyb3d8bbwe",
        "Clipchamp.Clipchamp_yxz26nhyzhsrt",
        "MSC",
        "Microsoft.549981C3F5F10_8wekyb3d8bbwe",
        "Sidia.LiveWallpaper_wkpx6gdq8qyz8",
        "OneNoteFreeRetail - pt-br",
        "OneNoteFreeRetail - es-mx",
        "OneNoteFreeRetail - en-gb",
        "O365HomePremRetail - pt-br",
        "O365HomePremRetail - es-mx",
        "O365HomePremRetail - en-gb",
        "Microsoft.Teams.Free",
    ]

    print("Iniciando a desinstalação de aplicativos padrão...")
    for app in apps_padrao:
        try:
            print(f"Tentando desinstalar: {app}...")
            subprocess.run(["winget", "uninstall", "-e", "--id", app], shell=True, check=True)
            print(f"Desinstalado com sucesso: {app}")
        except subprocess.CalledProcessError:
            print(f"Falha ao desinstalar: {app}. Pode ser que ele já esteja desinstalado ou não seja encontrado.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
    
    print("Processo concluído!")
