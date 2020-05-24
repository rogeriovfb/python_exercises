"""
Crie uma classe denominada Elevador para armazenar as informações de um elevaor dentro de um prédio. A classe
deve armazenar o andar atual (térreo = 0), total de andares no prédio (excluindo terreo), capacidade do elevador
e quantas pessoas estão presentes nele.
A classe deve disponibilizar os seguintes metodos:
- Inicializa
- Entra
- Sai
- Sobe
- Desce
"""


class Elevador:

    def __init__(self, andares, capacidade):
        self.__andares = andares
        self.__andar_atual = 0
        self.__capacidade = capacidade
        self.__pessoas = 0

    @property
    def andares(self):
        return self.__andares

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def pessoas(self):
        return self.__pessoas

    @property
    def andar_atual(self):
        return self.__andar_atual

    def entra(self):
        if self.__capacidade > self.__pessoas:
            self.__pessoas += 1
        else:
            print('Elevador está lotado')

    def sai(self):
        if self.__pessoas > 0:
            self.__pessoas += 1
        else:
            print('Elevador está vazio')

    def sobe(self):
        if self.__andar_atual < self.__andares:
            self.__andar_atual += 1
        else:
            print('Elevador está no último andar')

    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            print('Elevador está no térreo')


elev1 = Elevador(10, 5)
elev1.desce()
elev1.sai()
elev1.entra()
elev1.entra()
print(elev1.pessoas)
elev1.sobe()
print(elev1.andar_atual)
elev1.desce()
print(elev1.andar_atual)
