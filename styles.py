def apply_styles(widget):
    # Define estilos comunes para todos los widgets
    widget.config(
        bg='#282c34',    # Fondo oscuro
        fg='#ffffff',    # Texto blanco
        font=('Arial', 12)
    )

def apply_button_styles(button):
    # Estilos específicos para botones
    button.config(
        bg='#61afef',   # Fondo azul claro
        fg='#282c34',   # Texto oscuro
        activebackground='#528bb7',  # Fondo al hacer clic
        activeforeground='#ffffff',  # Texto al hacer clic
        font=('Arial', 12, 'bold')
    )

def apply_entry_styles(entry):
    # Estilos específicos para campos de entrada
    entry.config(
        bg='#abb2bf',   # Fondo gris claro
        fg='#282c34',   # Texto oscuro
        font=('Arial', 12)
    )

def apply_listbox_styles(listbox):
    # Estilos específicos para la lista de tareas
    listbox.config(
        bg='#3e4451',   # Fondo gris oscuro
        fg='#ffffff',   # Texto blanco
        selectbackground='#61afef',  # Fondo de selección
        selectforeground='#282c34',  # Texto de selección
        font=('Arial', 12)
    )
