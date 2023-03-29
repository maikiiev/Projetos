import PySimpleGUI as sg 

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')
        layout = [
            [sg.Text('Nome',border_width=(10.0)),sg.Input(border_width=(8.0),key='Nome')],
            [sg.Text('Idade',border_width=(10.0)),sg.Input(border_width=(8.0),key='Idade')],
            [sg.Text('Quais canais de e-mails são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'),sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Text('aceita cartao')],
            [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,100),default_value=0,orientation='h',size=(10,20),key='sliderVelocidade')],
            [sg.Button('Enviar Dados',border_width=(7.0))],
            [sg.Output(size=(20,20))]
        ]
        
        self.janela = sg.Window('Dados dos Usuários'). layout(layout)

        self.button, self.values = self.janela.read() 
    
    def iniciar(self):
        while True:
            self.button, self.values = self.janela.read()        
            nome = self.values['Nome']
            idade = self.values['Idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceitaCartao: {aceita_cartao}')
            print(f'naoAceitaCartao: {nao_aceita_cartao}')
            print(f'Velocidade Scripts: {velocidade_script}')
tela = TelaPython()
tela.iniciar()