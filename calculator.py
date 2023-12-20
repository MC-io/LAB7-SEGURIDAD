from md5 import MD5
from md4 import MD4
from hmac_hash import calcular_hmac
from tkinter import *
from sha import calcular_sha1, calcular_sha256

class Calculator:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Mensaje a Codificar')
        self.lbl2=Label(win, text='Tipo de Hash')
        self.lbl3=Label(win, text='Mensaje Codificado')
        self.lblc = Label(win, text = 'Clave secreta')
        self.lblc.place(x=350, y=100) 
        self.lblc.pack()
        self.lblc.pack_forget()
        OPTIONS = [
        "MD4",
        "MD5",
        "SHA-1",
        "SHA-256",
        "HMAC"
        ]
        self.t1 = Entry(bd=3, width=50)
        self.clave = Entry(bd=3, width=20)
        self.clave.place(x=450, y=100)
        self.clave.pack()
        self.clave.pack_forget()

        self.hash_function = StringVar(win)
        self.hash_function.set(OPTIONS[0])
        self.t2 = OptionMenu(win, self.hash_function, *OPTIONS)
        self.hash_function.trace_add("write", self.callback)
        self.t2.pack()
        self.t3 = Entry(width=65)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=250, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=250, y=100)
        self.b1=Button(win, text='Generar Hash', command=self.perform_hash)
        self.b1.place(x=300, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=250, y=200)
    def callback(self, *args):
        if self.hash_function.get() == "HMAC":
            self.clave.pack()
            self.clave.place(x=450, y=100)
            self.lblc.pack()
            self.lblc.place(x=350, y=100)
        else:
            self.clave.pack()
            self.clave.pack_forget()
            self.lblc.pack()
            self.lblc.pack_forget()

    def perform_hash(self):
        message = self.t1.get()
        if self.hash_function.get() == "MD4":
            self.md4_hash(message)
        elif self.hash_function.get() == "MD5":
            self.md5_hash(message)
        elif self.hash_function.get() == "SHA-1":
            self.sha1_hash(message)
        elif self.hash_function.get() == "SHA-256":
            self.sha256_hash(message)
        else:
            key = self.clave.get()
            self.hmachash(message, key)
        
    def md4_hash(self, message):
        self.t3.delete(0, 'end')
        md4 = MD4()
        self.t3.insert(END, str(md4.digest(message)))
    def md5_hash(self, message):
        self.t3.delete(0, 'end')
        md5 = MD5()
        self.t3.insert(END, str(md5.digest(message)))
    def hmachash(self, message, clave):
        self.t3.delete(0, 'end')
        self.t3.insert(END, str(calcular_hmac(message, clave)))
    def sha1_hash(self, message):
        self.t3.delete(0, 'end')
        self.t3.insert(END, str(calcular_sha1(message)))
    def sha256_hash(self, message):
        self.t3.delete(0, 'end')
        self.t3.insert(END, str(calcular_sha256(message)))

def main():    
    master = Tk()
    my_calc = Calculator(master)
    master.title('Calculadora Hash')
    master.geometry("700x300+10+10")
    master.mainloop()

if __name__ == "__main__":
    main()