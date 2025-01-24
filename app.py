from interface import criar_interface

if __name__ == "__main__":
    try:
        criar_interface()
    except Exception as e:
        print(f"Erro ao iniciar o programa: {e}")
