import pyautogui
from time import sleep

pyautogui.PAUSE=0.5
pyautogui.press('win')
pyautogui.write('Google')
pyautogui.press('enter')
sleep(2)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=540, y=396)
pyautogui.write('teste@hotmail.com')
pyautogui.press('tab')
sleep(2)
pyautogui.write('Nico1307')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(x=1142, y=340)


pyautogui.click(x=453, y=280)
pyautogui.write('CODIGO')
pyautogui.press('tab')
pyautogui.write('MARCA')
pyautogui.press('tab')
pyautogui.write('TIPO')
pyautogui.press('tab')
pyautogui.write('CATEGORIA')
pyautogui.press('tab')
pyautogui.write('PRECO')
pyautogui.press('tab')
pyautogui.write('CUSTO')
pyautogui.press('tab')
pyautogui.write('OBS')
pyautogui.press('tab')
pyautogui.press('enter')

