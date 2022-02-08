from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
from stdiomask import getpass
from time import sleep

# Comando do Colorama que volta a cor sempre que troca-la
init(autoreset=True)


# Criar o Menu de Opções

def exibir_menu():
    print(Fore.GREEN + '''Bem vindos ao projeto -- Sistema de login --\nEscolha uma Opção:\n
    [1] Cadastrar novo Usuário
    [2] Fazer Login
    [3] Sair    
    ''')
    try:
        opcao = int(input(('Digite sua opção: ')))
        return(opcao)
    except:
        print(Fore.RED+'Digite um valor valido!')

def fazer_login():
    login = input('Nome: ')
    senha = getpass(prompt='Senha: ', mask='*')
    return(login, senha)

def buscar_usuario(login,senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())
        #login, senha = fazer_login()
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if login == nome and senha == password:
                    return True
    except FileNotFoundError:
        return False


while True:
    system('cls')
    opcao = exibir_menu()

    if opcao == 1:
        # Cadastrar novo usuário
        login, senha = fazer_login()
        if login == senha:
            print('Sua senha deve ser diferente do login')
            senha = getpass('Senha: ')
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.RED+'Usuário já existe!')
            sleep(2)
            #exit()
        else:
            with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.writelines(f'{login} {senha}\n')
                print(Fore.CYAN + 'Cadastro aprovado!')
                sleep(2)
                exibir_menu()

    elif opcao == 2:
        #Fazer o login do usuário
        login, senha = fazer_login()
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.CYAN + 'Login realizado com sucesso!')
            sleep(1)
            exit()
        else:
            print(
                Fore.RED+'Você deve ter digitado seu nome de usuário ou a senha.\n Verifique os dados digitados novamente')
            sleep(2)
    elif opcao == 3:
        print(Fore.BLUE+'Bye bye!')
        exit()

    else:
        print(Fore.RED+'Digite apenas uma das opções disponiveis!')
        sleep(1)
        exibir_menu()




