from avaliacao import AVALIACAO
from avaliacao import Avaliacoes


class RESTAURANTE:

    Restaurantes = []
    def __init__(self,nome,categoria):
        self._nome = nome
        self.categoria = categoria 
        RESTAURANTE.Restaurantes.append(self)
        self._ativo = False
        
    


    def ativo(self):
        return "ATIVADO" if self._ativo == True else "DESATIVADO"


    @classmethod
    def LSITAR(cls):
        print(f'{"{Nome}".ljust(15)} | {"{Categoria}".ljust(15)} | {"{Ativado}"}')

        for i in cls.Restaurantes:
            return(f'{i._nome.ljust(15)} | {i.categoria.ljust(15)} | {i.ativo()}')
        


    def ATIVAR(self):
        
        if self._ativo == False:
            self._ativo = True 
        
        else:
            self._ativo = False 
        
        
    def receber_avaliacoes(self, avaliacao: AVALIACAO):
        Avaliacoes.append(avaliacao)


    @classmethod
    def medianotas(cls):
        notas = [avaliacao.nota for avaliacao in Avaliacoes]
        if notas:
            media = round(sum(notas) / len(notas), 2)
            return f" | {media:.2f}/5.0"
        else:
            return " | Sem avaliações"
        



rest1 = RESTAURANTE('allan', 'coiso')



print(RESTAURANTE.medianotas())