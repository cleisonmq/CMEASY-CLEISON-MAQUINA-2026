# Versão 0.1v
# Create By Cleison Máquina

import subprocess
import shutil

# 1.4. Btn Voltar
def voltar ():
    input("Pressione <ENTER> para continuar")
    subprocess.run(["clear"])
# 1. Menu Principal
def menu_principal ():
    print("+----------------------------------------------------+")
    print("|                    - CMEasy -                      |")
    print("+----------------------------------------------------+")
    print("|                     M E N U                        |")
    print("+----------------------------------------------------+")
    print("| 1. Instalar Promagramas                            |")
    print("| 2. Executar comandos                               |")
    print("| 3. Imformacao                                      |")
    print("| 4. Encerrar o programa                             |")
    print("+----------------------------------------------------+")
#-------------------------------------------------
#--- 1.1. Menu Instalacao de programas
def menu_instalar_programa ():
    print("+----------------------------------------------------+")
    print("|               DISTRIBUÇÃO LINUX                    |")
    print("+----------------------------------------------------+")
    print("| 1. Familia Debian (Ubunto, Kali Linux...)          |")
    print("| 2. Familia Red Hat (Rocky Linux, Cent OS...)       |")
    print("| 3. Familia Arch (Arch Linux, Manjaro...)           |")
    print("| 4. Voltar                                          |")
    print("+----------------------------------------------------+")
#-------- 1.1.1. Menu Tipo de SO
def menu_tipo_de_software ():
    print("+----------------------------------------------------+")
    print("|                TIPO DE SOFTWARE                    |")
    print("+----------------------------------------------------+")
    print("+----------------------------------------------------+")
    print("| 1. Ciberseguranca                                  |")
    print("| 2. Programacao                                     |")
    print("| 3. voltar                                          |")
    print("+----------------------------------------------------+")   
#-------- 1.1.2. Menu Programas disponiveis
def menu_progamas_disponiveis ():
    print("+----------------------------------------------------+")
    print("|                      SOFTWARE                      |")
    print("+----------------------------------------------------+")
    print("+----------------------------------------------------+")
    print("| 1. Fail2ban                                        |")
    print("| 2. Snort                                           |")
    print("| 3. Sair                                            |")
    print("+----------------------------------------------------+")   
#--- 1.2. Menu Execucao de comandos
def menu_executar_comandos ():
    print("+------------------------------------------------------------+")
    print("|                        O P C O E S                         |")
    print("+------------------------------------------------------------+")
    print("| 1.  | Alterar permissões de arquivos e pastas.             |")
    print("| 2.  | Alterar a senha de um usuário.                       |")
    print("| 3.  | Ajustar relógio do sistema.                          |")
    print("| 4.  | Atualizar todos os programas instalados.             |")
    #print(| 5.  | Copiar saída de comando para arquivo.                |")   " – Comando > Arquivo.txt – FIGURA 10")
    print("| 6.  | Desinstalar pacotes e limpar dependências.           |")
    #print("| 7. | Encadear comandos usando pipe.                       |")     " – | – FIGURA 21")
    print("| 8.  | Entrar como root.                                    |")
    #print("| 9. | Executar arquivo ou script.                          |")  python nome_do_arquivo.py – N/A")
    print("| 10. | Extrair arquivos .tar.                               |")
    print("| 11. | Extrair arquivos .tar.gz.                            |")
    #print("| 12. | Extrair partes específicas de um texto.             |")    – cut -d ':' -f 1 -c 1 – FIGURA 22")
    print("| 13. | Informações de rede e interfaces.                    |")
    print("| 14. | Informações do sistema completo.                     |")
    print("| 15. | Localizar arquivos no sistema.                       |") 
    print("| 16. | Listar arquivos e pastas de um diretório.            |")   
    print("| 17. | Listar arquivos e pastas de um diretório especifico. |")  
    print("| 18. | Nome de usuário atual.                               |")   
    #print("| 19. | Procurar texto em arquivos.                         |")    grep 'filtro' – FIGURA 19")
    print("| 20. | Virar root.                                          |")   
    #print("| 21. | Ver número de linhas no final do arquivo.           |")   tail -n 20 [arquivo.txt] – FIGURA 18")
    #print("| 22. | Ver arquivo em tempo real enquanto é atualizado.    |")   tail -f [arquivo.txt] – FIGURA 18")
    #print("| 23. | Verificar portas abertas.                           |")   netstat -nlp – FIGURA 23")
    #print("| 24. | Ver portas TCP abertas.                             |")   netstat -nlpt – FIGURA 23")
    #print("| 25. | Ver portas UDP abertas.                             |")   netstat -nlpu – FIGURA 23")
    #print("| 26. | Visualizar conteúdo de um arquivo.                  |")   cat [FICHEIRO] – FIGURA 12")
    print("+------------------------------------------------------------+")
    print("|                       30. S A I R                          |")
    print("+------------------------------------------------------------+")
 
    #print("14. Filtrar múltiplos padrões em arquivos (egrep) – egrep 'filtro1 | filtro2' – FIGURA 20")
    #print("15. Imprimir texto no terminal – echo 'texto de saída' – FIGURA 9")
    #print("22. Pesquisar exploits por serviço e versão – searchsploit [serviço] [versão] – N/A")
    #print("26. Ver últimas linhas de um arquivo – tail [Arquivo.txt] – FIGURA 18")
