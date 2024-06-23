class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def media_avaliacoes(self):
        if not self.avaliacoes:
            return "Sem avaliações"
        soma_avaliacoes = sum(avaliacao.nota for avaliacao in self.avaliacoes)
        media = soma_avaliacoes / len(self.avaliacoes)
        return round(media, 2)
