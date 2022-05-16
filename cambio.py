import requests
import json
from datetime import datetime


class Cambio():
    def __init__(self):
        self.url = "https://economia.awesomeapi.com.br/json"

    def cotacaoMoedas(self):
        r = requests.get(f"{self.url}/all")
        json_data = json.loads(r.text)
        resultado = {}
        for moeda in json_data:
            resultado[moeda] =self.__converteValores(json_data[moeda],1)
        # retirar valores desatualizados
        [resultado.pop(key) for key in ['BTC', 'LTC','XRP','ETH','DOGE']]
        return resultado

    def cotacaoMoeda2Moeda(self,moeda1,moeda2):
        r = requests.get(f"{self.url}/last/{moeda1}-{moeda2}")
        json_data = json.loads(r.text)
        return json_data

    def trataCotacao(self,moeda1,moeda2,quantidade):
        try:
            retorno = self.cotacaoMoeda2Moeda(moeda1,moeda2)
            if moeda1 == moeda2:
                return {'message':"Insira tipo de moedas diferentes"}
            #moeda1+moeda2 é a concatenação das strings
            cotacaoVenda = self.__converteValores(retorno[moeda1+moeda2],quantidade)
            return cotacaoVenda
        except KeyError:
            return {'message':"Não foram localizadas informações dessa cotação"}

    def __converteParaDinheiro(self,valor):
        return  str(valor).replace('.',',')


    def __converteValores(self,retornoCotacao,quantidade):
        retorno = retornoCotacao
        if 'message' not in retorno:
            nome = retorno['name'].split('/')[0]
            valorCompra = self.__converteParaDinheiro(float(retorno['bid']) * quantidade)
            valorVenda = self.__converteParaDinheiro(float(retorno['ask']) * quantidade)
            maximoDia = self.__converteParaDinheiro(float(retorno['high']))
            minimoDia = self.__converteParaDinheiro(float(retorno['low']))
            porcentagemVariacao = self.__converteParaDinheiro(float(retorno['pctChange']))+'%'
            variacao = self.__converteParaDinheiro(float(retorno['varBid']))
            dataCotacao = f"{datetime.strptime(retorno['create_date'], '%Y-%m-%d %H:%M:%S').date():'%d/%m/%Y'}".replace("'","")
            return { 'nome':nome,
                      'valorCompra': valorCompra,
                      'valorVenda':valorVenda,
                      'dataCotacao':dataCotacao,
                      'maximoDia':maximoDia,
                      'minimoDia': minimoDia,
                      'variacao':variacao,
                      'porcentagemVariacao': porcentagemVariacao}
        else:
            return retorno

    def moedasDisponiveis(self):
        r = requests.get(f"{self.url}/available/uniq")
        json_data = json.loads(r.text)
        return json_data

