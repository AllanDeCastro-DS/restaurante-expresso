from avaliacao import AVALIACAO

class RESTAURANTE:

    Restaurantes = []
    Avaliacoes = []
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
            return(f'{i.nome.ljust(15)} | {i.categoria.ljust(15)} | {i.ativo()}')
        


    def ATIVAR(self):
        
        if self._ativo == False:
            self._ativo = True 
        
        else:
            self._ativo = False 
        
        
    def receberavaliacoes(self):
        avaliacaod = AVALIACAO()
        RESTAURANTE.Avaliacoes.append(avaliacaod)

    @classmethod
    def medianotas(cls):
        notas = [avaliacao.nota for avaliacao in cls.Avaliacoes]
        media = round(sum(notas) / len(notas)) if len(notas) != 0 else 0

        return f" | {media}"  
        



rest1 = RESTAURANTE('allan', 'coiso')






print(RESTAURANTE.medianotas())