#--- 1.3. Menu Informacao
def informacao ():
    print("+-------------------------------------------------------+")
    print("|                 I N F O R M A C A O                   |")
    print("+-------------------------------------------------------+")
    print("| Nome: CMEasy                                          |")
    print("| Criador: Cleison Maquina (Tecnico de Ciberseguranca)  |")
    print("| Ano de Criacao: 2026                                  |")
    print("| Linguagem de Programacao: Python                      |")
    print("| Versao: 0.1v                                          |")
    print("| Descricao: Automatizacao de processos refente a       |")
    print("|instalacao de programas e execusao de comandos.        |")
    print("+-------------------------------------------------------+")
    print("|PRESSIONE <ENTER> PARA SAIR                            |")
    print("+-------------------------------------------------------+")
#------------------------------------------------

#Progamas disponiveis 
#----------------------------- Fail2Ban ---------------------------------------
#-------- Menu Principal
def fail2ban_menu1 ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                FAIL2BAN                                     |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | O Fail2Ban é uma ferramenta que protege servidores contraataques.|")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Proteger SSH                                                   |")
    print("|          | - Proteger sites (Apache/Nginx)                                  |")
    print("| Funções  | - Proteger serviços de email                                     |")
    print("|          | - Bloquear IPs automaticamente                                   |")
    print("|          | - Monitorar atividades suspeitas                                 |")
    print("|-----------------------------------------------------------------------------|")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+-----------------------------------------------------------------------------+")
    print("|          4. Configuracoes           |               5. Sair                 |")
    print("+-----------------------------------------------------------------------------+")
#-------- Menu comandos
def fail2ban_menu2 ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                FAIL2BAN                                     |")
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Ativar                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Iniciar                                                                |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar                                                                  |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar                                                              |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Ver IP'S Banidos                                                       |")
    print("+----+------------------------------------------------------------------------+")
    print("| 8. | Liberar IP                                                             |")
    print("+----+------------------------------------------------------------------------+")
    print("| 9. | Sair                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
#-------- Instalacao do Fail2Ban
def fail2ban_instalacao ():
    try:
        #--------------------- Atualizar pacotes
        print("|---------------------------- Atualizando os pacotes  ------------------------------|")
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
        #--------------------- Instalando o iptables
        print("|-------------------------- Instalando Pre-requisitos ------------------------------|")
        subprocess.run(["sudo", "apt", "install", "-y", "iptables"], check=True)
        print("|--------------------- Pre-requisitos instalados com sucesso -----------------------|")
        #-------------------- Instalar fail2ban
        print("|---------------------------- Instalando o Fail2Ban --------------------------------|")
        subprocess.run(["sudo", "apt", "install", "-y", "fail2ban"], check=True)
        print("|----------------------- Fail2ban instalado com sucesso ----------------------------|")
        #-------------------- Copia do arquivo de configuracao 
        print("|----------------------- Preparando o arquivo de configuracao ----------------------|")
        subprocess.run(["sudo", "cp", "/etc/fail2ban/jail.conf", "/etc/fail2ban/jail.local"], check=True)
        print("|--------------------- Arquivo de configuracao preparado ---------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    voltar ()
#-------- Comandos
def enable_fail2ban ():
    # Ativação do serviço
    subprocess.run(["sudo", "systemctl", "enable", "fail2ban.service"], check=True)
    print("+---------------------------------------------------------------------------------+")
    print("|-----------------------Fail2ban ativado com sucesso------------------------------|")
    print("+---------------------------------------------------------------------------------+")
    voltar ()
def start_fail2ban ():
    # Iniciação do serviço
    subprocess.run(["sudo", "systemctl", "start", "fail2ban.service"], check=True)
    print("+---------------------------------------------------------------------------------+")
    print("|-----------------------Fail2ban iniciado com sucesso-----------------------------|")
    print("+---------------------------------------------------------------------------------+")
    voltar ()
def status_fail2ban ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "fail2ban.service"], check=True)
    voltar ()
