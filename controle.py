from modelo import *
from visao import *
import datetime
import os
import re
def menu():
    return menu_visao()


def cadastro():
    global registro_voo
    cidades=list()
    numero_voo, dia, mes, ano, periodicidade, cidades, assentos = dados_cadastro()
    data= datetime.datetime(int(ano),int(mes),int(dia))
    for voo in registro_voo:
        if numero_voo == voo['numero']:
            alertas='Numero de voo em uso!!!'
            return alerta(alertas)
    if periodicidade=='diario':
        for i in range(365):
           date=data + datetime.timedelta(days=i) 
           cadastrar_voo(numero_voo, date, periodicidade, cidades, assentos)
           
    elif periodicidade=='semanal':
      for i in range(52):
           date=data + datetime.timedelta(weeks=i) 
           cadastrar_voo(numero_voo, date, periodicidade, cidades, assentos)  

    
def exibir():
    global registro_voo
    tamanho=len(registro_voo)
    if  verificar_vazio(registro_voo)== None:
        alertas='Nenhum voo cadastrado!!!'
        return alerta(alertas)
    else:
        return imprime_voo(registro_voo,tamanho)
    

def buscar_destino():
    busca_lista=[]
    global registro_voo
    dia,mes,ano,destino = dados_busca_destino()
    data_voo= datetime.datetime(int(ano),int(mes),int(dia))
    busca_lista=buscar_voo_destino(data_voo,destino)
    tamanho=len(busca_lista)
    if  verificar_vazio(busca_lista)== None:
        alertas='Nenhum voo encontrado!!!'
        return alerta(alertas),menu_visao()
    else:
        return imprime_voo(busca_lista,tamanho)

        
def buscar_escala():
    busca_lista_escala=[]
    global registro_voo
    dia,mes,ano,escala = dados_busca_escala()
    data_voo_escala = datetime.datetime(int(ano),int(mes),int(dia))
    busca_lista_escala = buscar_voo_escala(data_voo_escala,escala)
    tamanho = len(busca_lista_escala)
    if  verificar_vazio(busca_lista_escala)== None:
        alertas='Nenhum voo encontrado!!!'
        return alerta(alertas)
    else:
        return imprime_voo(busca_lista_escala,tamanho)

def buscar_venda():
    global busca_lista_venda
    busca_lista_venda=[]
    global registro_voo
    dia,mes,ano,destino_pessoal, origem_pessoal = dados_venda()
    data_voo_venda = datetime.datetime(int(ano),int(mes),int(dia))
    busca_lista_venda = buscar_voo_venda(data_voo_venda,destino_pessoal,origem_pessoal)
    tamanho = len(busca_lista_venda)
    if  verificar_vazio(busca_lista_venda)== None:
        alertas='Nenhum voo encontrado!!!'
        return alerta(alertas)
    else:
        return imprime_voo(busca_lista_venda,tamanho)

def venda():
    global busca_lista_venda
    buscar_venda()
    if verificar_vazio(busca_lista_venda)== None:
        alertas='Erro na venda!!!'
        return alerta(alertas)
    else:
        numero_voo,quantidade = vender()
    
        if vendendo(numero_voo,quantidade)==False or quantidade < 0:
            alertas='Erro na venda!!!'
            return alerta(alertas)
        
        else:
            alertas='Vendido com sucesso!!!'
            return alerta(alertas)
def carregar():
    if os.path.isfile('dados.csv'):
        global registro_voo
        cidades=list()
        bd = open('dados.csv','r')
        for line in bd:
          numero, data, periodicidade, cidade, assentos = line.split(";")
          cidades=cidade[1:].split(",")
          date= datetime.datetime(int(data[:4]),int(data[5:7]),int(data[8:10]))
          cadastrar_voo(numero, date, periodicidade, cidades, int(assentos))
        bd.close()

    

def salvar():
    global registro_voo
    cidade=''
    bd = open('dados.csv','w')    
    for voo in registro_voo:
        cidade=''
        for cidades in voo['cidades']:
            cidade=cidade + ',' + cidades
        
        bd.write("{};{};{};{};{}\n".format(voo['numero'], voo['data'], voo['periodicidade'], cidade, voo['assentos']))                          
    bd.close()

