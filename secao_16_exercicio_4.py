"""
Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume e trocar os canais da Televisao.
O controle de colume permite aumentar ou diminuir uma unidade de cada vez
O controle de canal permite aumentar e diminuir uma unidade ou trocar para canal indicado
Criar metodos para consultar valor do volume e canal selecionado
"""


class Televisao:

    def __init__(self):
        self.__canal = 0
        self.__volume = 1

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, valor):
        self.__canal = valor

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, valor):
        self.__volume = valor


class ControleRemoto:

    def __init__(self, televisao):
        self.__televisao = televisao

    def aumentar_volume(self):
        self.__televisao.volume += 1

    def diminuir_volume(self):
        self.__televisao.volume -= 1

    def aumentar_canal(self, valor=-1):
        if valor == -1:
            self.__televisao.canal += 1
        else:
            self.__televisao.canal = valor

    def diminuir_canal(self, valor=-1):
        if valor == -1:
            self.__televisao.canal -= 1
        else:
            self.__televisao.canal = valor


tv1 = Televisao()
controle = ControleRemoto(tv1)
