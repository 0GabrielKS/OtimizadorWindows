# OtmzWindows
 
# Gerenciador de Funções do Windows

Um programa em Python com interface gráfica para facilitar o gerenciamento de computadores Windows. Este programa reúne diversas funcionalidades úteis, como desinstalar aplicativos padrão, instalar programas essenciais, monitorar desempenho, gerenciar rede (incluindo IP fixo), entre outras.

## Funcionalidades

- **Listar aplicativos instalados:** Mostra todos os programas instalados no sistema.
- **Desinstalar aplicativos padrão:** Remove automaticamente aplicativos pré-instalados no Windows, como Cortana, Xbox, OneNote, entre outros.
- **Instalar programas úteis:** Instala softwares essenciais, como:
  - Google Chrome
  - Mozilla Firefox
  - WinRAR
  - Adobe Reader
  - Avast Free
- **Limpar cache e arquivos temporários:** Libera espaço ao remover arquivos desnecessários.
- **Monitorar desempenho:** Exibe informações sobre o uso de CPU, memória, disco e rede.
- **Atualizar sistema:** Verifica e instala atualizações pendentes do Windows.
- **Gerenciar rede:**
  - Exibe informações da rede.
  - Renova o DHCP.
  - Configura IP fixo.
- **Pingar um endereço:** Testa a conectividade com um endereço IP ou domínio fornecido pelo usuário.
- **Configurar IP fixo:** Permite configurar IP fixo, máscara de sub-rede, gateway e servidores DNS.

## Pré-requisitos

- **Sistema Operacional:** Windows 10/11 (com permissões de administrador para algumas funcionalidades).
- **Python:** Versão 3.8 ou superior.
- **Dependências:** Certifique-se de instalar os pacotes necessários.

---

## Instalação

### Passo 1: Clone o Repositório

Clone este repositório para o seu computador:

```bash
git clone https://github.com/seuusuario/gerenciador-funcoes-windows.git
cd gerenciador-funcoes-windows
```

### Passo 2: Instale as Dependências

Use o pip para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### Passo 3: Execute o Programa

Inicie o programa com:

```bash
python app.py
```

---

## Estrutura do Projeto

```plaintext
gerenciador-funcoes-windows/
├── app.py                  # Arquivo principal que inicializa o programa
├── interface.py            # Gerencia a interface gráfica
├── funcoes/
│   ├── __init__.py         # Arquivo de inicialização do módulo
│   ├── desinstalador.py    # Função para desinstalar aplicativos padrão
│   ├── utilitarios.py      # Funções utilitárias como ping, IP fixo e rede
├── requirements.txt        # Lista de dependências do projeto
└── README.md               # Documentação do projeto
```

---

## Como Usar o Programa

1. **Execute o programa:** Ao abrir, a interface gráfica será exibida com várias opções de funcionalidades.
2. **Escolha uma função:**
   - Para desinstalar aplicativos padrão, clique no botão **"Desinstalar aplicativos padrão"**.
   - Para instalar programas úteis, clique em **"Instalar programas úteis"**.
   - Para testar a conectividade, clique em **"Pingar um endereço"**.
   - Para configurar IP fixo, clique em **"Configurar IP fixo"** e preencha os campos solicitados.
3. **Visualize os resultados:** A maioria das ações mostra resultados diretamente na interface ou no terminal.

---

## Possíveis Problemas e Soluções

- **Erro ****\`\`****:** Certifique-se de ter instalado as dependências usando:
  ```bash
  pip install -r requirements.txt
  ```
- **Permissões de administrador:** Algumas funções, como desinstalar aplicativos padrão ou configurar IP fixo, exigem prívilegios de administrador.
- **Problemas ao configurar IP fixo:** Verifique se o adaptador de rede é reconhecido como "Ethernet" ou ajuste o nome do adaptador diretamente no código (`configurar_ip_fixo`).

---

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. **Faça um fork do repositório.**
2. **Crie uma branch para sua funcionalidade/ajuste:**
   ```bash
   git checkout -b minha-funcionalidade
   ```
3. **Faça suas alterações e realize o commit:**
   ```bash
   git commit -m "Descrição da mudança"
   ```
4. **Envie para o seu fork:**
   ```bash
   git push origin minha-funcionalidade
   ```
5. **Abra um Pull Request.**

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para usar, modificar e distribuir.

---

## Notas Adicionais

- Este programa foi testado em Windows 10 e 11.
- A interface gráfica foi desenvolvida com `tkinter` para simplicidade e compatibilidade.
- Em caso de dúvidas ou problemas, abra uma [issue](https://github.com/seuusuario/gerenciador-funcoes-windows/issues).

**Desenvolvido por:** GabrielKS 😊