def stop_fail2ban ():
    # Ativação do serviço
    subprocess.run(["sudo", "systemctl", "stop", "fail2ban.service"], check=True)
    print("+------------------------------------------------------------------------------------+")
    print("|-----------------------Fail2ban foi parado com sucesso------------------------------|")
    print("+------------------------------------------------------------------------------------+")
    voltar()
def restart_fail2ban ():
    # Reativacao do serviço
    subprocess.run(["sudo", "systemctl", "restart", "fail2ban.service"], check=True)
    print("+---------------------------------------------------------------------------------+")
    print("|-----------------------Fail2ban reativado com sucesso----------------------------|")
    print("+---------------------------------------------------------------------------------+")
def version_fail2ban ():
    # versao do serviço
    subprocess.run(["sudo", "fail2ban-client", "--version"], check=True)
    voltar ()
def remove_fail2ban ():
    try:
        # Verifica se o fail2ban-client existe no sistema
        if shutil.which("fail2ban-client") is None:
            print("+-------------------------------------------------------------------------------+")
            print("|-------------------O fail2ban nao existe nesta maquina-------------------------|")
            print("+-------------------------------------------------------------------------------+")
            return  # Se o Fail2Ban não existir, não faz sentido continuar com a remoção
        else:
            stop_fail2ban()
            subprocess.run(["sudo", "apt", "remove", "--purge", "fail2ban", "-y"], check=True)
            subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/etc/fail2ban"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/var/log/fail2ban*"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/var/lib/fail2ban"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/run/fail2ban"], check=True)
            subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
            try:
                saida = subprocess.run(["fail2ban-client", "-V"], capture_output=True, text=True)
                
                # Se o comando for bem-sucedido (returncode == 0)
                if saida.returncode == 0:
                    print("+-------------------------------------------------------------------------------+")
                    print("|----------------------------Desinstalacao bem sucedida------------------------|")
                    print("+-------------------------------------------------------------------------------+")
                else:
                    # Se o código de retorno for diferente de 0, indica erro na execução
                    print(f"Ainda existem traços do programa. ERRO: {saida.stderr}")
                    
            except FileNotFoundError:
                # Caso o comando fail2ban-client não exista no sistema
                print("+-------------------------------------------------------------------------------+")
                print("|----------------------------Desinstalacao bem sucedida------------------------|")
                print("+-------------------------------------------------------------------------------+")            
    except FileNotFoundError:
        # Caso o comando fail2ban-client não exista no sistema
        print("+-------------------------------------------------------------------------------+")
        print("|-------------------O fail2ban nao existe nesta maquina-------------------------|")
        print("+-------------------------------------------------------------------------------+")
    voltar ()
def ver_ip_banido ():
    print("|----------------------- IP'S Banidos ------------------------------|")
    subprocess.run(["sudo", "iptables", "-L", "-n", "--line"], check=True)
    voltar ()
def liberar_ip ():
    ip = input ("indique o ip que deseja liberar")
    subprocess.run(["sudo", "iptables", "-D", "f2b-sshd", ip], check=True)
    print("|----------------------- IP'S Banidos ------------------------------|")
    voltar ()
#--- Menu configuracoes fail2ban
def fail2ban_menu_conf ():
    print("+----------------------------------------------------------------------------------+")
    print("|                                FAIL2BAN - Conf                                   |")
    print("+----------------------------------------------------------------------------------+")
    print("| 1. | Configuração do Fail2Ban para Proteção contra Ataques de Força Bruta no SSH.|")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 2. | Entrar no arquivo de configuracao.                                          |")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 3. | Sair.                                                                       |")
    print("+----------------------------------------------------------------------------------+")
