class Tarefa: 
    '''Classe que representa uma tarefa com ID da tarefa, descrição, data de criação, status, prazo final e urgência'''

    def __init__(self, id, descricao, data_de_criacao, status, prazo_final, urgencia):
        self.id = id
        self.descricao = descricao
        self.data_de_criacao = data_de_criacao
        self.status = status
        self.prazo_final = prazo_final
        self.urgencia = urgencia

    def __str__(self):
        return f"{self.id},{self.descricao},{self.data_de_criacao},{self.status},{self.prazo_final},{self.urgencia}"