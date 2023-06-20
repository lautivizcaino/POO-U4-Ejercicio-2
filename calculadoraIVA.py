import tkinter as tk
from tkinter import messagebox,ttk
class Calculadora(tk.Tk):
    __sinIVA=None
    __iva=None
    __conIVA=None
    __valorIVA=None
    def __init__(self):
        super().__init__()
        self.title('Calculadora IVA')
        self.geometry('200x200')

        calculo=tk.Label(self,text='Cálculo de IVA',bg='sky blue').grid(row=0,column=0,columnspan=2,pady=5)
        
        precioSinIVA=tk.Label(self,text='Precio sin IVA').grid(row=1,column=0)

        self.__sinIVA=tk.StringVar()
        sinIVA=tk.Entry(self,textvariable=self.__sinIVA,width=15).grid(row=1,column=1)

        self.__valorIVA=tk.IntVar()
        iva21=tk.Radiobutton(self,text='IVA 21 %',value=21,variable=self.__valorIVA).grid(row=2,column=0)
        iva105=tk.Radiobutton(self,text='IVA 10.5 %',value=105,variable=self.__valorIVA).grid(row=3,column=0)
        self.__valorIVA.set(1)

        ivaLb=tk.Label(self,text='IVA').grid(row=4,column=0)
        self.__iva=tk.StringVar()
        iva=tk.Label(self,textvariable=self.__iva).grid(row=4,column=1)

        precioConIVA=tk.Label(self,text='Precio con IVA').grid(row=5,column=0)
        self.__conIVA=tk.StringVar()
        conIVA=tk.Label(self,textvariable=self.__conIVA).grid(row=5,column=1)



        calcular=tk.Button(self,text='Calcular',bg='PaleGreen1',padx=5,pady=5,command=lambda:self.calcularIVA()).grid(row=6,column=0)

        salir=tk.Button(self,text='Salir',bg='IndianRed1',padx=5,pady=5,command=quit).grid(row=6,column=1)

    def calcularIVA(self):
        if self.__sinIVA.get()!='':
            if self.__valorIVA.get()!=1:
                if self.__valorIVA.get()==21:
                    iva=float(self.__sinIVA.get())*0.21
                    self.__iva.set(iva)
                    self.__conIVA.set(iva+float(self.__sinIVA.get()))
                elif self.__valorIVA.get()==105:
                    iva=float(self.__sinIVA.get())*0.105
                    self.__iva.set(iva)
                    self.__conIVA.set(iva+float(self.__sinIVA.get()))
            else:
                messagebox.showerror(title='Error',message='Seleccione una opcion antes de realizar el cálculo')
        else:
            messagebox.showerror(title='Error',message='Ingrese un precio para realizar el calculo')