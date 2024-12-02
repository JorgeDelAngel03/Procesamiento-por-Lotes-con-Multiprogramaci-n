#Del Ángel Mercado Jorge Rafael
#Martínez Ríos Evelyn Yanet
import tkinter as tk
import customtkinter as ctk
import random
import math
from tkinter import messagebox

def operacion(num_1, num_2, signo):  #Función para determinar la cadena de la operación
    signos = ["+", "-", "*", "/", "%"]
    return f"{num_1} {signos[signo - 1]} {num_2}"

procesos = []
def validar_entero(P): #Función para aceptar solamente dígitos numéricos
    if P.isdigit() or P == "":
        return len(P) <= 5
    else:
        return False
#Ventana 1 - Número de Procesos y generación automática de estos
class NumeroProcesos(ctk.CTk): 
    def __init__(self):
        super().__init__()    
        self.resizable(False, False)
        # Configurar la ventana principal
        self.title("Número de procesos")
        self.geometry("330x210")
        global n_procesos
        global procesos
        label1 = ctk.CTkLabel(self, text="Número de procesos", padx=10, pady=10, font=("Arial", 16, "bold"))
        label1.pack(pady=10)
        validacion = self.register(validar_entero)

        self.entrada_variable = tk.StringVar()
        entrada = ctk.CTkEntry(self, textvariable=self.entrada_variable, validate="key", validatecommand=(validacion, "%P"), font=("Arial", 16), justify="center")
        entrada.pack(pady=20, padx=20)

        mostrar_boton = ctk.CTkButton(self, text="Aceptar", command=self.validar_valor, font=("Arial", 14, "bold"))
        mostrar_boton.pack(pady=10)

    def validar_valor(self): #Determinar si el número de procesos ingresados es válido
        global n_procesos
        if self.entrada_variable.get() == "" or self.entrada_variable.get() == "0":
            messagebox.showwarning("Advertencia", "El número de procesos debe ser mayor a 0")
        else:
            n_procesos = int(self.entrada_variable.get())
            messagebox.showinfo("¡Felicidades!", "Número de procesos asignado correctamente.") 
            for i in range(n_procesos):
                id=i+1
                num_1= random.randint(-100, 100) 
                num_2 = random.randint(-100,100)
                signo = random.randint(1,5)
                tme = random.randint(5,18)
    
                while (signo == 4 or signo == 5) and num_2 == 0:   #Validación  para evitar 0 en el denominador
                    num_2 = random.randint(-100, 100)
                
                procesos.append( {          #Agregar un proceso a la lista de procesos
                    "id": id,
                    "num_1": num_1,
                    "num_2": num_2,
                    "signo": signo,
                    "tme": tme,
                    "tt": 0
                })    
            self.destroy()  #Cerrar la ventana

batches = []
def asignar_lotes():    #Función para asignar los procesos a cada lote
    global n_batches, batches
    batches = []
    n_batches = math.ceil(n_procesos / 5)
    for i in range(1, n_batches + 1):
        batch = []
        for j in range((i - 1) * 5 + 1, len(procesos) + 1):
            batch.append(procesos[j - 1])
            if (j % 5 == 0): break
        batches.append(batch)
#Ventana 2 - Ejecución de procesos y lotes
class Lotes(ctk.CTkFrame):
    def __init__(self, master, num_lotes_pend, **kwargs):
        super().__init__(master, **kwargs)

        self.num_lotes_pend = num_lotes_pend  #Número de lotes pendientes
        #Etiqueta para los lotes pendientes
        label_1 = ctk.CTkLabel(self, text="No. Lotes Pendientes:  ", padx=5, pady=5, font=("Arial", 16, "bold"))
        label_1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.num_lotes = ctk.CTkLabel(self, text=str(self.num_lotes_pend), padx=5, pady=5, font=("Arial", 16, "bold"))
        self.num_lotes.grid(row=0, column=1, padx=10, pady=5)

    def lote_completado(self): #Función para alterar el número de lotes pendientes
        self.num_lotes_pend -= 1
        self.num_lotes.configure(text=f"{self.num_lotes_pend}")

