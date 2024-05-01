import pyautogui
import time

#cria um alerta
pyautogui.alert('Automação em andamento...')

#sequência de teclas.
pyautogui.hotkey("win","r")

#será digitado o link do game
pyautogui.write("chrome https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)
pyautogui.press("ENTER")
time.sleep(9.5)

pyautogui.move(191, 321)
x,y=pyautogui.position()
click = True
while click:
    time.sleep(0.5)
    pyautogui.click(191,321)
    time.sleep(10)