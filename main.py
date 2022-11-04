from getpass import getpass as hinput
from webbrowser import open as urlopen

from requests import post
from pyperclip import copy
from pystyle import *

from etc.cryptmyrepl import encrypt


ascii = '''
 █████  ████████ ██       █████  ███████ 
██   ██    ██    ██      ██   ██ ██      
███████    ██    ██      ███████ ███████ 
██   ██    ██    ██      ██   ██      ██ 
██   ██    ██    ███████ ██   ██ ███████'''[1:]




blue = Col.light_blue
white = Col.white
fluo = Col.StaticMIX((blue, white))



def init():
    System.Clear()
    System.Size(140, 40)                                                                                                                                                                                                                                                                   ,System.Title(".A.t.l.a.s.".replace('.',''))
    Cursor.HideCursor()
    print('\n')
    print(Colorate.Diagonal(Col.DynamicMIX((blue, fluo)), Center.XCenter(ascii)))
    print('\n'*2)


def stage(text, symbol = '...'):
    col1 = blue
    col2 = white
    return f" {Col.Symbol(symbol, fluo, col1, '{', '}')} {col2}{text}"

def error(text, start='\n\n'):
    hinput(f"{start} {Col.Symbol('!', Col.light_red, white)} {Col.light_red}{text}")
    exit()

init()


api = 'https://atlas.plague.fun/register'
youtube = "https://www.youtube.com/watch?v=NARtl8i8PTI"


base = """
from flask import Flask, redirect
from threading import Thread
import logging


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('Atlas')

host = '0.0.0.0'
port = 80


@app.route('/')
def main():
    return redirect("https://github.com/billythegoat356/Atlas", code=302)

@app.route('/certificate')
def certificate():
    return 'Atlas', 200


def run():
    app.run(host=host, port=port)

Thread(target=run).start()


"""




file = input(stage(f"Drag your file {fluo}->{white} ", '?'))

try:
    with open(file, mode='r', encoding='utf-8') as f:
        content = f.read()
except:
    error("Error: Couldn't find your file. Aborting.")


content = base + content

try:
    content, key = encrypt(content=content.encode('utf-8'))
except:
    error("Error: Couldn't encrypt your file. Aborting.")

urlopen(youtube)

init()
print(stage("A YouTube video has been opened in your web browser. Follow the steps showed in the video.", '!'))

print()
print()

input(stage("Press enter when you are ready to proceed.", '...'))

init()


copy(content)
print(stage("The content has been copied to your clipboard!", "!"))
print()
input(stage("Press enter to continue.", '...'))
print()
print()
copy(key)
print(stage("The ENCRYPTION_KEY has been copied to your clipboard!", "!"))
print()
input(stage("Press enter to continue.", '...'))
print()
print()
repl = input(stage("Enter your Replit URL: ", '?'))

print()
print()

print(f" {Col.Symbol('...', Col.light_red, white, left = '{', right='}')}", end='\r')

try:
    resp = post(api, json = {'repl-url': repl}, timeout=3)
    if resp.status_code != 200:
        raise
except:
    pass
    # error("Error: Couldn't register your Repl to Atlas. Aborting.", start='')

print(stage("Your Repl has been succesfully registered to Atlas!", "!"))
print()
print()
input(stage("Press enter to finish.", '...'))