#------- Tutorial de configuracoes
def fail2ban_conf_ssh ():
    print("+----------------------------------------------------------------------------------+")
    print("|                             CMEasy - FAIL2BAN - Conf                             |")
    print("+----------------------------------------------------------------------------------+")
    print("| 1. | Configuração do Fail2Ban para Proteção contra Ataques de Força Bruta no SSH.|")
    print("+----------------------------------------------------------------------------------+")
    print("| [sshd]                                                                           |")
    print("| enabled = true                                                                   |")
    print("| port = ssh                                                                       |")
    print("| filter = sshd                                                                    |")
    print("| logpath = /var/log/auth.log                                                      |")
    print("| bantime = 900                                                                    |")
    print("| banaction = iptables-allports                                                    |")
    print("| findtime = 900                                                                   |")
    print("| maxretry = 3                                                                     |")
    print("|----------------------------------------------------------------------------------|")
    print("| OBS: Copie e cole o codigo no arquivo de configuracao.| Clique <ENTER> para sair |")
    print("+----------------------------------------------------------------------------------+")
    voltar ()
#------- Configuracao do fail2ban
def fail2ban_conf ():
    while True: 
        fail2ban_menu_conf ()
        opcao= input("Indique a sua opcao: ")
        escolha= int (opcao)
        subprocess.run(["clear"])
        match escolha:
            case 1:
                fail2ban_conf_ssh () 
            case 2:
                try:
                    #--------------------- Editar o arquivo de configuracao
                    subprocess.run(["sudo", "nano", "/etc/fail2ban/jail.local"], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Ocorreu um erro ao executar o comando: {e}")
                    voltar ()
            case 3:
                voltar ()
                break
#------------------------------------------------------------------------------

#---------------------------- Snort--------------------------------------------
#--- Menu Snort Principal
def snort_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                   SNORT                                     |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | O Snort é um sistema de segurança de rede que detecta e bloqueia |")
    print("|          |ataques em tempo real.                                            |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Detecção e prevenção de intrusões (IDS/IPS)                    |")
    print("|          | - Análise de Comportamento e Anomalias                           |")
    print("| Funções  | - Registro e Armazenamento de Logs                               |")
    print("|          | - Inspeção Profunda de Pacotes (DPI - Deep Packet Inspection)    |")
    print("|          | - Detecção de Explorações de Vulnerabilidades (Exploits)         |")
    print("+----------+------------------------------------------------------------------+")
    print("| Requisi- | RAM: 4GB (Minimo)                                                |")
    print("| tos      | CPU: Arquitetura Moderna                                         |")
    print("|-----------------------------------------------------------------------------|")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+-----------------------------------------------------------------------------+")
    print("|          4. Configuracoes           |               5. Sair                 |")
    print("+-----------------------------------------------------------------------------+")   
#-------- Menu Snort comandos
def snort_menu_comandos ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                  SNORT                                      |")
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Ativar                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Iniciar                                                                |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar                                                                  |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar                                                              |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Sair                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
#--- Menu configuracoes fail2ban
def snort_menu_conf ():
    print("+----------------------------------------------------------------------------------+")
    print("|                                  SNORT - Conf                                    |")
    print("+----------------------------------------------------------------------------------+")
    print("| 1. | Regras que podem ser aplicadas.                                             |")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 2. | Entrar no arquivo de configuracao.                                          |")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 3. | Sair.                                                                       |")
    print("+----------------------------------------------------------------------------------+")
