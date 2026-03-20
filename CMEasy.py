# CMEasy
# Versão 0.1v
# Create By Cleison Máquina

import subprocess
import shutil
import os
import re
#--------------------> Codigos mais usados <-----------------
# Botao para quando o utilisador clicar em enter o programa limpre a tela 
def enter_clear ():
    input("Pressione [ ENTER ] para continuar")
    subprocess.run(["clear"])
# Caso o utilizador nao digite nada
def entrada_invalida1 ():
    print("|---------------- Entrada inválida, você deve escolher uma opção! ---------------------------|")
    input ("Presione [ ENTER ] para continuar... ")
# Se a conversão falhar (não for um número), exibe uma mensagem de erro
def entrada_invalida2 ():
    print("|---------------- Opção inválida! Por favor, insira um número. ---------------------------|")
    enter_clear()
# Este case captura qualquer entrada que não seja uma opção válida
def entrada_invalida3 ():
    print("|---------------- Opção inválida, tente novamente ---------------------------|")
    enter_clear ()
#------------------------------------------------------------

#-------------------------> CMEasy <-------------------------
# Menu Principal
def menu_principal ():
    print("+--------------------------------------------------------+")
    print("|                      - CMEasy -                        |")
    print("+--------------------------------------------------------+")
    print("|                       M E N U                          |")
    print("+------+-------------------------------------------------+")
    print("|  1.  | Instalar Promagramas                            |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Executar Comandos                               |")
    print("+------+-------------------------------------------------+")
    print("|  3.  | Informação                                      |")
    print("+------+-------------------------------------------------+")
    print("|  4.  | Encerrar o programa                             |")
    print("+--------------------------------------------------------+")
#------------------------------------------------------------
############################################################################

###########################################################################
#----------------> 1. Instalar Promagramas <-----------------

# Menu Principal (Tipos de distribuicao)
def menu_instalar_programas ():
    print("+--------------------------------------------------------+")
    print("|              --> INSTALAR PROGRAMAS <--                |")
    print("+--------------------------------------------------------+")
    print("|                  DISTRIBUÇÃO LINUX                     |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Familia Debian (Ubunto, Kali Linux...)          |")
    print("+------+-------------------------------------------------+")
    #print("|      | Familia Red Hat (Rocky Linux, Cent OS...)      |")
    #print("+------+-------------------------------------------------+")
    #print("|      | Familia Arch (Arch Linux, Manjaro...)           |")
    #print("+------+-------------------------------------------------+")
    print("|  2.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+")
#--- Menu Programas (Tipos de programas)
def menu_tipo_de_programa ():
    print("+--------------------------------------------------------+")
    print("|                --> TIPO DE SOFTWARE <--                |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Cibersegurança                                  |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Programação                                     |")
    print("+------+-------------------------------------------------+")
    print("|  3.  | Outros Tipos                                    |")
    print("+------+-------------------------------------------------+")
    print("|  4.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+")
#-------------------------------------------------
#------------------------> Ciberseguranca
#--- Menu programas Ciberseguranca
def menu_so_ciberseguranca ():
    print("+--------------------------------------------------------+")
    print("|               --> SO CIBERSEGURANCA <--                |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Fail2Ban                                        |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Snort                                           |")
    print("+------+-------------------------------------------------+")
    print("|  3.  | Proxy Squid                                     |")
    print("+------+-------------------------------------------------+")
    print("|  4.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+") 
