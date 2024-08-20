from tkinter import Button, Entry, Listbox

def create_add_task_button(root):
    return Button(root, text="Añadir Tarea")

def create_delete_task_button(root):
    return Button(root, text="Eliminar Tarea")

def create_task_entry(root):
    return Entry(root)

def create_task_list(root):
    return Listbox(root, selectmode='multiple')