#--------- Regras que podemos aplicar
def snort_menu_conf_rules ():
    print("+-------------------------------------------------------------------------------------------------+")
    print("|                                  SNORT - Regras                                                 |")
    print("+-------------------------------------------------------------------------------------------------+")
    print("| 1. | Tentativas de acesso FTP.                                                                  |")
    print("+-------------------------------------------------------------------------------------------------+")
    print('| alert tcp any any -> any 21 (msg:"Tentativa de intrusao por FTP!"; sid:1000001;)                |')
    print("+-------------------------------------------------------------------------------------------------+")
    print("| 2. | Tentativa de acesso por TELNET                                                             |")
    print("+-------------------------------------------------------------------------------------------------+")
    print('| alert tcp $EXTERNAL_NET any -> $HOME_NET 23 (msg:"tentativa exterior TELNET !"; sid:1000002;)   |')
    print("+-------------------------------------------------------------------------------------------------+")
    print("| 3. | Tentativa de Ping                                                                          |")
    print("+-------------------------------------------------------------------------------------------------+")
    print('| alert icmp $EXTERNAL_NET any -> $HOME_NET any (msg:"Estamos a ser pingados !"; sid:1000004;)    |')
    print("+-------------------------------------------------------------------------------------------------+")
    print("| 4. | Aceder ao arquivo de configuracao                                                          |")
    print("+-------------------------------------------------------------------------------------------------+")
    print("| 5. | Sair.                                                                                      |")
    print("+-------------------------------------------------------------------------------------------------+")
    print("| Copie a regra e cole no arquivo de configuracao, de seguida ative ela escolendo a opcao.        |")
    print("+-------------------------------------------------------------------------------------------------+")

def rules_snort ():
    while True:
        snort_menu_conf_rules ()
        opcao= input ("Escolha a sua opcao: ")
        escolha= int (opcao)
        match escolha:
            case 1:
                try:
                    int_rede= input ("Qual e a sua interfaze de rede")
                    subprocess.run(["sudo", "snort", "-q", "-l", "/var/log/snort", "-I", int_rede, "-A", "console", "-c", "/etc/snort/snort.conf"], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Ocorreu um erro ao executar o comando: {e}")

def snort_conf ():
    
    subprocess.run(["sudo", "nano", "/etc/snort/snort.conf"], check=True)
#-------- Instalacao do snort
def snort_instalacao ():
    try:
        #Atualizacao das dependencias
        print ("|---------------------Atualizando pacotes------------------------|")
        subprocess.run(["sudo", "apt", "update"], check=True)
        print ("|--------------Pacotes actualizados com sucesso------------------|")
        #Instalacao das dependencias do snort
        print("|------------------ Instalasndo dependencias ---------------------|")
        subprocess.run(["sudo", "apt", "install", "-y", "build-essential", "libpcap-dev", "libpcre3-dev", "libdumbnet-dev",
        "bison", "flex", "zlib1g-dev"], check=True)
        print("|-------------Dependencias instaladas com sucesso----------------|")
        #Instalacao do snort
        print("|----------------------- Instalando o Snort ---------------------|")
        subprocess.run(["sudo", "apt", "install", "snort", "-y"], check=True)
        subprocess.run(["sudo","snort", "-V"], check=True)
        print("|------------------Snort instalado com sucesso-------------------|")
        #Ativacao do modo promiscuo
        print("|--------------------------- Ativando do modo promisco ------------------------------|")
        subprocess.run(["ip", "a"])
        interface_de_rede = input("Indique a sua interface de rede: ")
        subprocess.run(["sudo", "ip", "link", "set", interface_de_rede, "promisc", "on"], check=True)
        print("|------------------------- Modo proviscuo Ativado ----------------------------------|")
        print("|--------------Caso for uma VM ative-o nas definicoes de rede ----------------------|")
        print("|------------------- Instalacao concluida com sucesso ------------------------------|")
        print("|------------ Agura deve proceder a configuracao do snort --------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    voltar ()
#--- Comandos
def enable_snort ():
    # Ativação do serviço
    print("|----------------------------- Ativando o snort ------------------------------------|")
    subprocess.run(["sudo", "systemctl", "enable", "snort"], check=True)
    print("|------------------------ Snort ativado com sucesso --------------------------------|")
    voltar ()
def start_snort ():
    # Iniciação do serviço
    print("|----------------------------- Iniciando o snort ------------------------------------|")
    subprocess.run(["sudo", "systemctl", "start", "snort"], check=True)
    print("|------------------------ Snort Iniciado com sucesso --------------------------------|")
    voltar ()
def status_snort ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "snort"], check=True)
    voltar ()
def stop_snort ():
    # parar do serviço
    print("|----------------------------- Parando o snort ------------------------------------|")
    subprocess.run(["sudo", "systemctl", "stop", "snort"], check=True)
    print("|------------------------ Snort parado com sucesso --------------------------------|")
    voltar()
