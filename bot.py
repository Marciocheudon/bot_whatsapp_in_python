# importando bibliotecas
import pywhatkit
import keyboard
import time
from datetime import datetime

# Envio de imagens já pré-definidas para números pré-definidos
pywhatkit.sendwhats_image(phone_no = "+5521xxxxxxxxx", img_path =  str(r"C:\Users\Pc\Desktop\Bruh_lanches\img\img1.jpg"), caption = str("Boa noite pessoal, segue o novo cardápio, já estamos abertos para pedidos. Quem puder compartilhar, ajudaria muito"))
keyboard.press_and_release('ENTER')

# Definindo horario
datetime.now().hour, datetime.now().minute + 1
time.sleep(30)
keyboard.press_and_release('CTRL + W')
