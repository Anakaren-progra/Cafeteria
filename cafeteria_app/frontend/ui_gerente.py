# ui_gerente.py
import customtkinter as ctk
from tkinter import messagebox
from backend_oop import InventarioManager, BebidaManager, JSONStorage

class GerenteUI:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario_manager = InventarioManager()
        self.bebida_manager = BebidaManager()
        self.bebidas = self.bebida_manager.cargar_bebidas()

        self.ventana = ctk.CTkToplevel()
        self.ventana.title("Entorno del Gerente")
        self.ventana.geometry("600x600")

        self.crear_interfaz()

    def mostrar(self):
        self.ventana.deiconify()

    def crear_interfaz(self):
        pestañas = ctk.CTkTabview(self.ventana)
        pestañas.pack(expand=True, fill="both")

        # --- TAB Inventario ---
        tab_inventario = pestañas.add("Inventario")

        ctk.CTkLabel(tab_inventario, text="Gestión de Inventario", font=("Arial", 16)).pack(pady=10)

        self.entry_ingrediente = ctk.CTkEntry(tab_inventario, width=300, placeholder_text="Ingrediente")
        self.entry_cantidad = ctk.CTkEntry(tab_inventario, width=300, placeholder_text="Cantidad")
        self.entry_ingrediente.pack(pady=5)
        self.entry_cantidad.pack(pady=5)

        ctk.CTkButton(tab_inventario, text="Agregar", command=self.agregar_ingrediente).pack(pady=5)
        ctk.CTkButton(tab_inventario, text="Eliminar", command=self.eliminar_ingrediente).pack(pady=5)

        self.lista_inventario = ctk.CTkTextbox(tab_inventario, width=400, height=150)
        self.lista_inventario.pack(pady=10)

        self.actualizar_lista_inventario()

        # --- TAB Precios ---
        tab_precios = pestañas.add("Asignar Precios")

        self.seleccion_bebida = ctk.StringVar()
        self.lista_nombres = [b["nombre"] for b in self.bebidas]
        self.combo_bebidas = ctk.CTkOptionMenu(tab_precios, values=self.lista_nombres, variable=self.seleccion_bebida, command=self.llenar_campos_precio)
        self.combo_bebidas.pack(pady=10)

        self.entry_chico = ctk.CTkEntry(tab_precios, placeholder_text="Precio chico")
        self.entry_mediano = ctk.CTkEntry(tab_precios, placeholder_text="Precio mediano")
        self.entry_grande = ctk.CTkEntry(tab_precios, placeholder_text="Precio grande")
        self.entry_extra = ctk.CTkEntry(tab_precios, placeholder_text="Precio ingrediente extra")
        self.entry_postre = ctk.CTkEntry(tab_precios, placeholder_text="Precio postre")

        ctk.CTkButton(tab_precios, text="Guardar Precio", command=self.guardar_precios).pack(pady=10)

        if self.lista_nombres:
            self.seleccion_bebida.set(self.lista_nombres[0])
            self.llenar_campos_precio()

        # --- Botón cerrar sesión ---
        ctk.CTkButton(self.ventana, text="Cerrar Sesión", command=self.ventana.destroy).pack(pady=10)

    def actualizar_lista_inventario(self):
        self.lista_inventario.delete("1.0", "end")
        inventario = self.inventario_manager.cargar()
        for item in inventario:
            self.lista_inventario.insert("end", f"{item['ingrediente']}: {item['cantidad']}\n")

    def agregar_ingrediente(self):
        nombre = self.entry_ingrediente.get()
        cantidad = self.entry_cantidad.get()
        if not nombre or not cantidad:
            messagebox.showerror("Error", "Debe llenar ambos campos")
            return
        self.inventario_manager.agregar_ingrediente(nombre, cantidad)
        self.actualizar_lista_inventario()

    def eliminar_ingrediente(self):
        nombre = self.entry_ingrediente.get()
        if not nombre:
            messagebox.showerror("Error", "Debe ingresar el ingrediente a eliminar")
            return
        self.inventario_manager.eliminar_ingrediente(nombre)
        self.actualizar_lista_inventario()

    def llenar_campos_precio(self, *args):
        self.ocultar_campos_precio()

        nombre = self.seleccion_bebida.get()
        bebida = next((b for b in self.bebidas if b["nombre"] == nombre), None)
        if not bebida:
            return

        precios = bebida.get("precios", {})

        if bebida["categoria"] in ["Bebida fria", "Bebida caliente"]:
            self.entry_chico.pack(pady=3)
            self.entry_mediano.pack(pady=3)
            self.entry_grande.pack(pady=3)
            self.entry_extra.pack(pady=3)

            self.entry_chico.delete(0, "end")
            self.entry_chico.insert(0, precios.get("chico", ""))
            self.entry_mediano.delete(0, "end")
            self.entry_mediano.insert(0, precios.get("mediano", ""))
            self.entry_grande.delete(0, "end")
            self.entry_grande.insert(0, precios.get("grande", ""))
            self.entry_extra.delete(0, "end")
            self.entry_extra.insert(0, precios.get("extra", ""))
        else:
            self.entry_postre.pack(pady=3)
            self.entry_extra.pack(pady=3)

            self.entry_postre.delete(0, "end")
            self.entry_postre.insert(0, precios.get("precio", ""))
            self.entry_extra.delete(0, "end")
            self.entry_extra.insert(0, precios.get("extra", ""))

    def ocultar_campos_precio(self):
        for entry in [self.entry_chico, self.entry_mediano, self.entry_grande, self.entry_extra, self.entry_postre]:
            entry.pack_forget()

    def guardar_precios(self):
        nombre = self.seleccion_bebida.get()
        for bebida in self.bebidas:
            if bebida["nombre"] == nombre:
                if bebida["categoria"] in ["Bebida fria", "Bebida caliente"]:
                    bebida["precios"] = {
                        "chico": self.entry_chico.get(),
                        "mediano": self.entry_mediano.get(),
                        "grande": self.entry_grande.get(),
                        "extra": self.entry_extra.get()
                    }
                else:
                    bebida["precios"] = {
                        "precio": self.entry_postre.get(),
                        "extra": self.entry_extra.get()
                    }
                break

        JSONStorage.guardar("bebidas.json", self.bebidas)
        messagebox.showinfo("Éxito", "Precios actualizados correctamente")
