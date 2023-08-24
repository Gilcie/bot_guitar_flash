import pyautogui
from time import sleep
import keyboard

#Iniciar o jogo
pyautogui.click(2560,733, duration=1)

#Mapear Botões



#Pressionar Botões
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(2413,922, (0, 152, 0)):
        pyautogui.press('a')
        sleep(0.05)

    if pyautogui.pixelMatchesColor(2504,921, (255,0,0)):
        pyautogui.press('s')
        sleep(0.05)

    if pyautogui.pixelMatchesColor(2592,920, (244,244,2)):
        pyautogui.press('j')
        sleep(0.05)

