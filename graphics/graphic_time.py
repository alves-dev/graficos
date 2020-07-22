from graphics.interface_graphic import InterfaceGraphics


class GraphicTime(InterfaceGraphics):
    """
        Realiza as chamadas dos metodos na ordem...

        :param directory: Lista dos csv para criar o data frame
            :key index: uma lista de index para serem filtrado = ['04:30:00', ..., '07:30:00']
            :key index_interval: uma lista de dois index para serem filtrado entre eles = ['08:00:00', '17:30:00']
            :key columns: uma lista de datas para serem filtradas = ['10/05/2020',..., '15/05/2020']
            :key columns_days: uma lista de dias da semana para serem filtrado = ['Segunda','terca','']
            :key columns_interval: uma lista contendo datas para serem filtradas entre elas= ['22/12/2019','21/02/2020']
            :key activities: uma lista contendo atividades para serem filtradas = ['Dev', 'Trabalho', 'Descanso', 'TCC']
        :return: ALTERAR O RETORNO PARA UM json
        """

    def __init__(self, directory, type_graphic: list = ['all'], title: str = 'Atividades', label_axisx: str = '',
                 label_axisy: str = 'Quantidade / 2 = X horas ', index: list = [], index_interval: list = [],
                 columns: list = [], columns_days: list = [], columns_interval: list = [], activities: list = [],
                 label_rotation_x='60'):
        InterfaceGraphics.__init__(self, type_graphic, title, label_axisx, label_axisy, directory)
        self.index = index
        self.index_interval = index_interval
        self.columns = columns
        self.columns_days = columns_days
        self.columns_interval = columns_interval
        self.activities = activities
        self.label_rotation_x = label_rotation_x