def restart_snort ():
    # Reativacao do serviço
    print("|----------------------------- reiniciando o snort ------------------------------------|")
    subprocess.run(["sudo", "systemctl", "restart", "snort"], check=True)
    print("|------------------------ Snort reiniciado com sucesso --------------------------------|")
def version_snort ():
    # versao do serviço
    subprocess.run(["snort", "-V"], check=True)
    voltar ()

def remove_fail2ban ():
    try:
        # Verifica se o fail2ban-client existe no sistema
        if shutil.which("fail2ban-client") is None:
            print("+-------------------------------------------------------------------------------+")
            print("|-------------------O fail2ban nao existe nesta maquina-------------------------|")
            print("+-------------------------------------------------------------------------------+")
            return  # Se o Fail2Ban não existir, não faz sentido continuar com a remoção
        else:
            stop_fail2ban()
            subprocess.run(["sudo", "apt", "remove", "--purge", "fail2ban", "-y"], check=True)
            subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/etc/fail2ban"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/var/log/fail2ban*"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/var/lib/fail2ban"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/run/fail2ban"], check=True)
            subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
            try:
                saida = subprocess.run(["fail2ban-client", "-V"], capture_output=True, text=True)
                
                # Se o comando for bem-sucedido (returncode == 0)
                if saida.returncode == 0:
                    print("+-------------------------------------------------------------------------------+")
                    print("|----------------------------Desinstalacao bem sucedida------------------------|")
                    print("+-------------------------------------------------------------------------------+")
                else:
                    # Se o código de retorno for diferente de 0, indica erro na execução
                    print(f"Ainda existem traços do programa. ERRO: {saida.stderr}")
                    
            except FileNotFoundError:
                # Caso o comando fail2ban-client não exista no sistema
                print("+-------------------------------------------------------------------------------+")
                print("|----------------------------Desinstalacao bem sucedida------------------------|")
                print("+-------------------------------------------------------------------------------+")            
    except FileNotFoundError:
        # Caso o comando fail2ban-client não exista no sistema
        print("+-------------------------------------------------------------------------------+")
        print("|-------------------O fail2ban nao existe nesta maquina-------------------------|")
        print("+-------------------------------------------------------------------------------+")
    voltar ()


















    
#1. Comandos de permicao
def menu_permisions_type ():
    print("+----------------------------------------+")
    print("|            O P C O E S                 |")
    print("+----------------------------------------+")
    print("|1. Permissão de leitura (read)          |")
    print("|2. Permissão de escrita (write).        |")
    print("|3. Permissão de execução (execute).     |")
    print("|4. Remover permissão de leitura.        |")
    print("|5. Remover permissão de escrita.        |")
    print("|6. Remover permissão de execução.       |")
    print("|7. Sair.                                |")
    print("+----------------------------------------+")
def cmd_permisions_user ():
                while True:
                    menu_permisions_type ()
                    opcao_permition2 = input ("Selecione a sua escolhe: ")
                    escolha_permition2 = int(opcao_permition2)
                    match escolha_permition2:
                        case 1:
                            arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                            subprocess.run(["chmod", "+r", arquivo_pasta])
                            print("|------------Comando executado com sucesso--------------|")
                            voltar ()
                        case 2:
                            arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                            subprocess.run(["chmod", "+w", arquivo_pasta])
                            print("|------------Comando executado com sucesso--------------|")
                            voltar ()
                        case 3:
                            arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                            subprocess.run(["chmod", "+x", arquivo_pasta])
                            print("|------------Comando executado com sucesso--------------|")
                            voltar ()
                        case 4:
                            arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                            subprocess.run(["chmod", "-x", arquivo_pasta])
                            print("|------------Comando executado com sucesso--------------|")
                        case 5:
                            arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                            subprocess.run(["chmod", "-r", arquivo_pasta])
                            print("|------------Comando executado com sucesso--------------|")
                            voltar ()
                        case 6:
                            arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                            subprocess.run(["chmod", "-w", arquivo_pasta])
                            print("|------------Comando executado com sucesso--------------|")
                            voltar ()
                        case 7:
                            voltar ()
                            break
