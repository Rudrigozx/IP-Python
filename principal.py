from controle import *
import os

carregar()
opcao=menu()

while opcao!=0:
     
    if opcao==1:
        os.system('cls') or None
        cadastro()

    elif opcao==2:
        os.system('cls') or None
        exibir()
        
        
    elif opcao==3:
        os.system('cls') or None
        buscar_destino()
        
    elif opcao==4:
        os.system('cls') or None
        buscar_escala()
        
    elif opcao==5:
        os.system('cls') or None
        venda()
    opcao=menu()
salvar()
