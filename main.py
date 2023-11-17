import speech_recognition as sr
import subprocess
import pyautogui

regognizer = sr.Regognizer()
proceso = None

saludo='epale'

def ejecutar(comando):
    global proceso
    if "abrir" in comando:
        proceso = subprocess.Popen(['notepad.exe'])
    elif "saludar" in comando:
        pyautogui.write(saludo)
    elif "cerrar" in comando:
        proceso.termnate()

def escuchar():
    with sr.Microphone() as source:
        print('dime')
        regognizer.adjust_for_ambient_noise(source)
        audio = regognizer.listen(source)
    try:
        comando = regognizer.recognizer_google(audio, language='es-ES')
        print(comando)
        ejecutar(comando)
    except sr.UnkownValueError:
        print("Unkown value")
    except sr.RequestError as e:
        print(e)

while True:
    escuchar()        