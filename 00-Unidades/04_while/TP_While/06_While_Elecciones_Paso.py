import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Daniel
apellido:iwach
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        mas_votos=0
        primer_candidato=1
        seguir=True
        total_edades=0
        candidatos=0
        votos_totales=0
        while seguir==True:
             nombre=prompt(title="candidatos", prompt="ingrese el nombre del cadidato")

             edad=prompt(title="candidatos", prompt="ingrese la edad del cadidato")
             while int(edad)<25:
                 edad=prompt(title="candidatos", prompt="ingrese la edad del cadidato")

             votos=prompt(title="candidatos", prompt="ingrese la cantidad de votos del cadidato")
             while int(votos)<0:
                 votos=prompt(title="candidatos", prompt="ingrese la cantidad de votos del cadidato")

             total_edades=total_edades+int(edad)
             candidatos=candidatos+1

             votos_totales=int(votos)+votos_totales

             if primer_candidato==1:
                 menos_votos=int(votos)

                 nombre_menos_votos=nombre
                 edad_menos_votos=edad
                 
                 primer_candidato=0

             if int(votos)<menos_votos:
                  nombre_menos_votos=nombre
                  edad_menos_votos=edad
                 

             if mas_votos<int(votos):
                 ganador=nombre
                 mas_votos=int(votos)
                 



             seguir=question("ingreso de candidatos","quiere continuar?")

        alert("candidatos","el nombre del candidato mas votado es "+ ganador)

        alert("candidatos"," el candidato menos votado fue "+nombre_menos_votos+" de "+edad_menos_votos+" años")

        promedio_edad=total_edades/candidatos
        alert("candidatos","el promedio de edades es "+str(promedio_edad))

        alert("candidattos"," el total de votos fue de "+str(votos_totales))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
