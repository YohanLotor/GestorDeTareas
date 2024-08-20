from tkinter import Tk
from layouts import setup_layout
from events import setup_events

def main():
    root = Tk()
    root.title("Gestor de Tareas")
    setup_layout(root)
    root.mainloop()

if __name__ == "__main__":
    main()