#---> Fail2Ban <---
# Menu principal
def fail2ban_menu_principal ():
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
    print("|----------+------------------------------------------------------------------+")
    print("|  Testes  | Ubunto (v22.04), Devian (13).                                    |")
    print("|-----------------------------------------------------------------------------+")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+------------------------+---------------------------+------------------------+")
    print("|    4. Configuracoes    |       5. Alertas          |        6. Sair         |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
#---> 1. Comandos
# Menu Principal
def fail2ban_menu_comandos ():
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
    print("| 8. | Banir Host                                                             |")
    print("+----+------------------------------------------------------------------------+")
    print("| 10.| Sair                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
# Comandos
def enable_fail2ban ():
    # Ativação do serviço
    print("|-----------------------> Ativando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "enable", "fail2ban.service"], check=True)
    print("|-----------------------> Fail2ban ativado com sucesso <------------------------------|")
    enter_clear ()
def start_fail2ban ():
    # Iniciação do serviço
    print("|-----------------------> Iniciando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "start", "fail2ban.service"], check=True)
    print("|-----------------------> Fail2ban iniciado com sucesso <-----------------------------|")
    enter_clear ()
def status_fail2ban ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "fail2ban.service"])
    enter_clear ()
def stop_fail2ban ():
    # Ativação do serviço
    print("|-----------------------> Parando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "stop", "fail2ban.service"], check=True)
    print("|-----------------------> Fail2ban foi parado com sucesso <------------------------------|")
    enter_clear()
def restart_fail2ban ():
    # Reativacao do serviço
    print("|-----------------------> Reiniciando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "restart", "fail2ban.service"], check=True)
    print("|-----------------------> Fail2ban reiniciado com sucesso <----------------------------|")
def version_fail2ban ():
    # versao do serviço
    subprocess.run(["sudo", "fail2ban-client", "--version"], check=True)
    enter_clear ()
def fail2ban_banir_ip ():
    ip = input ("indique o ip que deseja banir: ")
    subprocess.run(["sudo", "fail2ban-client," "set", "sshd", "banip", ip], check=True)
    print (f"O Host {ip} Foi banido")
def ver_ip_banido ():
    print("|----------------------- IP'S Banidos ------------------------------|")
    subprocess.run(["sudo", "iptables", "-L", "-n", "--line"], check=True)
    enter_clear ()
def liberar_ip ():
    ip = input ("indique o ip que deseja liberar: ")
    id = input ("indique o id que deseja liberar: ")
    subprocess.run(["sudo", "iptables", "-D", "f2b-sshd", id], check=True)
    subprocess.run(["sudo", "fail2ban-client", "set", "sshd", "unbanip", ip], check=True)
    print('|--------------------------- Host liberado -------------------------|')
    enter_clear ()
def fail2ban_banir_ip ():
    ip = input ("indique o ip que deseja banir: ")
    subprocess.run(["sudo", "fail2ban-client," "set", "sshd", "banip", ip], check=True)
    print (f"O Host {ip} Foi banido")
#---> 2. Instalar
def fail2ban_instalacao():
    try:
        # Verificando se o fail2ban já está instalado
        print("|---------------------------- Verificando se o Fail2Ban já está instalado ---------------------------|")
        result = subprocess.run(["dpkg", "-l", "fail2ban"], capture_output=True, text=True)
        
        if "fail2ban" in result.stdout:
            print("|---------------------------- Fail2Ban já está instalado ----------------------------|")
        else:
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
    enter_clear () 
#---> 3. Desinstalar
def fail2ban_remove ():
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
    enter_clear ()
#---> 4. Ver Logs
def fail2ban_logs ():
    print ("|------------ Viusalizaras as ultimas 20 linhas de log em tempo real ----------------|")
    subprocess.run(["sudo", "tail", "-f", "n20", "/var/log/fail2ban.log"], check=True)
#---> 5. Configuracoes
def fail2ban_menu_conf ():
    print("+----------------------------------------------------------------------------------+")
    print("|                                FAIL2BAN - Conf                                   |")
    print("+----------------------------------------------------------------------------------+")
    print("| 1. | Configuração do Fail2Ban para Proteção contra Ataques de Força Bruta no SSH.|")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 2. | Entrar no arquivo de configuracao.                                          |")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 3. | Verificar erro.                                                             |")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 4. | Sair.                                                                       |")
    print("+----------------------------------------------------------------------------------+")
    print("|                                    - CMEasy -                                    |")
    print("+----------------------------------------------------------------------------------+")
#------- Tutorial de configuracoes
# Tutorial configuracao ssh
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
    print("| Copie e cole o codigo no arquivo de configuracao.                                |")
    print("| ATENCAO: Só pode existir UMA seção [sshd] neste arquivo.                         |")
    print(r'| Verificar duplicação com: grep -n "\[sshd\]" /etc/fail2ban/jail.local           |')
    print("+----------------------------------------------------------------------------------+")
    print("|                            Clique <ENTER> para sair                              |")
    print("+----------------------------------------------------------------------------------+")
    enter_clear ()
#-------------------------------------------------
def fail2ban_arquivo_conf ():
    try:
    #--------------------- Editar o arquivo de configuracao
        subprocess.run(["sudo", "nano", "/etc/fail2ban/jail.local"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        enter_clear ()
# Verificar erros no arquivo de configuracao 
def fail2ban_erro_arquivo_conf ():
    print ("|------------------ Erros ----------------------------------|")
    subprocess.run(["sudo", "fail2ban-server", "-t"], check=True)
    enter_clear ()
# Programa Fail2Ban
def fail2ban ():
    while True:
        subprocess.run(["clear"])
        fail2ban_menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    # Instalar o Fail2Ban  
                    case 1:
                        fail2ban_instalacao()
                        continue
                    # Desinstalar Fail2Ban
                    case 2:
                        fail2ban_remove ()
                        continue
                    # Comandos Fail2Ban
                    case 3:
                        while True:
                            subprocess.run(["clear"])
                            fail2ban_menu_comandos ()
                            escolha = input ("Escolha uma das opções acima: ")
                            if escolha == "":
                                entrada_invalida1 ()
                                continue
                            else:
                                try:
                                    opcao = int (escolha)
                                    match opcao:
                                        # Ativar  
                                        case 1:
                                            enable_fail2ban ()
                                            continue
                                        # Iniciar
                                        case 2:
                                            start_fail2ban ()
                                            continue
                                        # Estado
                                        case 3:
                                            status_fail2ban ()                                                                                                                            
                                            continue                                                                                                                       
                                        # Parar
                                        case 4:
                                            stop_fail2ban ()
                                            continue   
                                        # Reiniciar                                                                                                                        
                                        case 5:
                                            restart_fail2ban ()
                                            continue
                                        # Versao
                                        case 6:
                                            version_fail2ban ()
                                            continue
                                        # Ver IP'S Banidos
                                        case 7:
                                            ver_ip_banido()
                                            continue
                                        # Liberar IP  
                                        case 8:
                                            liberar_ip ()
                                            compile
                                        # Banir Host
                                        case 9:
                                            fail2ban_banir_ip ()
                                            continue
                                        # Voltar ao menu anterior
                                        case 10:
                                            break
                                        case _:
                                            entrada_invalida3 ()
                                            continue
                                except ValueError:
                                    entrada_invalida2 ()
                                    continue
                    # Configuracoes Fail2Ban
                    case 4:
                        while True:
                            subprocess.run(["clear"])
                            fail2ban_menu_conf ()
                            escolha = input ("Escolha uma das opções acima: ")
                            if escolha == "":
                                entrada_invalida1 ()
                                continue
                            else:
                                try:
                                    opcao = int (escolha)
                                    match opcao:
                                        # turorial conf ssh  
                                        case 1:
                                            subprocess.run(["clear"])
                                            fail2ban_conf_ssh ()
                                            continue
                                        # Arquivo de configuracao
                                        case 2:
                                            fail2ban_arquivo_conf ()
                                            continue
                                        # Verificar erros
                                        case 3:
                                            fail2ban_erro_arquivo_conf ()
                                            continue
                                        #voltar 
                                        case 4:
                                            break
                                        case _:
                                            entrada_invalida3 ()
                                            continue
                                except ValueError:
                                    entrada_invalida2 ()
                                    continue
                    # Ver Logs Fail2Ban
                    case 5:
                        fail2ban_logs ()
                        continue
                    # Voltar ao menu anterior
                    case 6:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#-------------------------------------------------------------
#-------------------------------------------------------------
#---> Snort <---
# Menu Principal
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
    print("|tos       | CPU: Arquitetura Moderna                                         |")
    print("|-----------------------------------------------------------------------------|")
    print("| Site ofi-| Link: https://www.snort.org/downloads#snort3-downloads           |")
    print("|cial      | Link: www.snort.org                                              |")
    print("|-----------------------------------------------------------------------------|")
    print("|  Testes  | Ubunto (v22).                                                    |")
    print("|-----------------------------------------------------------------------------+")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+------------------------+---------------------------+------------------------+")
    print("|    4. Configuracoes    |          5. Logs          |        6. Sair         |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
#---> 1. Instalar
def snort_menu_instalacao ():
    print("+-----------------------------------------------------------------------------+")
    print("|                             INSTALACAO - SNORT                              |")
    print("+-----------------------------------------------------------------------------+")
    print("| Recomendacao: Inicie o CMEasy na diretoria de download para esta operacao.  |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Instalar com link de download do site oficial.                         |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Instalar o versao disponivel no CMEasy.                                |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Instalar a partir dos repositorios da distro (Ubunto/Debian).          |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Voltar.                                                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def snort_instalacao1():
    result = subprocess.run(["dpkg", "-l", "snort"], capture_output=True, text=True)        
    if "snort" in result.stdout:
        print("|---------------------------- snort já está instalado ----------------------------|")
    else:
        try:
            snort_link = input ("Cole o link de download do site oficial: ")
            # Atualizar os pacotes do so
            print ("|---------------------Atualizando pacotes------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "wget"], check=True)
            print ("|--------------Pacotes actualizados com sucesso------------------|")
            # instalacao das dependencias
            print("|---------------------------- Instalando as dependencias necessarias ---------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "build-essential", "libpcap-dev", "libpcre3-dev", "libdumbnet-dev", "bison", "flex", "zlib1g-dev"], capture_output=True, text=True)
            print("|---------------------------- Dependencias instaladas com sucesso ---------------------------|")
            # Download
            print("|---------------------------- Baixando o snort ---------------------------|")
            subprocess.run(["sudo", "wget", snort_link], check=True)
            print("|---------------------------- Download concluido ---------------------------|")
            # Extracao do arquivo
            snort_arquivo1 = input(r"Indique o nome do arquivo baixado -> 'nome.tar.gz' <-: ")
            print("|---------------------------- Extraindo o arquivo ---------------------------|")
            subprocess.run(["sudo", "tar", "-xvzf", snort_arquivo1], check=True)
            print("|---------------------------- Arquivo extraido ---------------------------|")
            snort_arquivo2 = input("Indique o nome do arquivo ja extraido: ")
            subprocess.run(["cd", snort_arquivo2], check=True)
            print("|---------------------------- Configurando a compilacao ---------------------------|")        
            subprocess.run(["sudo", "./configure"], check=True)
            print("|---------------------------- Compilacao Configurada ---------------------------|")
            print("|---------------------------- Compilando programa ---------------------------|")
            subprocess.run(["make"], check=True)
            print("|---------------------------- Programa Compilado ---------------------------|")
            print("|---------------------------- Instalando o programa no sistema ---------------------------|")
            subprocess.run(["sudo", "make", "install"], check=True)
            print("|---------------------------- Snort Instalado com sucesso ---------------------------|")
            print("|---------------------------- Criando os arquivos de configuracao ---------------------------|")
            subprocess.run(["sudo", "mkdir", "/etc/snort"], check=True)
            subprocess.run(["sudo", "mkdir", "/etc/snort/rules"], check=True)
            subprocess.run(["sudo", "mkdir", "/var/log/snort"], check=True)
            print("|---------------------------- Criando copias dos arquivos de configuracao ---------------------------|")
            subprocess.run(["sudo", "cp", "etc/*.conf*", "/etc/snort/"], check=True)
            subprocess.run(["sudo", "cp", "etc/*.map", "/etc/snort/"], check=True)
            print("|---------------------------- Snort pronto para ser utilizado ---------------------------|")
            subprocess.run(["snort", "-v"])
            enter_clear ()
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
def snort_instalacao2():
    result = subprocess.run(["dpkg", "-l", "snort"], capture_output=True, text=True)        
    if "snort" in result.stdout:
        print("|---------------------------- snort já está instalado ----------------------------|")
    else:
        try:
            # Atualizando pacotes do SO
            print("|--------------------- Atualizando pacotes ------------------------|")
            subprocess.run(["sudo", "apt", "update"])
            subprocess.run(["sudo", "apt", "install", "wget", "-y"])
            print("|-------------- Pacotes atualizados com sucesso ------------------|")

            # Instalando dependências
            print("|---------------------------- Instalando as dependências necessárias ---------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "build-essential", "libpcap-dev", "libpcre3-dev", "libdumbnet-dev", "bison", "flex", "zlib1g-dev", "libtool", "autotools-dev", "automake", "autoconf"])
            subprocess.run(["sudo", "apt-get", "install", "-y", "libluajit-5.1-dev", "libssl-dev", "libtirpc-dev", "rpcbind", "libnfs-dev"])
            print("|---------------------------- Dependências instaladas com sucesso ---------------------------|")

            # Download do DAQ (Data Acquisition library)
            print("|---------------------------- Download do DAQ ---------------------------|")
            subprocess.run(["sudo", "wget", "https://www.snort.org/downloads/snort/daq-2.0.7.tar.gz"])
            print("|---------------------------- Download concluído ---------------------------|")

            # Extração do arquivo DAQ
            daq_arquivo = input("Indique o nome do arquivo baixado -> 'daq-2.0.7.tar.gz' <-: ")
            print("|---------------------------- Extraindo o arquivo do DAQ ---------------------------|")
            subprocess.run(["sudo", "tar", "-xvzf", daq_arquivo])
            print("|---------------------------- Arquivo do DAQ extraído ---------------------------|")

            # Salvar o diretório atual (diretório antes de mudar)
            diretorio_anterior = os.getcwd()

            # Mudança para o diretório do DAQ
            daq_diretorio = input("Indique o nome do diretório do DAQ extraído: ")
            os.chdir(daq_diretorio)

            # Compilação e instalação do DAQ
            print("|---------------------------- Configurando o DAQ ---------------------------|")
            subprocess.run(["sudo", "./configure"])
            print("|---------------------------- Compilação configurada para o DAQ ---------------------------|")
            subprocess.run(["make"])
            subprocess.run(["sudo", "make", "install"])
            os.chdir(diretorio_anterior)
            print("|---------------------------- DAQ instalado com sucesso ---------------------------|")

            # Download do Snort
            print("|---------------------------- Download do Snort ---------------------------|")
            subprocess.run(["sudo", "wget", "https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz"])
            print("|---------------------------- Download concluído ---------------------------|")

            # Extração do arquivo Snort
            snort_arquivo = input("Indique o nome do arquivo baixado -> 'snort-2.9.20.tar.gz' <-: ")
            print("|---------------------------- Extraindo o arquivo do Snort ---------------------------|")
            subprocess.run(["sudo", "tar", "-xvzf", snort_arquivo])
            print("|---------------------------- Arquivo do Snort extraído ---------------------------|")

            # Mudança para o diretório do Snort
            snort_diretorio = input("Indique o nome do diretório do Snort extraído: ")
            os.chdir(snort_diretorio)

            # Compilação e instalação do Snort
            print("|---------------------------- Configurando o Snort ---------------------------|")
            subprocess.run(["sudo", "./configure", "--disable-open-appid", "CFLAGS=-I/usr/include/tirpc"])
            subprocess.run(["sudo", "make"])
            subprocess.run(["sudo", "make", "install"])
            print("|---------------------------- Snort instalado com sucesso ---------------------------|")

            # Criando diretórios e configurando o Snort
            print("|---------------------------- Criando arquivos de configuração ---------------------------|")
            subprocess.run(["sudo", "mkdir", "-p", "/etc/snort"])
            subprocess.run(["sudo", "mkdir", "-p", "/etc/snort/rules"])
            subprocess.run(["sudo", "mkdir", "-p", "/var/log/snort"])

            # Copiando arquivos de configuração
            print("|---------------------------- Copiando arquivos de configuração ---------------------------|")
            subprocess.run(["sudo", "cp", "etc/*.conf*", "/etc/snort/"])
            subprocess.run(["sudo", "cp", "etc/*.map", "/etc/snort/"])

            # Testando o Snort
            print("|---------------------------- Snort pronto para ser utilizado ---------------------------|")
            subprocess.run(["snort", "-v"])
            enter_clear ()
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
def snort_instalacao3():
    result = subprocess.run(["dpkg", "-l", "snort"], capture_output=True, text=True)        
    if "snort" in result.stdout:
        print("|---------------------------- snort já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Instalando o Snort ----------------------------|")
            subprocess.run(["sudo", "apt-get", "install", "-y", "snort"], check=True)
            print("|---------------------------- Snort pronto para ser utilizado ---------------------------|")
            print("|---------------------------- Ativando modo promisco ----------------------------|")
            subprocess.run(["ip", "a"])
            int_rede= input("Qaul e a sua interface de rede: ")
            subprocess.run(["sudo", "ip", "link", "set", int_rede, "promisc", "on"], check=True)
            print("|---------------------------- Modo promisco ativado ---------------------------|")
            # Criando diretórios e configurando o Snort
            print("|---------------------------- Criando arquivos de configuração ---------------------------|")
            subprocess.run(["sudo", "touch", "/etc/snort/rules/local.rules"])
            subprocess.run(["snort", "-V"])
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
def snort_instalacao ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        snort_menu_instalacao ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 3:
                        snort_instalacao3 ()
                        continue
                    case 4:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                    
#---> 2. Desinstalar
def snort_desintalar ():
    try:
        print ("|--------------------- Desinstalando o snort ------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "snort"], check=True)
        subprocess.run(["sudo", "apt", "remove", "--purge", "snort", "-y"], check=True)
        subprocess.run(["sudo", "apt-get", "remove", "--purge", "daq", "libpcap-dev", "libpcre3-dev", "libdumbnet-dev"], capture_output=True, text=True)
        subprocess.run(["sudo", "dpkg", "--remove", "snort"], capture_output=True, text=True)
        subprocess.run(["sudo", "dpkg", "--purge", "snort", "snort-common", "snort-doc"], capture_output=True, text=True)
        subprocess.run(["sudo", "dpkg", "--purge", "snort-rules-default"], capture_output=True, text=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], capture_output=True, text=True)
        subprocess.run(["sudo", "apt", "clean", "-y"], capture_output=True, text=True)
        print ("|--------------------- Deletando todos os arquivos ------------------------|")
        subprocess.run(["sudo", "rm", "-rf", "/etc/snort"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/log/snort"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/lib/snort"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/usr/local/etc/snort"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/usr/local/bin/snort"], check=True)
        print("|---------------------------- Snort desinstalado com sucesso ---------------------------|")
        print("|-------------- Nao esqueca-se de desativar o modo promisc caso nao for preciso ---------|")
        enter_clear ()
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
#---> 3. Comandos
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
def enable_snort ():
    # Ativação do serviço
    print("|-----------------------> Ativando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "enable", "snort"], check=True)
    print("|-----------------------> snort ativado com sucesso <------------------------------|")
    enter_clear ()
def start_snort ():
    # Iniciação do serviço
    print("|-----------------------> Iniciando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "start", "snort"], check=True)
    print("|-----------------------> snort iniciado com sucesso <-----------------------------|")
    enter_clear ()
def status_snort ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "snort"])
    enter_clear ()
def stop_snort ():
    # Ativação do serviço
    print("|-----------------------> Parando o servico Snort <------------------------------|")
    subprocess.run(["sudo", "systemctl", "stop", "snort"], check=True)
    print("|-----------------------> snort foi parado com sucesso <------------------------------|")
    enter_clear()
def restart_snort ():
    # Reativacao do serviço
    print("|-----------------------> Reiniciando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "restart", "snort"], check=True)
    print("|-----------------------> snort reiniciado com sucesso <----------------------------|")
    enter_clear ()
def version_snort (): 
    subprocess.run(["snort", "-V"])
    enter_clear() 
def comandos_snort ():
    while True:
        subprocess.run(["clear"])
        snort_menu_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    case 1:
                        enable_snort ()
                        continue
                    case 2:
                        start_snort ()
                        continue
                    case 3:
                        status_snort ()
                        continue
                    case 4:
                        stop_snort ()
                        continue
                    case 5:
                        restart_snort ()
                        continue
                    case 6:
                        version_snort ()
                        continue
                    case 7:
                        enter_clear ()
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#---> 4. Configuracoes
def snort_menu_conf ():
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     SNORT - Conf                                    |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   1.   | Configuracao de regras.                                                    |")   
    print("+--------+----------------------------------------------------------------------------+")
    print("|   2.   | Configuracao de alertas.                                                   |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   3.   | Configuracoes gerais.                                                      |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   4.   | Sair.                                                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def snort_menu_conf_alerts ():
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|                                                 SNORT - Alerts                                              |")
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("| Copie e cole os codigos no arquivo de configuracao e de seguida ative o alerta correspondente.              |")  
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|   1.   | Ativar a alerta de tentativa de coneccao FTP.                                                      |")
    print('| Codigo | alert tcp any any -> any 21 (msg:"tentativa exterior FTP!"; sid:1000001;)                          |')    
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print("|   2.   | Ativar a alerta de tentativa de coneccao TELNET.                                                   |")
    print('| Codigo | alert tcp $EXTERNAL_NET any -> $HOME_NET 23 (msg:"tentativa exterior TELNET !"; sid:1000002;)      |')
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print("|   3.   | Ativar a alerta de tentativa de coneccao Ping.                                                     |")
    print('| Codigo | alert icmp $EXTERNAL_NET any -> $HOME_NET any (msg:"Estamos a ser pingados !"; sid:1000004;)       |')
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print("|   4.   | Aceder ao arquivo de configuracao.                                                                 |")
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print("|   5.   | Sair.                                                                                              |")
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|                                                 - CMEasy -                                                  |")
    print("+-------------------------------------------------------------------------------------------------------------+")
def snort_menu_conf_geral ():
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|                                            CONFIGURACAO GERAL                                              |")
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("| Ao abrir o arquivo modifique deacordo a orientacao a baixo.                                                 |")  
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|   1.   | ipvar HOME_NET 192.168.1.0/24 ### sua rede interna ###                                             |")
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print('|   2.   | ipvar EXTERNAL_NET any                                                                             |')    
    print("+-------------------------------------------------------------------------------------------------------------+")
    print('|                                      Clique em [ ENTER ] para continuar                                     |') 
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|                                                 - CMEasy -                                                  |")
    print("+-------------------------------------------------------------------------------------------------------------+")
def snort_conf_alerts ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        snort_menu_conf_alerts ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 3:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 4:
                        subprocess.run(["sudo", "nano", "/etc/snort/rules/local.rules"])
                        continue
                    case 5:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue
def configuracao_snort():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        snort_menu_conf ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                subprocess.run(["clear"])
                match opcao:
                    case 1:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 2:
                        snort_conf_alerts ()
                        continue
                    case 3:
                        snort_menu_conf_geral ()
                        enter_clear ()
                        subprocess.run(["sudo", "nano", "/etc/snort/snort.conf"], check=True)
                        continue
                    case 4:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue
#---> 5. Alertas
def snort_alertas ():
    # Função para validar o formato CIDR
    def validar_endereco_rede(endereco_rede):
        padrao = r"^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$"
        return bool(re.match(padrao, endereco_rede))

    # Solicitar o endereço de rede ao usuário
    ind_rede = input("Indique o endereco de rede 'ex: 192.168.10.0/24': ")

    # Verificar se o endereço de rede é válido
    if not validar_endereco_rede(ind_rede):
        print("Endereço de rede inválido. Por favor, insira no formato correto 'xxx.xxx.xxx.xxx/xx'.")
    else:
        # Se o endereço de rede for válido, rodar o Snort
        print("|-----------------------> Alertas Snort <------------------------------|")
        try:
            subprocess.run(
                ["sudo", "snort", "-d", "-l", "/var/log/snort/", "-h", ind_rede, "-A", "console", "-c", "/etc/snort/snort.conf"],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o Snort: {e}")
# Programa Snort
def snort ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        snort_menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        snort_instalacao ()
                        continue
                    case 2:
                        snort_desintalar ()
                        continue
                    case 3:
                        comandos_snort ()
                        continue
                    case 4:
                        configuracao_snort ()
                        continue
                    case 5:
                        snort_alertas ()
                        continue
                    case 6:
                        enter_clear ()
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                
#-------------------------------------------------------------
#-------------------------------------------------------------
#---> Proxy Squid <---
# Menu Principal
def squid_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                 PROXY SQUID                                 |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | O proxy Squid é um intermediário que acede à internet por ti,    |")
    print("|          |podendo controlar, guardar e monitorizar os acessos.              |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Cache: guarda páginas já visitadas para carregar mais rápido.  |")
    print("|          | - Controlo de acesso: permite bloquear ou autorizar sites.       |")
    print("| Funções  | - Filtragem: impede conteúdos indesejados.                       |")
    print("|          | - Aumento de segurança: esconde o IP dos utilizadores.           |")
    print("|          | - Monitorização: regista e acompanha o que é acedido na rede.    |")
    print("+----------+------------------------------------------------------------------+")
    print("| Requisi- | SO: Linux (Debian, Ubuntu, CentOS...) ou Windows (em Cygwin).    |")
    print("|tos       | Acesso root / administrador para instalar e configurar o serviço.|") 
    print("|tos       | Porta de rede livre (padrão: TCP 3128, mas pode ser alterada).   |")
    print("|-----------------------------------------------------------------------------|")
    print("| Site ofi-| Link: https://www.squid-cache.org/                               |")
    print("|cial      |                                                                  |")
    print("|-----------------------------------------------------------------------------|")
    print("|  Testes  | Ubunto (v22).                                                    |")
    print("|-----------------------------------------------------------------------------+")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+------------------------+---------------------------+------------------------+")
    print("|    4. Configuracoes    |          5. Logs          |        6. Sair         |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
#---> 1. Instalar
def squid_instalacao():
    result = subprocess.run(["dpkg", "-l", "snort"], capture_output=True, text=True)        
    if "snort" in result.stdout:
        print("|---------------------------- snort já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
    
            print("|---------------------------- Instalando o Proxy Squid ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "squid", "-y"], check=True)
            print("|---------------------------- Proxy squid instaldo com sucesso ---------------------------|")

            subprocess.run("echo '# Liste os sites que pretende bloquear' >> /etc/squid/bad-sites.acl", shell=True)
            
            print("|-----------------------> Ativando o servico Squid <------------------------------|")
            subprocess.run(["sudo", "systemctl", "enable", "squid"], check=True)
            print("|-----------------------> squid ativado com sucesso <------------------------------|")
            
            print("|-----------------------> Iniciando o servico Squid <------------------------------|")
            subprocess.run(["sudo", "systemctl", "start", "squid"], check=True)
            print("|-----------------------> squid iniciado com sucesso <-----------------------------|")

            subprocess.run(["squid", "-v"])
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear ()                 
#---> 2. Desinstalar
def squid_desintalar ():
    try:
        print ("|--------------------- Desinstalando o squid ------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "squid"], check=True)
        subprocess.run(["sudo", "apt", "purge", "squid", "-y"], check=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], capture_output=True, text=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/spool/squid", "/var/log/squid", "/etc/squid"], capture_output=True, text=True)
        print("|---------------------------- Squid desinstalado com sucesso ---------------------------|")
        enter_clear ()
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
#---> 3. Comandos
def squid_menu_comandos ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                  SQUID                                      |")
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
def enable_squid ():
    # Ativação do serviço
    print("|-----------------------> Ativando o servico Squid <------------------------------|")
    subprocess.run(["sudo", "systemctl", "enable", "squid"], check=True)
    print("|-----------------------> squid ativado com sucesso <------------------------------|")
    enter_clear ()
def start_squid ():
    # Iniciação do serviço
    print("|-----------------------> Iniciando o servico Squid <------------------------------|")
    subprocess.run(["sudo", "systemctl", "start", "squid"], check=True)
    print("|-----------------------> squid iniciado com sucesso <-----------------------------|")
    enter_clear ()
def status_squid ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "squid.service"])
    enter_clear ()
def stop_squid ():
    # Ativação do serviço
    print("|-----------------------> Parando o servico Squid <------------------------------|")
    subprocess.run(["sudo", "systemctl", "stop", "squid"], check=True)
    print("|-----------------------> squid foi parado com sucesso <------------------------------|")
    enter_clear()
def restart_squid ():
    # Reativacao do serviço
    print("|-----------------------> Reiniciando o servico squid <------------------------------|")
    subprocess.run(["sudo", "systemctl", "restart", "squid"], check=True)
    print("|-----------------------> squid reiniciado com sucesso <----------------------------|")
    enter_clear ()
def version_squid (): 
    subprocess.run(["squid", "-v"])
    enter_clear() 
def comandos_squid ():
    while True:
        subprocess.run(["clear"])
        squid_menu_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    case 1:
                        enable_squid ()
                        continue
                    case 2:
                        start_squid ()
                        continue
                    case 3:
                        status_squid ()
                        continue
                    case 4:
                        stop_squid ()
                        continue
                    case 5:
                        restart_squid ()
                        continue
                    case 6:
                        version_squid ()
                        continue
                    case 7:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#---> 4. Configuracoes
def squid_menu_cof1 ():   
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     SQUID Conf                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   1.   | Arquivo de configuracao.                                                   |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   2.   | Boquei de Url's.                                                           |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   3.   | Sair.                                                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def squid_menu_cof2 ():
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     SQUID Conf                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("| Altere estas configuracoes deacordo ao seu ambiente, e cuidado com duplicidade de   |")
    print("|codigo.                                                                              |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   1.   | Definir a porta por defeito (Opcional, pos ja vem configurado).            |")
    print("| Codigo | port http_port 3128                                                        |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   2.   | Define a rede local permitida (toda a subnet 192.168.1.0/24).              |")
    print("| Codigo | acl localnet src 192.168.1.0/24                                            |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   a)   | Bloquer o acesso de um ip ao exterior.                                     |")
    print("+--------+----------------------------------------------------------------------------+")
    print("| Acl: acl ip_bloqueado src 192.168.1.100 | Info: Define o IP que queremos bloquear.  |")
    print("| Regra: http_access deny ip_bloqueado    | Info: Nega acesso ao IP bloqueado.        |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   b)   | Definir lista de sites para serem bloqueados.                              |")
    print("+--------+----------------------------------------------------------------------------+")
    print("| Acl: acl bad_url dstdomain “/etc/squid/bad-sites.acl”                               |")
    print("| Regra: http_access deny bad_url                                                     |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   3.   | permite o acesso ao proxy para todos os IPs que estão na ACL localnet.     |")
    print("| Codigo | http_access allow localnet                                                 |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   4.   | Nega tudo o resto (segurança — regra final).                               |")
    print("| Codigo | http_access deny all                                                       |")
    print("+-------------------------------------------------------------------------------------+")
    print("| No final reinicie o servico squid e configure o browser do host com o ip do         |")
    print("|servidor e e prta correspondente.                                                    |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                          Precione [ E N T E R ] para continuar                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def squid_menu_cof3 ():
    print("+-------------------------------------------------------------------------------------+")
    print("|                                SQUID - Conf - Sintaxe                               |")
    print("+-------------------------------------------------------------------------------------+")
    print("|1. Definir ACLs (Critérios usados para decidir quem ou o quê pode aceder ao proxy.). |")
    print("|2. Regras específicas.                                                               |")
    print("|3. Regra final (catch-all 'seguranca').                                              |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                          Precione [ E N T E R ] para continuar                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def squid_logs ():    
    while True:
        subprocess.run(["clear"])
        print("+-------------------------------------------------------------------------------------+")
        print("|                                     SQUID Logs                                      |")
        print("+-------------------------------------------------------------------------------------+")
        print("|   1.   | Monitorizar o trafego proxy.                                               |")
        print("+--------+----------------------------------------------------------------------------+")
        print("|   2.   | Monitorizar a cache.                                                       |")
        print("+--------+----------------------------------------------------------------------------+")
        print("|   3.   | Sair.                                                                      |")
        print("+-------------------------------------------------------------------------------------+")
        print("|                                       - CMEasy -                                    |")
        print("+-------------------------------------------------------------------------------------+")
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["clear"])
                        print ("|------------- Registro de acesso ao exterior ----------------|")
                        subprocess.run(["sudo", "tail", "-f", "/var/log/squid/access.log"])
                        continue
                    case 2:
                        subprocess.run(["clear"])
                        print ("|------------- Registro de acesso ----------------|")
                        subprocess.run(["sudo", "tail", "-f", "/var/log/squid/cache.log"])
                        continue
                    case 3:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue              
def squid_cof ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        squid_menu_cof1 ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["clear"])
                        squid_menu_cof3 ()
                        input ("Clique < ENTER > para continuar")
                        subprocess.run(["clear"])
                        squid_menu_cof2 ()
                        input ("Clique < ENTER > para continuar")
                        subprocess.run(["sudo", "nano", "/etc/squid/squid.conf"])
                        continue
                    case 2:
                        subprocess.run(["sudo", "nano", "/etc/squid/bad-sites.acl"])
                        continue
                    case 3:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                

# Programa Squid
def proxy_squid ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        squid_menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        squid_instalacao ()
                        continue
                    case 2:
                        squid_desintalar ()
                        continue
                    case 3:
                        comandos_squid ()
                        continue
                    case 4:
                        squid_cof ()
                        continue
                    case 5:
                        squid_logs ()
                        continue
                    case 6:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                


def ciberseguranca ():
    while True:
        subprocess.run(["clear"])
        menu_so_ciberseguranca ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    # Programa Fail2Ban  
                    case 1:
                        fail2ban ()
                        continue
                    # Programa Snort
                    case 2:
                        snort ()
                        continue
                    # Programa Proxy Squid
                    case 3:
                        proxy_squid ()
                        continue
                    # Voltar ao menu anterior
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue





#------------------------> Programacao

#------------------------> Outros programas
# Menu Principal
def menu_outros_programas ():
    print("+--------------------------------------------------------------+")
    print("|                      OUTROS PROGRAMAS                        |")
    print("+--------------------------------------------------------------+")
    print("|  1.  | SSH (Secure Shell)                                    |")
    print("+------+-------------------------------------------------------+")
    #print("| 2. | Iniciar                                                 |")
    #print("+----+---------------------------------------------------------+")
    #print("| 3. | Estado                                                  |")
    #print("+----+---------------------------------------------------------+")
    #print("| 4. | Parar                                                   |")
    #print("+----+---------------------------------------------------------+")
    #print("| 5. | Reiniciar                                               |")
    #print("+----+---------------------------------------------------------+")
    #print("| 6. | Versão                                                  |")
    #print("+----+---------------------------------------------------------+")
    #print("| 7. | Ver IP'S Banidos                                        |")
    #print("+----+---------------------------------------------------------+")
    #print("| 8. | Liberar IP                                              |")
    #print("+----+---------------------------------------------------------+")
    #print("| 8. | Banir Host                                              |")
    #print("+----+---------------------------------------------------------+")
    print("|  2.  | Sair                                                  |")
    print("+--------------------------------------------------------------+")
    print("|                        - CMEasy -                            |")
    print("+--------------------------------------------------------------+")
#---> ssh
def menu_ssh ():
    print("+----------------------------------------------------+")
    print("|                      S S H                         |")
    print("+----------------------------------------------------+")
    print("| SSH (Secure Shell) é um protocolo de rede utilizado|")
    print("|para acessar de forma segura e remota computadores  |")
    print("|ou servidores, permitindo a execução de comandos e a|")
    print("|transferência de arquivos criptografados.           |")
    print("+----------------------------------------------------+")
    print("|      1. Instalar         |     2. Desinstalar      |")
    print("+--------------------------+-------------------------+") 
    print("|      3. Comandos         |        4. Sair          |")
    print("+----------------------------------------------------+")
    print("|                   - CMEasy -                       |")
    print("+----------------------------------------------------+")
# Instalar ssh
def instalacao_ssh ():
    try:
        print("|---------------------------- Instalando o ssh  ------------------------------|")
        subprocess.run(["sudo", "apt","install", "-y", "openssh-server"], check=True)
        print("|---------------------- SSH instalado com sucesso --------------------------------|")
        
        print("|-------------------------- ativando o ssh ------------------------------|")
        subprocess.run(["systemctl", "enable", "ssh"], check=True)
        print("|---------------------- SSH ativado com sucesso --------------------------------|")
        
        print("|---------------------------- Iniviando o ssh --------------------------------|")
        subprocess.run(["sudo", "apt", "install", "-y", "fail2ban"], check=True)
        print("|----------------------- ssh iniciado com sucesso ----------------------------|")
        print("|---------------------------- ssh instalado com sucesso ------------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear()
# Desinstalar ssh
def desinstalacao_ssh ():
    try:
        print("|---------------------------- Desinstalando o ssh  ------------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "ssh"], check=True) 
        subprocess.run(["sudo", "apt", "remove", "--purge", "-y", "openssh-server"], check=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/etc/ssh"], check=True) 
        subprocess.run(["sudo", "rm", "-rf", "/home/*/.ssh"], check=True)
        print("|----------------------- ssh desinstalado com sucesso ----------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear()
# Comandos
def menu_ssh_comandos ():
    print("+----------------------------------------------------+")
    print("|                    COMANDOS SSH                    |")
    print("+----------------------------------------------------+")
    print("| 1. Ativar                                          |")
    print("| 2. Iniciar                                         |")
    print("| 3. Estado                                          |")
    print("| 4. Parar                                           |")
    print("| 5. Reiniciar                                       |")
    print("| 6. Versao                                          |")
    print("| 7. Sair                                            |")
    print("+----------------------------------------------------+") 
def comandos_ssh ():
    while True:
        subprocess.run(["clear"])
        menu_ssh_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["sudo", "systemctl", "enable", "ssh"], check=True) 
                        print ("|---------------- ssh Ativado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 2:
                        subprocess.run(["sudo", "systemctl", "start", "ssh"], check=True) 
                        print ("|---------------- ssh iniciado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 3:
                        subprocess.run(["sudo", "systemctl", "status", "ssh"]) 
                        enter_clear ()
                        continue
                    case 4:
                        subprocess.run(["sudo", "systemctl", "stop", "ssh"], check=True) 
                        print ("|---------------- ssh parado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 5:
                        subprocess.run(["sudo", "systemctl", "restart", "ssh"], check=True) 
                        print ("|---------------- ssh reiniciado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 6:
                        subprocess.run(["ssh", "-V"], check=True) 
                        enter_clear ()
                        continue
                    case 7:
                        enter_clear ()
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
                continue 
###########################################################################

###########################################################################
#----------------> 2. Executar Comandos <-----------------

###########################################################################

###########################################################################
#----------------> 3. Informacao <-----------------
# Menu Informacao
def menu_inform ():
    print("+--------------------------------------------------------+")
    print("|           --> INFORMACAO DO PROGRAMA <--               |")
    print("+--------------------------------------------------------+")
    print("| Nome: CMEasy                                           |")
    print("+--------------------------------------------------------+")
    print("| Criador: Cleison Maquina                               |")
    print("+--------------------------------------------------------+")
    print("| Sistema Operacional: Linux                             |")
    print("+--------------------------------------------------------+")
    print("| Ano de Criacao: 2026                                   |")
    print("+--------------------------------------------------------+")
    print("| Linguagem de Programacao: Python                       |")
    print("+--------------------------------------------------------+")
    print("| Versao: 0.1v                                           |")
    print("+--------------------------------------------------------+")
    print("| Descricao: Automatizacao de processos refente a        |")
    print("|instalacao de programas e execusao de comandos.         |")
    print("+--------------------------------------------------------+")
    print("|            Clique [ ENTER ] para voltar                |")
    print("+--------------------------------------------------------+")
    print("|                     @cmeasy                            |")
    print("+--------------------------------------------------------+") 
###########################################################################

###########################################################################
# Programa CMEasy.
def main ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            # Tentar converter a entrada para um número inteiro
            try:
                opcao = int(escolha)
                match opcao:
                    #-------- 1. Instalar Promagramas
                    case 1:
                        while True: 
                            subprocess.run(["clear"])
                            menu_instalar_programas ()
                            escolha = input ("Escolha uma das opções acima: ")
                            if escolha == "":
                                entrada_invalida1 ()
                                continue
                            else:
                                try:
                                    opcao = int (escolha)
                                    match opcao:
                                        #-------- Tipos de programas 
                                        case 1:
                                            while True: 
                                                subprocess.run(["clear"])
                                                menu_tipo_de_programa ()
                                                escolha = input ("Escolha uma das opções acima: ")
                                                if escolha == "":
                                                    entrada_invalida1 ()
                                                    continue
                                                else:
                                                    try:
                                                        opcao = int (escolha)
                                                        match opcao:
                                                            #-------- Ciberseguranca  
                                                            case 1:
                                                                ciberseguranca ()
                                                                continue
                                                            #-------- Programacao
                                                            case 2:
                                                                print ("Indisponivel no momento...")
                                                                enter_clear ()
                                                                continue
                                                            #-------- Outros Programas
                                                            case 3:
                                                                while True: 
                                                                    subprocess.run(["clear"])
                                                                    menu_outros_programas ()
                                                                    escolha = input ("Escolha uma das opções acima: ")
                                                                    if escolha == "":
                                                                        entrada_invalida1 ()
                                                                        continue
                                                                    else:
                                                                        try:
                                                                            opcao = int (escolha)
                                                                            match opcao: 
                                                                                #-------- Programa SSH
                                                                                case 1:
                                                                                    while True: 
                                                                                        subprocess.run(["clear"])
                                                                                        menu_ssh ()
                                                                                        escolha = input ("Escolha uma das opções acima: ")
                                                                                        if escolha == "":
                                                                                            entrada_invalida1 ()
                                                                                            continue
                                                                                        else:
                                                                                            try:
                                                                                                opcao = int (escolha)
                                                                                                match opcao: 
                                                                                                    # Instalar
                                                                                                    case 1:
                                                                                                        instalacao_ssh ()
                                                                                                        continue
                                                                                                    # Desinstalar
                                                                                                    case 2:
                                                                                                        desinstalacao_ssh ()
                                                                                                        continue
                                                                                                    # Comandos
                                                                                                    case 3:
                                                                                                        comandos_ssh()
                                                                                                        continue
                                                                                                    # Voltar
                                                                                                    case 4:
                                                                                                        break
                                                                                                    case _:
                                                                                                        entrada_invalida3 ()
                                                                                                        continue 
                                                                                            except ValueError:
                                                                                                entrada_invalida2 ()
                                                                                                continue 
                                                                                case 2:
                                                                                    break
                                                                                case _:
                                                                                    entrada_invalida3 ()
                                                                                    continue 
                                                                        except ValueError:
                                                                            entrada_invalida2 ()
                                                                            continue                                                               
                                                            # Voltar ao menu anterior
                                                            case 4:
                                                                break
                                                            case _:
                                                                entrada_invalida3 ()
                                                                continue
                                                    except ValueError:
                                                        entrada_invalida2 ()
                                                        continue                                        
                                        # Voltar ao menu anterior
                                        case 2:
                                            break
                                        case _:
                                            entrada_invalida3 ()
                                            continue  
                                except ValueError:
                                    entrada_invalida2 ()
                                    continue
                    # Executar comandos
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    # Informacao do sistema operacional
                    case 3:
                        subprocess.run(["clear"])
                        menu_inform ()
                        enter_clear ()
                        continue
                    #-------- 4. Encerrar o programa
                    case 4:
                        print("Programa 'CMEasy' encerrado, Obrigado!")
                        break 
                    case _:
                            # Este case captura qualquer entrada que não seja uma opção válida
                            entrada_invalida3 ()
                            continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue

main ()