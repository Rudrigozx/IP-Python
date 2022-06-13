registro_voo= []
lista_de_cidades= list()
busca_lista=list()
busca_lista_escala=list()
busca_lista_venda=list()
import datetime

 
def cadastrar_voo(numero_voo, data_voo, periodicidade, lista_de_cidades, assentos_disponiveis):
    global registro_voo
    
    registro_voo.append({'numero': numero_voo,
                         'data':data_voo,
                         'periodicidade':periodicidade,
                         'cidades':lista_de_cidades,
                         'assentos':assentos_disponiveis})



def verificar_vazio(lista):
    
    for verificador in lista:
        return verificador


def buscar_voo_destino(data_voo,destino):
    busca_lista=list()
    global registro_voo
    for voo in registro_voo:
        if destino == voo['cidades'][-1] and data_voo == voo['data']:
            busca_lista.append(voo)
    return busca_lista


def buscar_voo_escala(data_voo_escala, escala):
    busca_lista_escala= list()
    global registro_voo
    for voo in registro_voo:
        for i in range(len(voo['cidades'])-2):
            if escala == voo['cidades'][i+1] and data_voo_escala == voo['data']:
                busca_lista_escala.append(voo)
    return busca_lista_escala

def buscar_voo_venda(data_voo_venda, destino_pessoal, origem_pessoal):
    global busca_lista_venda
    busca_lista_venda=list()
    global registro_voo
    
    for voo in registro_voo:
        for cidade in voo['cidades'][1:]: 
            if destino_pessoal== cidade :
                if data_voo_venda == voo['data'] and origem_pessoal==voo['cidades'][0]:
                    busca_lista_venda.append(voo)
    return busca_lista_venda

def vendendo(numero_voo,quantidade):
    global busca_lista_venda
    global registro_voo
    for voo in busca_lista_venda:
        if int(voo['assentos'])< int(quantidade):
            return False
        else:
            if numero_voo == voo['numero']:
              for voos in  registro_voo:
              
                  if voo==voos:
                      voos['assentos']= int(voos['assentos']) - int(quantidade)
                      return True
    

