import ctypes
def Mbox(title, text, style):
  return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('ERROR FFT89ED654QA7E', 'Une erreur a était detecter veuillez réesseyer !', 1)