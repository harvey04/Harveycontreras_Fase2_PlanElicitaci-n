#Estudiante: Harvey Alexander Contreras Gonzalez
#CC: 1024597908
#Grupo: 301305_228

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

valores_cargo = {
    "Servicios Generales": 40000,
    "Administrativo": 50000,
    "Electricista": 60000,
    "Mecánico": 80000,
    "Soldador": 90000
}

class GestionEmpleados:

    def __init__(self, identificacion, nombre, genero, cargo, dias):
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.cargo = cargo
        self.dias = dias
        self.fecha = datetime.now().strftime("%d/%m/%Y")

    def calcular_nomina(self):
        valor_dia = valores_cargo[self.cargo]
        return self.dias * valor_dia



def verificar():
    if entrada_password.get() == "4682":
        ventana_login.destroy()
        abrir_registro()
    else:
        messagebox.showerror("Error", "Contraseña incorrecta")


ventana_login = tk.Tk()
ventana_login.title("Acceso a la aplicación")
ventana_login.geometry("300x200")

tk.Label(ventana_login, text="Aplicación Nómina Empleados").pack(pady=10)
tk.Label(ventana_login, text="Harvey Alexander Contreras Gonzalez").pack(pady=10)
tk.Label(ventana_login, text="Ingrese contraseña").pack()

entrada_password = tk.Entry(ventana_login, show="*")
entrada_password.pack()

tk.Button(ventana_login, text="Ingresar", command=verificar).pack(pady=10)


def abrir_registro():

    global entry_id, entry_nombre, entry_dias, combo_cargo, valor_dia_label

    ventana = tk.Tk()
    ventana.title("Registro de Empleado")
    ventana.geometry("400x400")

    tk.Label(ventana, text="Identificación").pack()
    entry_id = tk.Entry(ventana)
    entry_id.pack()

    tk.Label(ventana, text="Nombre completo").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Género").pack()
    genero_var = tk.StringVar()
    tk.Radiobutton(ventana, text="Masculino", variable=genero_var, value="Masculino").pack()
    tk.Radiobutton(ventana, text="Femenino", variable=genero_var, value="Femenino").pack()

    tk.Label(ventana, text="Cargo").pack()
    combo_cargo = tk.StringVar(ventana)
    combo_cargo.set("Servicios Generales")

    cargos = list(valores_cargo.keys())
    menu = tk.OptionMenu(ventana, combo_cargo, *cargos)
    menu.pack()

    tk.Label(ventana, text="Valor día trabajo").pack()
    valor_dia_label = tk.Label(ventana, text="")
    valor_dia_label.pack()

    def mostrar_valor(*args):
        cargo = combo_cargo.get()
        valor_dia_label.config(text=str(valores_cargo[cargo]))

    combo_cargo.trace("w", mostrar_valor)
    mostrar_valor()

    tk.Label(ventana, text="Días trabajados").pack()
    entry_dias = tk.Entry(ventana)
    entry_dias.pack()

    def calcular():
        empleado = GestionEmpleados(
            int(entry_id.get()),
            entry_nombre.get(),
            genero_var.get(),
            combo_cargo.get(),
            int(entry_dias.get())
        )

        total = empleado.calcular_nomina()

        mostrar_reporte(empleado, total)

    tk.Button(ventana, text="Calcular Nómina / Mostrar Reporte", command=calcular).pack(pady=10)

    tk.Button(ventana, text="Salir", command=ventana.destroy).pack()

    ventana.mainloop()


def mostrar_reporte(emp, total):

    ventana = tk.Tk()
    ventana.title("Reporte Nómina")
    ventana.geometry("350x300")

    tk.Label(ventana, text="REPORTE EMPLEADO", font=("Arial", 14)).pack(pady=10)

    tk.Label(ventana, text="Identificación: " + str(emp.identificacion)).pack()
    tk.Label(ventana, text="Nombre: " + emp.nombre).pack()
    tk.Label(ventana, text="Género: " + emp.genero).pack()
    tk.Label(ventana, text="Cargo: " + emp.cargo).pack()
    tk.Label(ventana, text="Días trabajados: " + str(emp.dias)).pack()
    tk.Label(ventana, text="Fecha registro: " + emp.fecha).pack()

    tk.Label(ventana, text="Total a pagar: $" + str(total), font=("Arial", 12)).pack(pady=15)


ventana_login.mainloop()
