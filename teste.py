# Edite o código onde está o link do outlook e coloque o link do seu outlook! onde já esteja logado

import pyautogui
import time
import pyperclip
pyautogui.press('win')
time.sleep(2)
pyautogui.write('Opera')
pyautogui.press('enter')
time.sleep(5)  
pyautogui.write('https://outlook.live.com/owa/')
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('N')
time.sleep(10)
pyautogui.write('maikiiev22@hotmail.com')
time.sleep(2)
pyautogui.press('tab')
time.sleep(1.5)
pyautogui.press('tab')
time.sleep(1.5)
pyperclip.copy('Relatório')
pyautogui.hotkey('ctrl','v')
time.sleep(2)
pyautogui.press('tab')
pyperclip.copy('Olá isso é um teste')
pyautogui.hotkey('ctrl','v')
time.sleep(3)
pyautogui.hotkey('ctrl', 'enter')