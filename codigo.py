import pyautogui
from time import sleep
#pip install pandas numpy openpyxl
import pandas

#teste

pyautogui.PAUSE=0.5
pyautogui.press('win')
pyautogui.write('Google')
pyautogui.press('enter')
sleep(2)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=540, y=396)
pyautogui.write('teste@hotmail.com')
pyautogui.press('tab')
sleep(1)
pyautogui.write('Nico1307')
sleep(1)
pyautogui.press('enter')
sleep(2)
pyautogui.click(x=1142, y=340)

tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']

    pyautogui.click(x=453, y=280)
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(tipo)
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    if not pandas.isna(obs):
     pyautogui.write(str(obs))

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)

