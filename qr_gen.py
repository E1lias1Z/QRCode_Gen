#-----------------------------
from tkinter import *
from tkinter import messagebox

import pyqrcode
import png
import random
import string
import re
#-----------------------------
#main class of main application
class Application:
    #initialize window of application
    def __init__(self, width, height, title= 'Генератор QR-кода'):
        self.mainWin = Tk()
        self.mainWin.geometry('x'.join([str(width), str(height)]))
        self.mainWin.title(title)
        self.mainWin.resizable(width=False, height=False)
    #draws elements of app
    def widgetsApp(self):
        self.drawURLLabel()
        self.drawQRButton()
        self.drawSaveFolder()
    #draws label for url-link
    def drawURLLabel(self):
        self.url = StringVar()
        Label(text="Введите URL: ", font="Arial 12").grid(row=0, column=0, padx=20, pady=20)
        Entry(self.mainWin, textvariable=self.url, width=60).grid(row=0, column=1)
        #string bar for link of folder
    def drawSaveFolder(self):
        self.save_folder = StringVar()
        Label(text="Путь сохранения:", font="Arial 12").grid(row=6, column=0, padx=20)
        folder_Entry = Entry(self.mainWin, textvariable=self.save_folder, width=60).grid(row=6, column=1)
    #generate QRCode and saves to png-file
    def genQRCode(self):
        # try:
        url_get = self.url.get(); save_fol_get = self.save_folder.get()
        folder_correct = re.sub(r'\\', r'\\\\', save_fol_get)
        if(url_get):
            qr_code = pyqrcode.create(url_get); nameFile = "QR_code_" + random.choice(string.ascii_letters) + ".png"
            folder = folder_correct + '\\' + nameFile
            qr_code.png(folder, scale = 10)
            Label(text="QR-код сгенерирован успешно!", font="Arial 14 bold", fg="#32CD32").grid(row=7, column=1, pady=20)
        else:
            messagebox.showerror("Ошибка!", "URL не был введен или введен неверно! Повторите ввод!")
        # except exceptions.RegexMatchError:
        #     messagebox.showerror("Ошибка!", "Введен неверный URL! Повторите ввод!")
    #draws button for make QRCode command
    def drawQRButton(self):
        Button(self.mainWin, text='Сгенерировать QR-код', command=self.genQRCode).grid(row=7, column=0, padx=20, pady=20)
    #running application
    def run(self):
        self.widgetsApp()
        self.mainWin.mainloop()

#--------------------------------------------------------------------------------------------

app = Application(600, 200)
app.run()
#-------------------------------------------------------------------------------------------- 


