import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Daniel
apellido:Iwach
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos=0
        suma_negativos=0
        positivos=0
        negativos=0
        ceros=0
        diferencia=0
        while True:
           numero=prompt(title="numeros", prompt="ingrese un numero")
           if numero is None :   
            break 
           numero=int(numero)

           if numero==0:
              ceros=ceros+1


           elif numero>0:
              positivos=positivos+1
              suma_positivos=suma_positivos+numero


           elif numero<0:
              negativos=negativos+1  
              suma_negativos=suma_negativos+numero


        diferencia=positivos-negativos

        primera_linea="la suma de negativos="+str(suma_negativos)
        segunda_linea="la suma de positivos="+str(suma_positivos)
        tercera_linea="la cantidad de numeros positivos es de "+str(positivos)+" numero/s"
        cuarta_linea="la cantidad de numeros negativos es de "+str(negativos)+" numero/s"
        quinta_linea="la cantidad de ceros ingresados es de "+str(ceros)
        sexta_linea="la diferencia entre la cantidad de positivos y negativos da "+str(diferencia)



        alert(title="resultados", message=primera_linea+"\n"+segunda_linea+"\n"+tercera_linea+"\n"+cuarta_linea+"\n"+quinta_linea+"\n"+sexta_linea)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
