"""
06/0/2019

Me propongo a crear una graficadora estatica de:

Seno:

grafica el seno

cos

gra...


como se limpia : yo tageo todos los puntos del universo

"""

from tkinter import *
import math

class SW:
    def __init__(self):
        self.pantalla = Tk()
        self.tela = Canvas(self.pantalla, height=400, width=720, bg='white')
        self.btnPintarSeno = Button(self.tela, text="SEN", command=self.graficarSeno)
        self.btnPintarCoseno = Button(self.tela, text="COS", command=self.graficarCoseno)
        self.btnPintarTangente = Button(self.tela, text="TAN", command=self.graficarTangente)
        self.btnLimpiarPantalla = Button(self.tela, text="limpiar", command=self.limpiarPantalla)
        self.btnSenXX = Button(self.tela, text="(SENX)/X)", command=self.graficarSenoXX)
        self.lblYUP = Label(self.tela, text="1")
        self.lblMittle = Label(self.tela, text="0")
        self.lblButtom = Label(self.tela, text="-1")
        self.pi = 3.141593


        self.mostrarInterfaz()


    def mostrarInterfaz(self):
        """Configuracion de la pantalla principal"""
        self.pantalla.title("Funciones by loko")
        self.pantalla.geometry("720x400")
        """Configuracion de la pantalla"""
        self.tela.place(x=0, y=0) 
        self.tela.create_line(0,200, 720, 200, fill="cyan")

        # Eje y
        self.tela.create_line(360, 200, 360, 400)
        self.lblYUP.place(x = 350, y=200)
        self.lblMittle.place(x= 350, y=300)
        self.lblButtom.place(x= 350, y=380)
        # Eje x
        self.tela.create_line(0,300, 720, 300)


        self.btnPintarSeno.place(x=20, y=20)
        self.btnPintarCoseno.place(x=100, y=20)
        self.btnPintarTangente.place(x=180, y=20)
        self.btnLimpiarPantalla.place(x=600, y=150)
        self.btnSenXX.place(x=420, y=20)


        self.pantalla.mainloop()

    def graficarSeno(self):
        """
        A lo bestia es graficado el seno
        """
        angulo = 0
        # Pinto desde -pi a cero
        for i in range(0, 361):
            angulo = float((-(2-(i/180)))*(self.pi))
            # Calculo la cordenada en y 
            y = -(math.sin(angulo)*98)+300
            self.tela.create_oval(i,y,i,y, tag="graficar")
            self.tela.create_oval(i+360,y,i+360,y, tag="graficar")

    def graficarCoseno(self):
        """
        A lo bestia es graficado el coseno
        """
        angulo = 0
        # Pinto desde -pi a cero
        for i in range(0, 361):
            angulo = float((-(2-(i/180)))*(self.pi))
            # Calculo la cordenada en y 
            y = -(math.cos(angulo)*98)+300
            self.tela.create_oval(i,y,i,y, fill="dark blue", tag="graficar")
            self.tela.create_oval(i+360,y,i+360,y, fill="dark blue", tag="graficar")

    def graficarTangente(self):
        """
        A lo bestia es graficado el coseno
        """
        angulo = 0
        # Pinto desde -pi a cero
        for i in range(0, 361):
            angulo = float((-(2-(i/180)))*(self.pi))
            # Calculo la cordenada en y 
            y = -(math.tan(angulo)*98)+300
            if y > 200: 
                self.tela.create_oval(i,y,i,y, tag="graficar")
                self.tela.create_oval(i+360,y,i+360,y, tag="graficar")


    def graficarSenoXX(self):
        """Me dispongo a calcular sexx para todo -2pi hasta 0"""
        angulo = 0
        # pintooooooo -2pi to 
        for i in range(1, 720):
            angulo = float((-(2-(i/180)))*(self.pi))
            try:
                y = -((math.sin(angulo)/angulo)*98)+300
                self.tela.create_oval(i,y,i,y, tag="graficar")
            except:
                pass


    def limpiarPantalla(self):
        self.tela.delete("graficar")
            



s = SW()