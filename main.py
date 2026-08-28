import os
import tkinter as tk
from tkinter import filedialog, messagebox


def analizar_log(ruta):
    resumen = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    try:
        archivo = open(ruta, "r")
        for linea in archivo:
            if "[INFO]" in linea:
                resumen["INFO"] += 1
            elif "[WARNING]" in linea:
                resumen["WARNING"] += 1
            elif "[ERROR]" in linea:
                resumen["ERROR"] += 1
        archivo.close()
        return resumen
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
        return None


def seleccionar_archivo():
    ruta = filedialog.askopenfilename(
        title="Seleccionar log",
        filetypes=(("Archivos LOG", "*.log"), ("Archivos TXT", "*.txt")),
    )

    if ruta:
        nombre_archivo = os.path.basename(ruta)
        lbl_estado.config(
            text=f"Archivo cargado: {nombre_archivo}", fg="#111827"
        )

        datos = analizar_log(ruta)

        if datos:
            val_info.config(text=str(datos["INFO"]))
            val_warning.config(text=str(datos["WARNING"]))
            val_error.config(text=str(datos["ERROR"]))


# --- CONFIGURACIÓN DE VENTANA ---
ventana = tk.Tk()
ventana.title("Log Analyzer")
ventana.geometry("500x550")
ventana.minsize(380, 480)  # Tamaño mínimo para que no se deforme
ventana.config(bg="#f4f6f8")

# Permitir que el contenido principal crezca vertical y horizontalmente
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)


# --- CABECERA AZUL OSCURO (#23394d) ---
frame_header = tk.Frame(ventana, bg="#23394d", padx=25, pady=20)
frame_header.grid(row=0, column=0, sticky="ew")

# Configurar expansión en la cabecera
frame_header.columnconfigure(0, weight=1)


lbl_titulo_head = tk.Label(
    frame_header,
    text="Log Analyzer",
    fg="white",
    bg="#23394d",
    font=("Segoe UI", 18, "bold"),
    anchor="w",
)
lbl_titulo_head.grid(row=1, column=0, sticky="ew", pady=(5, 0))



# --- SECCIÓN DASHBOARD ---
frame_cuerpo = tk.Frame(ventana, bg="#f4f6f8", padx=25, pady=15)
frame_cuerpo.grid(row=1, column=0, sticky="nsew")

# Configurar expansión en el cuerpo
frame_cuerpo.columnconfigure(0, weight=1)
frame_cuerpo.rowconfigure(2, weight=1)

lbl_dash = tk.Label(
    frame_cuerpo,
    text="Dashboard",
    fg="#111827",
    bg="#f4f6f8",
    font=("Segoe UI", 20, "bold"),
    anchor="w",
)
lbl_dash.grid(row=0, column=0, sticky="ew")

lbl_bienvenida = tk.Label(
    frame_cuerpo,
    text="Bienvenido, Técnico",
    fg="#4b5563",
    bg="#f4f6f8",
    font=("Segoe UI", 11),
    anchor="w",
)
lbl_bienvenida.grid(row=1, column=0, sticky="ew", pady=(0, 15))


# --- TARJETA BLANCA RESPONSIVE ---
card = tk.Frame(
    frame_cuerpo,
    bg="white",
    highlightbackground="#e5e7eb",
    highlightthickness=1,
    padx=20,
    pady=20,
)
card.grid(row=2, column=0, sticky="nsew")

card.columnconfigure(0, weight=1)

lbl_card_title = tk.Label(
    card,
    text="Resumen de logs",
    fg="#111827",
    bg="white",
    font=("Segoe UI", 12, "bold"),
    anchor="w",
)
lbl_card_title.grid(row=0, column=0, sticky="ew", pady=(0, 15))

# Sub-contenedor de métricas (Grilla de 3 columnas elásticas)
frame_metricas = tk.Frame(card, bg="white")
frame_metricas.grid(row=1, column=0, sticky="ew", pady=10)

frame_metricas.columnconfigure(0, weight=1)
frame_metricas.columnconfigure(1, weight=1)
frame_metricas.columnconfigure(2, weight=1)

# Columna INFO
m_info = tk.Frame(frame_metricas, bg="white")
m_info.grid(row=0, column=0, sticky="nsew")
tk.Label(
    m_info, text="INFO", fg="#2e7d32", bg="white", font=("Segoe UI", 9, "bold")
).pack()
val_info = tk.Label(
    m_info, text="-", fg="#111827", bg="white", font=("Segoe UI", 16, "bold")
)
val_info.pack()

# Columna WARNING
m_warn = tk.Frame(frame_metricas, bg="white")
m_warn.grid(row=0, column=1, sticky="nsew")
tk.Label(
    m_warn,
    text="WARNING",
    fg="#ed6c02",
    bg="white",
    font=("Segoe UI", 9, "bold"),
).pack()
val_warning = tk.Label(
    m_warn, text="-", fg="#111827", bg="white", font=("Segoe UI", 16, "bold")
)
val_warning.pack()

# Columna ERROR
m_err = tk.Frame(frame_metricas, bg="white")
m_err.grid(row=0, column=2, sticky="nsew")
tk.Label(
    m_err, text="ERROR", fg="#d32f2f", bg="white", font=("Segoe UI", 9, "bold")
).pack()
val_error = tk.Label(
    m_err, text="-", fg="#111827", bg="white", font=("Segoe UI", 16, "bold")
)
val_error.pack()

# Estado del archivo
lbl_estado = tk.Label(
    card,
    text="Ningún archivo seleccionado",
    fg="#6b7280",
    bg="white",
    font=("Segoe UI", 9, "italic"),
)
lbl_estado.grid(row=2, column=0, sticky="ew", pady=(15, 10))

# Botón Azul de Acción
btn_cargar = tk.Button(
    card,
    text="Seleccionar log",
    command=seleccionar_archivo,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=15,
    pady=8,
    cursor="hand2",
)
btn_cargar.grid(row=3, column=0, pady=(5, 0))

ventana.mainloop()