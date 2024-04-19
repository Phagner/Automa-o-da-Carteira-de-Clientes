import pyautogui as py
import os
import time
import subprocess
import cv2

#funções
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def localizar(name,localizando_oq,sml):
    for tentar in range(60):
        try:
            py.locateOnScreen(fr"C:\img\{name}.png", confidence=sml)
            print(f"localizado {localizando_oq}")
            valor = 1
            break

        except:
            print(f"localizando {localizando_oq}", tentar)
            time.sleep(1)
            valor = 0

    if valor == 0:
        print(f"FALHA AO LOCALIZAR {localizando_oq}")
        exit()


# ENTRAR NO PROTHEUS


"""local = r"C:\TOTVS 12.1.2210 - SMARTCLIENT 20.3.1.5\smartclient.exe"
subprocess.Popen(local)"""



"""localizar("pi","parametros inicias",9)
print(" ok")"""

ponto = py.locateOnScreen(fr"C:\img\ic.png", confidence=9)
ponto = py.center(ponto)
py.click(ponto)