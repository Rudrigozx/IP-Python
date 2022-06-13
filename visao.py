

def menu_visao():
    
    print("\n         Menu")
    print("\n")
    print( " - 1 -  Cadastrar")
    print( " - 2 -  Exibir todos os voo(Atenção:lista muito grande,recomendado apenas para testes)")
    print( " - 3 -  Buscar voo(Destino)")
    print( " - 4 -  Buscar voo(Escala)")
    print( " - 5 -  vender Bilhete")
    print( " - 0 -  Sair e Salvar")
    print("\n")
    opcao=int(input("escolha uma das opções: "))
    
    return opcao

def dados_cadastro():
    
    cidades=list()
    numero_voo=input("digite o numero do voo: ")
    dia, mes, ano=input("digite a data do voo(d/m/aaaa): ").split('/')
    periodicidade=input("digite a periodicidade (diario, semanal): ")
    cidades=input("digite a lista de cidades(começando na origem e terminando no destino) todos separados por vírgula: ").split(',')
    assentos=int(input("digite o numero de assentos disponiveis no voo: "))
    
    return numero_voo, dia, mes, ano, periodicidade, cidades, assentos

def imprime_voo(dados,tamanho):
    
    for i in range(tamanho):
        data=str(dados[i]['data'])
        print("\nNumero do voo: {}".format(dados[i]['numero']))
        print("Data: {}".format(data[:-8]))
        print("Periodicidade: {}".format(dados[i]['periodicidade']))
        print("Lista de cidades: saindo de: '{}' passando por: {} e com destino em: '{}'".format(dados[i]['cidades'][0], dados[i]['cidades'][1:-1], dados[i]['cidades'][-1]))
        print("Assentos disponiniveis: {} \n".format(dados[i]['assentos']))
        
def alerta(alertas):
    
    print("\n\n{}\n\n".format(alertas))
    
    voltar=input("aperte -Enter- para voltar!")
    

def dados_busca_destino():
    
    destino=input("digite o destino do voo: ")
    dia,mes,ano=input("digite a data do voo(d/m/aaaa): ").split('/')
    return dia,mes,ano,destino

def dados_busca_escala():
    escala=input("digite o uma escala do voo: ")
    dia,mes,ano=input("digite a data do voo(d/m/aaaa): ").split('/')
    return dia,mes,ano,escala

def dados_venda():
    origem_pessoal=input("digite a cidade de saida do voo: ")
    destino_pessoal=input("digite a sua cidade de destino: ")
    dia,mes,ano=input("digite a data do voo(d/m/aaaa): ").split('/')
    return dia,mes,ano,destino_pessoal,origem_pessoal

def vender():
    num=input('digite o numero do voo da venda: ')
    vendas=int(input('deseja vender quantos bilhetes para esse voo?'))
    return num,vendas