class Procesos_Pendientes(ctk.CTkFrame): #Tabla de procesos del lote actual pendientes
    def __init__(self, master, lote_inicial, **kwargs):
        super().__init__(master, **kwargs)
        self.lotes_pendientes = master.lote
        self.lote_actual = 1
        self.proceso_inicial = lote_inicial.pop(0)
        self.lote_procesar = lote_inicial
        self.num_pros_pend = len(self.lote_procesar)
        self.row_count = 2
        self.labels_procesos = []
        #Etiquetas para los procesos pendientes
        label_1 = ctk.CTkLabel(self, text="Procesos Pendientes \n del lote actual: ", padx=5, pady=5, font=("Arial", 14, "bold"))
        label_1.grid(row=0, column=0, padx=10, pady=5)
        self.num_pros = ctk.CTkLabel(self, text=str(self.num_pros_pend), padx=5, pady=5, font=("Arial", 14, "bold"), justify="center")
        self.num_pros.grid(row=0, column=1, padx=10, pady=5)

        label_id = ctk.CTkLabel(self, text="ID:", padx=5, pady=5, font=("Arial", 12, "bold"))
        label_id.grid(row=1, column=0, padx=10, pady=5)
        label_tme = ctk.CTkLabel(self, text="TME:", padx=5, pady=5, font=("Arial", 12, "bold"))
        label_tme.grid(row=1, column=1, padx=5, pady=5)
        label_tt = ctk.CTkLabel(self, text="TT:", padx=5, pady=5, font=("Arial", 12, "bold"))
        label_tt.grid(row=1, column=2, padx=5, pady=5)
        #Ciclo para crear la tabla de procesos pendientes de manera automática
        self.crear_labels()
    def crear_labels(self):
        for i in range(0,5):
            label_id = ctk.CTkLabel(self, text="", font=("Arial", 14))
            label_id.grid(row=self.row_count, column = 0, padx = 5, pady = 5)
            label_tme = ctk.CTkLabel(self, text="", font=("Arial", 14))
            label_tme.grid(row=self.row_count, column = 1, padx = 5, pady = 5)
            label_tt = ctk.CTkLabel(self, text="", font=("Arial", 14))
            label_tt.grid(row=self.row_count, column = 2, padx = 5, pady = 5)
            self.labels_procesos.append((label_id, label_tme, label_tt))
            self.row_count += 1
        for i in range(0, self.num_pros_pend):  
            self.labels_procesos[i][0].configure(text=f"{self.lote_procesar[i]['id']}")
            self.labels_procesos[i][1].configure(text=f"{self.lote_procesar[i]['tme']}")
            self.labels_procesos[i][2].configure(text=f"{self.lote_procesar[i]['tt']}")

    #Función para limpiar la tabla de procesos pendientes
    def limpiar_procesos(self): 
        for label_id, label_tme, label_tt in self.labels_procesos:
            label_id.configure(text="")
            label_tme.configure(text="")
            label_tt.configure(text="")
    def encolar_proceso(self, proceso):
        self.labels_procesos[self.num_pros_pend - 1][0].configure(text=f"{proceso['id']}")
        self.labels_procesos[self.num_pros_pend - 1][1].configure(text=f"{proceso['tme']}")
        self.labels_procesos[self.num_pros_pend - 1][2].configure(text=f"{proceso['tt']}")
    #Función para recorrer los procesos en la tabla cada que termina un proceso
    def recorrer_procesos(self):
        for i in range (0, self.num_pros_pend):
            self.labels_procesos[i][0].configure(text=f"{self.labels_procesos[i+1][0].cget("text")}")
            self.labels_procesos[i][1].configure(text=f"{self.labels_procesos[i+1][1].cget("text")}")
            self.labels_procesos[i][2].configure(text=f"{self.labels_procesos[i+1][2].cget("text")}")
        self.labels_procesos[self.num_pros_pend][0].configure(text="")
        self.labels_procesos[self.num_pros_pend][1].configure(text="")
        self.labels_procesos[self.num_pros_pend][2].configure(text="")
    #Función para cambiar la lista de procesos cuando cambia el lote
    def cambiar_procesos(self):
        if(self.num_pros_pend > 0): 
            self.num_pros_pend -= 1
            self.num_pros.configure(text=f"{self.num_pros_pend}")
        if (self.num_pros_pend == 0 and self.lotes_pendientes.num_lotes_pend == 0):
            self.limpiar_procesos()
    #Función para cambiar el lote
    def cambiar_lote(self):
        self.lotes_pendientes.lote_completado()
        self.lote_procesar = batches[self.lote_actual]
        #self.proceso_inicial = self.lote_procesar.pop(0)
        self.num_pros_pend = len(self.lote_procesar) - 1
        self.num_pros.configure(text=f"{self.num_pros_pend}")
        num_label = 0
        for i in range (1, len(self.lote_procesar)):
            self.labels_procesos[num_label][0].configure(text=f"{self.lote_procesar[i]['id']}")
            self.labels_procesos[num_label][1].configure(text=f"{self.lote_procesar[i]['tme']}")
            self.labels_procesos[num_label][2].configure(text=f"{self.lote_procesar[i]['tt']}")
            num_label += 1
        self.lote_actual += 1
