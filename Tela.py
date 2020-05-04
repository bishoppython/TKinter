import PySimpleGUI as sg

class TelaPython:
    def __init__(self): #Definir os dados iniciais
        sg.change_look_and_feel('DarkBlue14')
        #Layout - Criação do Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0), key='nome')], # Definição de estilos
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de e-mail você utiliza?')],
            [sg.Checkbox('Gmail', key='gmail'),sg.Checkbox('Outlook', key='outlook'),sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita Cartões?')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartoes'), sg.Radio('Nao', 'cartoes',key='naoAceitaCartoes')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
           #[sg.Text('Deseja ver o Log?')],   #Trabalhando nisso ainda
           #[sg.Radio('Sim', 'log', key='quersim'), sg.Radio('Nao', 'log',key='quernao')],
            [sg.Output(size=(30,20))]
        ]
        #Janela - Criação da janela
                 # Dentro do "sg.Window" passamos o nome da tela/janela e após isso implementamos
                 # com o atributo Layout que irá trazer as informações em Tela
        self.janela = sg.Window("Dados dos Usuarios").layout(layout)


    def Iniciar(self): #Metodo para inicar esses dados
        #print(self.values) # E imprimir na tela pra ver o resultado
        while True:

            #Extrair os dados da tela
            #Aqui fazemos um hantek, transferindo informações para mais de uma variavel
            self.Button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            usa_gmail = self.values['gmail']
            usa_outlook = self.values['outlook']
            usa_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartoes']
            naoaceita_cartao = self.values['naoAceitaCartoes']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'Usa Gmail: {usa_gmail}')
            print(f'Usa Outlook: {usa_outlook}')
            print(f'Usa Yahoo: {usa_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Nao Aceita Cartão: {naoaceita_cartao}')
            print(f'Velocidade Script:{velocidade_script}')

tela = TelaPython() #Instanciamos a Classe
tela.Iniciar() # E iniciamos o metodo