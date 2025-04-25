
# ☕ Cafetería App

Aplicación de escritorio para la gestión de una cafetería, desarrollada con Python y CustomTkinter, siguiendo el paradigma de programación orientada a objetos (OOP).

---

## 📂 Estructura del Proyecto

```
cafeteria_app/
├── backend/
│   └── backend_oop.py
├── frontend/
│   ├── main.py
│   ├── login_ui.py
│   ├── ui_gerente.py
│   ├── ui_barista.py
│   └── ui_cliente.py
├── data/
│   ├── bebidas.json
│   ├── inventario.json
│   ├── puntos.json
│   ├── usuarios.json
│   ├── empleados.json
│   └── historial_pedidos.json
```

---

## 🚀 Requisitos

- Python 3.8+
- `customtkinter`
- `tkinter` (viene incluido en Python)

Instalación de dependencias:

```bash
pip install customtkinter
```

---

## ▶️ Cómo Ejecutar

Desde el directorio `frontend/` ejecutar:

```bash
python main.py
```

---

## 👤 Roles Disponibles

- **Cliente:** Puede ver productos, personalizar bebidas, comprar y acumular puntos.
- **Empleado - Barista:** Puede registrar/modificar/eliminar bebidas y postres.
- **Empleado - Gerente:** Gestiona el inventario y precios de productos.

---

## 🗂 Archivos JSON

Se almacenan en `data/`:

- `usuarios.json`, `empleados.json`: Registro de cuentas.
- `bebidas.json`: Lista de productos disponibles.
- `inventario.json`: Ingredientes y cantidades.
- `puntos.json`: Sistema de recompensas.
- `historial_pedidos.json`: Registro de compras.

---

## ✨ Créditos

Desarrollado como sistema completo de gestión de una cafetería, modular y extensible.
