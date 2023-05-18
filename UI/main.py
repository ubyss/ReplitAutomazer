import tkinter as tk
from tkinter import filedialog
import os

def run_script(script_name):
    os.system(f"python {script_name}")

def open_file():
     run_script('publicacao/abrirNavegador.py')

def individual_file():
    run_script('publicacao\publicarIndividual.py')

def group_file():
    run_script('publicacao\publicarGrupo.py')


# Cria a janela principal
root = tk.Tk()
root.title("Monitoria")


root.geometry("400x300")

open_navigator = tk.Button(root, text="Abrir navegador", command=open_file)
open_navigator.pack(pady=20)

publish_individual = tk.Button(root, text="Publicar Individual", command=individual_file)
publish_individual.pack(pady=20)

publish_group = tk.Button(root, text="Publicar Grupo", command=group_file)
publish_group.pack(pady=20)

# Inicia o loop principal da interface
root.mainloop()
