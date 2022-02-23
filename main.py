"""
Main entrance of app and UI logic
"""

from cgitb import text
import tkinter as tk

current_option_menu = None

def truth_table_generator_widgets():
    """
    Function that packs all the widgets of the truth table generator
    section of the app
    """
    global main_area, current_option_menu

    if current_option_menu == "truth_table": # we are already in the option
        return

    current_option_menu = "truth_table"
    main_entry = tk.Entry(main_area)
    main_entry.pack(pady=20)

    # operator buttons
    button_container = tk.Frame(main_area, width=500, height=500)
    button_container.pack()

    tk.Button(button_container, text="p", width=5, height=2).grid(row=1, column=0)
    tk.Button(button_container, text="q", width=5, height=2).grid(row=1, column=1)
    tk.Button(button_container, text="r", width=5, height=2).grid(row=1, column=2)
    tk.Button(button_container, text="s", width=5, height=2).grid(row=1, column=3)
    tk.Button(button_container, text="t", width=5, height=2).grid(row=1, column=4)

    tk.Button(button_container, text="^", width=5, height=2).grid(row=2, column=0)
    tk.Button(button_container, text="v", width=5, height=2).grid(row=2, column=1)
    tk.Button(button_container, text="~", width=5, height=2).grid(row=2, column=2)
    tk.Button(button_container, text="->", width=5, height=2).grid(row=2, column=3)
    tk.Button(button_container, text="<->", width=5, height=2).grid(row=2, column=4)
    

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




