from components import create_add_task_button, create_delete_task_button, create_task_entry, create_task_list
from events import setup_events
from styles import apply_button_styles, apply_entry_styles, apply_listbox_styles

def setup_layout(root):
    # Crear componentes
    task_entry = create_task_entry(root)
    add_button = create_add_task_button(root)
    delete_button = create_delete_task_button(root)
    task_list = create_task_list(root)
    
    # Aplicar estilos
    apply_entry_styles(task_entry)
    apply_button_styles(add_button)
    apply_button_styles(delete_button)
    apply_listbox_styles(task_list)
    
    # Posicionar los componentes usando grid
    task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    add_button.grid(row=0, column=1, padx=10, pady=10)
    delete_button.grid(row=0, column=2, padx=10, pady=10)
    task_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    
    # Configurar expandibilidad
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    # Configurar eventos
    setup_events(root, add_button, delete_button, task_entry, task_list)
