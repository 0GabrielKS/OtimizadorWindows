import os

def limpar_lixeira():
    try:
        print("Limpando a lixeira...")
        os.system("del /q /s %systemdrive%\\$Recycle.Bin")
        print("Lixeira limpa!")
    except Exception as e:
        print(f"Erro ao limpar a lixeira: {e}")
