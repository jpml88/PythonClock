from Tkinter import *
import time
import Tkinter

root = Tkinter.Tk()
root.attributes('-fullscreen', True)
canvas = Tkinter.Canvas(root)
canvas.pack(expand=1, fill=Tkinter.BOTH)
height = root.winfo_screenheight()
width  = root.winfo_screenwidth()

class Main:
    def __init__(self, canvas):
        self.canvas = canvas
        self.filename = PhotoImage(file = "Fondo_Pre.png")
        self.canvas.create_image(0,0, anchor=NW, image=self.filename)
        _clock = time.strftime('%H:%M')
        if(self.getrevision() != 'OK'):
            root.mainloop()
        self.texto = self.canvas.create_text(width / 2, height /2, text=self.getrevision(),font="Helvetica 500 bold")
    def tick(self):
        if(self.getrevision() != 'OK'):
            root.mainloop()
        time_now = time.strftime('%H:%M')
        self.canvas.itemconfigure(self.texto,text=time_now)
        self.canvas.after(50, self.tick)
    def getrevision(self):
        try:
            revision = "00000000"
            f = open('/proc/cpuinfo','r')
            for linea in f:
                if linea[0:6]=='Serial':
                    longitud =len(linea)
                    revision = linea[10:longitud-1]
            f.close()
            if(revision == '0000000082e25bbb'):
                revision = 'OK'
        except IOError:
            revision = "ERROR"
        return revision

main = Main(canvas)
main.tick()
root.mainloop()
