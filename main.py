"""
Main entrance of app and UI logic

*********************************************************
CREATED AND MAINTAINED BY ANDRES QUIROZ
*********************************************************

"""

from cgitb import text
from sqlite3 import Row
import tkinter as tk
from app_logic import generate_truth_table

current_option_menu = None

def truth_table_generator_widgets():
    """
    Function that packs all the widgets of the truth table generator
    section of the app
    """
    global main_area, current_option_menu

    if current_option_menu == "truth_table": # we are already in the option
        return

    table_container = tk.Frame(main_area, width=500, height=500)
   
    def generate_table_tkinter():
        """"
        Creates all entries
        """
        table = generate_truth_table(entry_text.get()) # matrix
        table_container.pack()

        # first pack the headers
        for i in range(0, len(table[0])):
            header = tk.Entry(table_container)
            header.insert(0, table[0][i])
            header.grid(row=0, column=i)
        
        # pack the content
        for j in range(1, len(table)):
            for i in range(0, len(table[j])):
                cell_content = tk.Entry(table_container)
                cell_content.insert(0, table[j][i])
                cell_content.grid(row=j, column=i)

    def clear_contents():
        """
        Limpia los contenidos del programa
        """
        table_container.pack_forget()
        main_entry.delete(0, tk.END)
        

    def change_text(text):
        main_entry.insert(0, text)


    current_option_menu = "truth_table"
    entry_text = tk.StringVar()
    main_entry = tk.Entry(main_area, textvariable=entry_text)
    main_entry.pack(pady=20)
    
    tk.Button(main_area, text="Generar", command=lambda:generate_table_tkinter()).pack(pady=5)
    tk.Button(main_area, text="Limpiar", command=lambda:clear_contents()).pack(pady=5)

    # operator buttons
    button_container = tk.Frame(main_area, width=500, height=500)
    button_container.pack()

    tk.Button(button_container, text="p", width=5, height=2, command=lambda:change_text("p")).grid(row=1, column=0)
    tk.Button(button_container, text="q", width=5, height=2, command=lambda:change_text("q")).grid(row=1, column=1)
    tk.Button(button_container, text="r", width=5, height=2, command=lambda:change_text("r")).grid(row=1, column=2)
    tk.Button(button_container, text="s", width=5, height=2, command=lambda:change_text("s")).grid(row=1, column=3)
    tk.Button(button_container, text="t", width=5, height=2, command=lambda:change_text("t")).grid(row=1, column=4)

    tk.Button(button_container, text="u", width=5, height=2, command=lambda:change_text("u")).grid(row=2, column=0)
    tk.Button(button_container, text="w", width=5, height=2, command=lambda:change_text("w")).grid(row=2, column=1)
    tk.Button(button_container, text="x", width=5, height=2, command=lambda:change_text("x")).grid(row=2, column=2)
    tk.Button(button_container, text="y", width=5, height=2, command=lambda:change_text("y")).grid(row=2, column=3)
    tk.Button(button_container, text="z", width=5, height=2, command=lambda:change_text("z")).grid(row=2, column=4)

    tk.Button(button_container, text="^", width=5, height=2, command=lambda:change_text("^")).grid(row=3, column=0)
    tk.Button(button_container, text="v", width=5, height=2, command=lambda:change_text("v")).grid(row=3, column=1)
    tk.Button(button_container, text="~", width=5, height=2, command=lambda:change_text("~")).grid(row=3, column=2)
    tk.Button(button_container, text="->", width=5, height=2, command=lambda:change_text("->")).grid(row=3, column=3)
    tk.Button(button_container, text="<->", width=5, height=2, command=lambda:change_text("<->")).grid(row=3, column=4)



def main():
    truth_table_generator_widgets()

root = tk.Tk()
# defining layouts ----

# header
headbar = tk.Frame(root, bg='#CCC', height=40, borderwidth=2)
headbar.pack(expand=False, fill='both', side='top', anchor='nw')

# sidebar
sidebar = tk.Frame(root, width=200, bg='green', height=500, relief='sunken', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# main content area
main_area = tk.Frame(root, width=500, height=500)
main_area.pack(expand=True, fill='both', side='right', padx=10, pady=10)

# defining widgets -----

# main title
tk.Label(headbar, text="Tablify", bg="#CCC", font=('Arial', 15)).grid(row=0,column=0)

# sidebar buttons
tk.Button(sidebar, command=truth_table_generator_widgets, text="Generador tablas de verdad", bg="green", relief="flat").grid(row=0, column=0)

main()

root.mainloop()




