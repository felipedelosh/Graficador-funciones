"""
06/0/2019

Me propongo a crear una graficadora estatica de:

Seno:


"""

from tkinter import *
import math

class SW:
    def __init__(self):
        self.pantalla = Tk()
        self.tela = Canvas(self.pantalla, height=400, width=720, bg='white')
        self.btnPintarSeno = Button(self.tela, text="SEN", command=self.graficarSeno)
        self.btnPintarCoseno = Button(self.tela, text="COS", command=self.graficarCoseno)
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
        # Eje x
        self.tela.create_line(0,300, 720, 300)


        self.btnPintarSeno.place(x=20, y=20)
        self.btnPintarCoseno.place(x=100, y=20)


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
            self.tela.create_oval(i,y,i,y)
            self.tela.create_oval(i+360,y,i+360,y)

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
            self.tela.create_oval(i,y,i,y)
            self.tela.create_oval(i+360,y,i+360,y)



s = SW()