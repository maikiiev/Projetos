import pandas

tabela = pandas.read_csv(r'C:\Users\MIKE\Downloads/Compras.csv', sep=';')
display(tabela)
total_gasto = tabela['ValorFinal']. sum()
quantidade = tabela['Quantidade']. sum()
preco_medio = total_gasto/quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)

import pyautogui
import time
import pyperclip
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://outlook.live.com/mail/0/')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=216, y=210)
time.sleep(5)
pyautogui.write('luanova537@gmail.com')
time.sleep(2)
pyautogui.press('tab')
time.sleep(1.5)
pyautogui.press('tab')
time.sleep(1.5)
pyperclip.copy('Relatório')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = f'''Prezados, segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}

Quantidade de Produtos: {quantidade:,}

Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida retorne para mim.

att: Michael Douglas
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.hotkey('ctrl', 'enter')