#2. Alterar senha de usuarios
def passwd_users ():
    userName= input("Qual e o nome do usuario: ")
    subprocess.run(["passwd", userName])
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#3. Ajuste de relogio
def time_so ():
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "dpkg-reconfigure", "tzdata"], check=True)
        subprocess.run(["sudo", "apt", "install", "chrony", "-y"], check=True)
        
        print("|------------Comando executado com sucesso--------------|")
        
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
    voltar()
#4. Atualizacao dos programas
def actu_prog ():
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#5. Copiar saída
#6. Desinstalar pacotes
def purg_prog():
    subprocess.run(["sudo", "apt", "purge", "-y"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#7. Encadear comandos
#8. Entrar como root
def root_mode():
    subprocess.run(["su", "-"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#9. Esecutar script
#10. Extrair arquivos .tar
def extrat_tar():
    arquivo_pasta= input ("Indique o camindo do arquivo: ")
    subprocess.run(["tar", "-xvf", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#11. Extrair arquivos .tar.gz
def extrat_targz():
    arquivo_pasta= input ("Indique o camindo do arquivo: ")
    subprocess.run(["tar", "-xzvf", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#12. Extrair partes específicas de um texto
#13. Informações de rede
def inf_rede ():
    subprocess.run(["ip", "a"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#14. Informacao do so
def inf_SO ():
    subprocess.run(["uname", "-a"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#15. Localizar arquivos
def local_arq ():
    arquivo_pasta= input ("Escreva o nome do arquivo: ")
    subprocess.run(["locate", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#16. Listar arquivos e pastas
def list_dir1():
    subprocess.run(["ls", "-lh"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#17. Listar arquivos e pastas especifico
def list_dir2():
    arquivo_pasta= input ("Indique o camindo da Diretoria: ")
    subprocess.run(["ls", "-lh", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#18. Nome de usuário atual
def user_name():
    subprocess.run(["whoami"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()
#19. Nome de usuário atual
#20. Virar root
def user_root():
    subprocess.run(["sudo", "su"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    voltar()


while True:
    #Consulta do menu principal
    menu_principal()
    escolha = input("Selecione a opção desejada: ")
    opcao = int(escolha)
    subprocess.run(["clear"])
    #Opcoes do menu principal
    match opcao:
        #01. Instalar Programas
        case 1: 
            while True:
                #Janela de instalacao dos programas
                menu_instalar_programa ()
                distro_linux = input("Selecione a opção desejada: ")
                familia_linux = int(distro_linux)
                subprocess.run(["clear"])
                match familia_linux:
                    case 1:
                        while True:
                            #Janela dos tipos de distribuicao Linux
                            menu_tipo_de_software ()
                            areas = input("Selecione a opção desejada: ")
                            areas_so = int(areas)
                            subprocess.run(["clear"])
                            match areas_so:
                                case 1:
                                    while True:
                                        menu_progamas_disponiveis ()
                                        programas = input("Selecione a opção desejada: ")
                                        programas_disponivel = int(programas)
                                        subprocess.run(["clear"])
                                        match programas_disponivel:
                                            #Fail2Ban -----------------
                                            case 1:
                                                while True:
                                                    #-------- Fail2Ban Menu Principal
                                                    fail2ban_menu1 ()
                                                    opcao_fai2ban = input("Selecione a opção desejada: ")
                                                    escolha_fail2ban = int(opcao_fai2ban)
                                                    subprocess.run(["clear"])
                                                    match escolha_fail2ban:                                                        
                                                        case 1:
                                                            fail2ban_instalacao ()
                                                            while True:
                                                                fail2ban_menu2 ()
                                                                opcao_fai2ban2 = input("Selecione a opção desejada: ")
                                                                escolha_fail2ban2 = int(opcao_fai2ban2)
                                                                match escolha_fail2ban2:
                                                                    case 1:
                                                                        enable_fail2ban ()                                                                          
                                                                    case 2:
                                                                        start_fail2ban ()                                                                          
                                                                    case 3: 
                                                                        status_fail2ban ()                                                                         
                                                                    case 4:
                                                                        stop_fail2ban ()                                                                         
                                                                    case 5:
                                                                        restart_fail2ban ()                                                                         
                                                                    case 6:
                                                                        version_fail2ban ()  
                                                                    case 7:
                                                                        ver_ip_banido ()
                                                                    case 8:
                                                                        liberar_ip ()                                                                       
                                                                    case 9:
                                                                        voltar ()
                                                                        break
                                                        case 2:
                                                            remove_fail2ban ()
                                                            voltar ()
                                                            break
                                                        case 3:
                                                            #-------- Fail2Ban Menu Comandos 
                                                            fail2ban_menu2 ()
                                                            opcao_fai2ban3 = input("Selecione a opção desejada: ")
                                                            escolha_fail2ban3 = int(opcao_fai2ban3)
                                                            while True:
                                                                match escolha_fail2ban3:
                                                                    case 1:
                                                                        enable_fail2ban ()
                                                                        break
                                                                    case 2:
                                                                        start_fail2ban ()
                                                                        break
                                                                    case 3: 
                                                                        status_fail2ban ()
                                                                        break
                                                                    case 4:
                                                                        stop_fail2ban ()
                                                                        break
                                                                    case 5:
                                                                        restart_fail2ban ()
                                                                        break
                                                                    case 6:
                                                                        version_fail2ban ()
                                                                        break
                                                                    case 7:
                                                                        voltar ()
                                                                        break
                                                        case 4:
                                                            fail2ban_conf ()
                                                            voltar ()
                                                        case 5:
                                                            voltar ()
                                                            break
                                            #Snort --------------- 
                                            case 2:                                                
                                                while True:
                                                    snort_menu_principal ()
                                                    opcao_snort = input("Selecione a opção desejada: ")
                                                    escolha_snort = int(opcao_snort)
                                                    match escolha_snort:
                                                        # Instalacao
                                                        case 1:
                                                            snort_instalacao ()
                                                        #Desinstalacao
                                                        #case 2:
                                                        # Comandos
                                                        case 3:
                                                            while True:
                                                                snort_menu_comandos ()
                                                                opcao = input ("Indique o seu comando: ")
                                                                escolha = int (opcao)
                                                                match escolha:
                                                                    #Ativar
                                                                    case 1:
                                                                        enable_snort()
                                                                    #Iniciar
                                                                    case 2:
                                                                        start_snort ()
                                                                    #Estado
                                                                    case 3:
                                                                        status_snort ()
                                                                    #Parar
                                                                    case 4: 
                                                                        stop_snort ()
                                                                    #Reiniciar
                                                                    case 5:
                                                                        restart_snort ()
                                                                    #Versao
                                                                    case 6:
                                                                        version_snort ()
                                                                    #Sair
                                                                    case 7 :
                                                                        voltar ()
                                                                        break
                                                        # configuracoes
                                                        case 4:
                                                            while True:
                                                                snort_menu_conf ()
                                                                opcao = input ("Indique o seu comando: ")
                                                                escolha = int (opcao)
                                                                match escolha:
                                                                    case 1:
                                                                        rules_snort ()
                                                                    case 2:
                                                                        snort_conf ()
                                                                    case 3:
                                                                        voltar ()
                                                                        break                                                        
                                                        # sair
                                                        case 5:
                                                            voltar ()
                                                            break
                                            case 3:
                                                voltar ()
                                                break   
                                
                                case 3:
                                    voltar ()
                                    break  
                    case 4:
                        voltar ()
                        break 
        case 2:
            while True:
                menu_executar_comandos ()
                opcao_comando = input("Selecione a opção desejada: ")
                escolha_comando = int(opcao_comando)
                match escolha_comando:
                    case 1:
                        cmd_permisions_user ()
                    case 2:
                        passwd_users ()
                    case 3:
                        time_so ()
                    case 4:
                        actu_prog()
                    #case 5:
                    case 6:
                        purg_prog()
                    #case 7:
                    case 8:
                        root_mode()
                    #case 9:
                    case 10:
                        extrat_tar ()
                    case 11:
                        extrat_targz ()
                    #case 12:
                    case 13:
                        inf_rede ()
                    case 14:
                        inf_SO ()
                    case 15:
                        local_arq()
                    case 16:
                        list_dir1 ()
                    case 17:
                        list_dir2 ()
                    case 18:
                        user_name ()
                    #case 19:
                    case 20:
                        user_root
                    #case 20:
                    #case 21:
                    case 30:
                        voltar()
                        break
        case 3:
            informacao ()
            voltar()
        case 4:
            print("Programa 'CMEasy' encerrado, Obrigado!")
            break  



           