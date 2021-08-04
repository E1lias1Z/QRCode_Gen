#-----------------------------
from tkinter import *
from tkinter import messagebox

import pyqrcode
import png
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
        self.drawNameLabel()
        self.drawSafeQRButton()
    
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

    def drawNameLabel(self):
        self.filename = StringVar()
        Label(text="Имя файла:", font="Arial 12").grid(row=7, column=0, padx=20, pady=20)
        name_entry = Entry(self.mainWin, textvariable=self.filename, width=60).grid(row=7, column=1)

    #generate QRCode and saves to png-file
    def saveQRCode(self):
        # try:
        save_fol_get = self.save_folder.get()
        folder_correct = re.sub(r'\\', r'\\\\', save_fol_get)
        nameFile = self.filename.get() + ".png"
        folder = folder_correct + '\\' + nameFile
        try:
            if(self.url_get):
                self.qr_code.png(folder, scale = 6)
                Label(text="QR-код сохранен успешно!", font="Arial 14 bold", fg="#32CD32").grid(row=9, column=1, pady=20)
        except:
            messagebox.showerror("Ошибка!", "QR-код не сгенерирован успешно!")
    #showing the generated code on main window
    def ShowCode(self):
        global photo
        self.url_get = self.url.get()
        if(self.url_get):
            self.qr_code = pyqrcode.create(self.url_get)
            qrImage = self.qr_code.xbm(scale=6)
            photo = BitmapImage(data=qrImage)
            notificationLabel = Label(self.mainWin)
            notificationLabel.grid(row=8, column=1, padx=40)
            notificationLabel.config(image = photo)
        else:
            messagebox.showerror("Ошибка!", "URL не был введен или введен неверно! Повторите ввод!")
    #draws button for make QRCode command
    def drawQRButton(self):
        Button(self.mainWin, text='Сгенерировать QR-код', command=self.ShowCode, font="Arial 12").grid(row=6, column=2, padx=20, pady=20)
    #draws button for saving to PNG-file
    def drawSafeQRButton(self):
        Button(self.mainWin, text='Сохранить в PNG', font="Arial 12", command=self.saveQRCode).grid(row=7, column=2, padx=20, pady=20)
    #running application
    def run(self):
        self.widgetsApp()
        self.mainWin.mainloop()

#--------------------------------------------------------------------------------------------

app = Application(800, 580)
app.run()

#-------------------------------------------------------------------------------------------- 


