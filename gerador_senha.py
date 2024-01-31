import string
from random import choice
import PySimpleGUI as psg


def tela():
    """
    Função que define o formato da janela;
    """
    psg.theme('DarkBlack')

    estilo = [
        [psg.Text('Digite o tamanho da senha:'), psg.Input(key='tamanho_senha', size=5)],
        [psg.Output(size=(30, 5))],
        [psg.Button('Gerar senha', key='gerar_senha')]
    ]

    return psg.Window('Inicio', finalize=True, layout=estilo)


def gerador_senha(tamanho_senha):
    """
    Função que recebe um parâmetro e é resposável por gerar uma senha pseudoaleatória;
    O tamanho da senha é definida pelo parâmetro de entrada;
    A senha criado utiliza apenas números, letras maiúsculas e letras minúsculas;

    >>>gerador_acao(10)
    t7yyiloVfZ
    """
    caracteres = string.ascii_letters + string.digits
    senha = ''

    while len(senha) < tamanho_senha:
        senha += choice(caracteres)

    return senha


janela1 = tela()


while True:
    window, event, values = psg.read_all_windows()

    if window == janela1 and event == psg.WINDOW_CLOSED:
        break

    elif window == janela1 and event == 'gerar_senha':
        try:
            tamanho_senha = int(values['tamanho_senha'])
            senha = gerador_senha(tamanho_senha)
            print(f'Sua senha de {tamanho_senha} caracteres é:')
            print(f'{senha}\n')

        except:
            print('Digite um tamanho valido (EX: 10)\n')
