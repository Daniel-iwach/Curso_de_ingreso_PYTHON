import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:Daniel
apellido:Iwach
---
Ejercicio: Match_08
---
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el botón 
‘Informar’ indicar mediante alert si en el destino hace frío o calor la mayoría 
de las estaciones del año.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
          ubicacion=self.combobox_destino.get()
          match(ubicacion):
            case'Bariloche'|'Ushuaia':
                alert(title="Destino",message="En su destino hace frio la mayor parte del año")
            case'Mar del plata':
                alert(title="Destino",message="En su destino hace calor la mayor parte del año")
            case'Cataratas':
                  alert(title="Destino",message="En su destino hace calor la mayor parte del año")
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()