#CLase para la tabla de los procesos en ejecución
class Procesos_Ejecucion(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.procesos_programados = master.proceso_pend
        self.procesos_terminados = master.proceso_term
        self.contador = master.contador
        self.tiempo_transcurrido = 0
        self.tiempo_restante = 0
        self.num_pros_eje = 1
        self.lote_actual = self.procesos_programados.lote_procesar
        self.ope = ""
        self.ejecutar = True
        #Etiquetas informativas
        label_1 = ctk.CTkLabel(self, text="Proceso en\nEjecución:", padx=5, pady=5, font=("Arial", 14, "bold"), justify="center")
        label_1.grid(row=0, column=0, padx=10, pady=5)
        self.num_eje = ctk.CTkLabel(self, text=f" {self.num_pros_eje} ", padx=20, pady=5, font=("Arial", 14, "bold"), justify="center")
        self.num_eje.grid(row=0, column=1, padx=10, pady=5)

        #Columna 1
        label_id = ctk.CTkLabel(self, text="ID:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_id.grid(row=1, column=0, padx=5, pady=5)
        label_ope = ctk.CTkLabel(self, text="Operación:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_ope.grid(row=2, column=0, padx=5, pady=5)
        label_ope = ctk.CTkLabel(self, text="Tiempo Max\nEstimado:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_ope.grid(row=3, column=0, padx=5, pady=5)
        label_tt = ctk.CTkLabel(self, text="Tiempo  \nTranscurrido:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_tt.grid(row=4, column=0, padx=5, pady=5)
        label_tr = ctk.CTkLabel(self, text="Tiempo\n  Restante:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_tr.grid(row=5, column=0, padx=5, pady=5)

        #Columna 2
        self.texto_id = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_id.grid(row=1, column=1, padx=5, pady=5)
        self.texto_ope = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_ope.grid(row=2, column=1, padx=5, pady=5)
        self.texto_tme = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_tme.grid(row=3, column=1, padx=5, pady=5)
        self.texto_tt = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_tt.grid(row=4, column=1, padx=5, pady=5)
        self.texto_tr = ctk.CTkLabel(self, text="", padx=5, pady=5, font=("Arial", 13))
        self.texto_tr.grid(row=5, column=1, padx=5, pady=5)
        self.proceso_en_ejecucion(self.procesos_programados.proceso_inicial)
        self.avanzar_tiempo()
    #Función para el cambio de proceso en la tabla
    def proceso_en_ejecucion(self, proceso):
        self.proceso_actual = proceso
        self.tiempo_transcurrido = self.proceso_actual['tt']
        self.texto_id.configure(text=f"{self.proceso_actual['id']}")
        self.ope = operacion(self.proceso_actual['num_1'], self.proceso_actual['num_2'], self.proceso_actual['signo']) 
        self.texto_ope.configure(text=self.ope)
        self.texto_tme.configure(text=f"{self.proceso_actual['tme']}")
        self.texto_tt.configure(text=f"{self.tiempo_transcurrido}")
        self.tiempo_restante = self.proceso_actual['tme'] - self.proceso_actual['tt']
        self.texto_tr.configure(text=f"{self.tiempo_restante}")
    def error_proceso(self):
        self.procesos_terminados.agregar_proceso(self.proceso_actual, self.procesos_programados.lote_actual, self.ope, False)  
        if(self.num_pros_eje < len(procesos)): 
            self.procesos_programados.cambiar_procesos()       
            self.nuevo_proceso()
            self.num_pros_eje += 1
            self.num_eje.configure(text=f"{self.num_pros_eje}")
        else: 
            self.tiempo_restante = 0
            self.limpiar_datos()
    def interrumpir_proceso(self):
        self.proceso_actual['tt'] = self.tiempo_transcurrido
        self.lote_actual.append(self.proceso_actual)
        self.nuevo_proceso()
        self.procesos_programados.encolar_proceso(self.lote_actual[len(self.lote_actual) - 1])
    def nuevo_proceso(self):
        if(self.procesos_programados.num_pros_pend >= 0 and self.procesos_programados.num_pros_pend != len(self.lote_actual)):
            self.procesos_programados.recorrer_procesos()  
        else:
            self.procesos_programados.cambiar_lote()
            self.lote_actual = self.procesos_programados.lote_procesar
        self.proceso_actual = self.lote_actual.pop(0)
        self.proceso_en_ejecucion(self.proceso_actual)
    #Función para limpiar los campos de la tabla de procesos
    def limpiar_datos(self):
        self.ejecutar = False
        self.num_eje.configure(text="N/A")
        self.texto_id.configure(text="")
        self.texto_ope.configure(text="")
        self.texto_tme.configure(text="")
        self.texto_tt.configure(text="")
        self.texto_tr.configure(text="")
        self.contador.terminar()
    #Función para el avance del tiempo en la ejecución del proceso
    def avanzar_tiempo(self):
        if (self.ejecutar == False): return
        self.tiempo_transcurrido += 1
        self.tiempo_restante -= 1
        self.texto_tt.configure(text=f"{self.tiempo_transcurrido}")
        self.texto_tr.configure(text=f"{self.tiempo_restante}")    

        if (self.tiempo_restante == 0): #Si el tiempo restante es 0, se hace lo siguiente:
            self.procesos_terminados.agregar_proceso(self.proceso_actual, self.procesos_programados.lote_actual, self.ope, True)  
            #Si ya no existe ningún proceso ni lote, se termina el conteo
            if (self.procesos_programados.lotes_pendientes.num_lotes_pend == 0 and self.procesos_programados.num_pros_pend == 0 and self.tiempo_restante == 0): 
                self.limpiar_datos()
                return
            self.procesos_programados.cambiar_procesos()
            self.nuevo_proceso()
            self.num_pros_eje += 1
            self.num_eje.configure(text=f"{self.num_pros_eje}")

        self.after(1000, self.avanzar_tiempo) #Esto se ejecuta cada segundo
#Clase para la tabla de procesos terminados
class Procesos_Terminados(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.num_pros_term = 0 
        self.row_count = 2 #Esto nos sirve para ubicarnos en la tabla correctamente
        #Etiquetas informativas
        label_1 = ctk.CTkLabel(self, text="Procesos \nTerminados: ", padx=5, pady=5, font=("Arial", 14, "bold"))
        label_1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.num_term = ctk.CTkLabel(self, text=str(self.num_pros_term), padx=5, pady=5, font=("Arial", 14, "bold"))
        self.num_term.grid(row=0, column=1, padx=10, pady=5)
        #Etiquetas de encabezado de los procesos finalizados
        label_lote = ctk.CTkLabel(self, text="No. Lote:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_lote.grid(row=1, column=0, padx=10, pady=5)
        label_id = ctk.CTkLabel(self, text="ID:", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_id.grid(row=1, column=1, padx=10, pady=5)
        label_ope = ctk.CTkLabel(self, text="Operación: ", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_ope.grid(row=1, column=2, padx=5, pady=5)
        label_res = ctk.CTkLabel(self, text="Resultado: ", padx=5, pady=5, font=("Arial", 12, "bold"), justify="center")
        label_res.grid(row=1, column=3, padx=5, pady=5)
    #Función para agregar un proceso finalizado a la tabla de procesos finalizados
    def agregar_proceso(self, proceso, lote, ope, correcto):
        ctk.CTkLabel(self, text=f"{lote}", font=("Arial", 13)).grid(row=self.row_count, column = 0, pady = 5)
        ctk.CTkLabel(self, text=f"{proceso['id']}", font=("Arial", 13)).grid(row=self.row_count, column = 1, pady = 5)
        ctk.CTkLabel(self, text=f"{ope}", font=("Arial", 13)).grid(row=self.row_count, column = 2, pady = 5)
        if (correcto == False):
            ctk.CTkLabel(self, text="Error", font=("Arial", 13)).grid(row=self.row_count, column=3, pady=5)
        else:
            ctk.CTkLabel(self, text=f"{int(eval(ope)) if eval(ope).is_integer() else f'{eval(ope):.2f}'}", font=("Arial", 13)).grid(row=self.row_count, column=3, pady=5)
        self.row_count += 1
        self.num_pros_term += 1
        self.num_term.configure(text=f"{self.num_pros_term}")

#Clase del contador que muestra el tiempo transcurrido
class Contador(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tiempo_total = 0
        self.contar = True  #Esto nos sirve para saber cuándo finalizar el conteo
        #Etiquetas informativas
        label_1 = ctk.CTkLabel(self, text="Contador:", padx=5, pady=5, font=("Arial", 16, "bold"))
        label_1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.label_tiempo = ctk.CTkLabel(self, text="0", padx=5, pady=5, font=("Arial", 16, "bold"))
        self.label_tiempo.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.actualizar_tiempo()
    #Función para contar
    def actualizar_tiempo(self):
        if self.contar == True and self.master.terminar == False:  #Siempre que contar sea True, cuenta
            self.label_tiempo.configure(text=f"{self.tiempo_total}")
            self.tiempo_total += 1
            self.after(1000, self.actualizar_tiempo)
    #Función para terminar el conteo
    def terminar(self):
        self.contar = False #Aquí determinamos que ya no queremos contar
        self.master.terminar = True
        messagebox.showinfo("Finalizar", "¡Todos los procesos han sido terminados!")
#Clase para la ventana 3 de ejecución de procesos
class Aplicacion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.ejecutar = True
        self.terminar = False
        self.puede = False
        #proceso_ejecucion = batches[0][0]   #Proceso inicial
        self.num_pros_pend=len(batches[0])  #Determinar cuántos procesos tiene el lote
        self.num_lotes_pend=len(batches) - 1    #Determinar cuántos lotes quedan pendientes
        #Configuración de la ventana
        self.title("Ventana de Procesos")
        self.grid_rowconfigure(0, weight=0)  
        self.grid_columnconfigure(0, weight=0)
        self.resizable(False, False)
        #Creación del contador global
        self.contador = Contador(master=self)
        self.contador.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")
        #Creación del cuadro de lotes pendientes
        self.lote = Lotes(master=self, num_lotes_pend=self.num_lotes_pend)
        self.lote.grid(row=0, column=0, padx=30, pady=20, sticky="nw")
        #Creación de la tabla de procesos pendientes
        self.proceso_pend = Procesos_Pendientes(master=self, lote_inicial=batches[0])
        self.proceso_pend.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        #Creación de la tabla de procesos terminados
        self.proceso_term = Procesos_Terminados(master=self, width = 340)
        self.proceso_term.grid(row=1, column=2, padx=20, pady=10, sticky="nsew")
        #Creación de la tabla de procesos en ejecución
        self.proceso_eje = Procesos_Ejecucion(master=self)
        self.proceso_eje.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

        self.bind("<KeyRelease>", self.key_pressed)
    def key_pressed(self, event):
        tecla = event.keysym.lower()
        print(f"Tecla presionada: {event.keysym}")
        if(tecla == "i" and self.contador.contar == True and self.proceso_pend.num_pros_pend > 0):
            self.proceso_eje.interrumpir_proceso()
        if(tecla == "e" and self.contador.contar == True and self.proceso_eje.num_pros_eje <= len(procesos)):
            self.proceso_eje.error_proceso()
        if(tecla == "p" and self.ejecutar == True and not self.terminar):
            self.ejecutar = False
            self.proceso_eje.ejecutar = False
            self.contador.contar = False
            self.after(1000, self.bandera)
        if(tecla == "c" and self.ejecutar == False and self.puede == True and not self.terminar):
            self.continuar()
    def bandera(self):
        self.puede = True
    def continuar(self):
        self.proceso_eje.ejecutar = True
        self.proceso_eje.avanzar_tiempo()
        self.contador.contar = True
        self.contador.actualizar_tiempo()
        self.ejecutar = True
        self.puede = False

inicial = NumeroProcesos()
inicial.mainloop()

asignar_lotes()

lotes = Aplicacion()
lotes.mainloop()