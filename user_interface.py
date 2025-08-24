from ttkbootstrap import Window, Toplevel
from ttkbootstrap import ttk
from ttkbootstrap.dialogs import Messagebox
import tkinter as tk

import logic
import database
import globals

userinformation = None
iteration = 0

def interface(password="unknown"):
    global length_input

    globals.active_windows += 1
    if globals.active_windows > 1:
        return

    root = globals.root
    root.title("Secure Password Generator")
    root.geometry("450x350")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")

    # Überschrift
    title = ttk.Label(root, text="Passwort Generator", font=("Helvetica", 18, "bold"))
    title.pack(pady=(20, 10))

    # Eingabe
    length_label = ttk.Label(root, text="Wie lang soll das Passwort sein?", font=("Helvetica", 12))
    length_label.pack(pady=(10, 5))
    length_input = ttk.Entry(root, width=20)
    length_input.pack(pady=(0, 15))

    # Buttons Frame
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    submit_button = ttk.Button(button_frame, text="Generieren", width=15, command=lambda: logic.entry_get("UI", length_input))
    submit_button.grid(row=0, column=0, padx=5, pady=5)

    db_button = ttk.Button(button_frame, text="Datenbank anzeigen", width=15, command=lambda: on_watch_db_clicked(globals.root))
    db_button.grid(row=0, column=1, padx=5, pady=5)

    root.bind("<Return>", lambda event: logic.entry_get("UI", length_input))

    root.mainloop()


def on_watch_db_clicked(window):
    #global iteration
    #iteration += 1
    #print(iteration)
    #if iteration > 1:
     #   return

    if len(globals.rows) > 7:
        print(globals.rows)
        window.geometry("700x700")

    labels_frame = ttk.Frame(window)
    labels_frame.pack(pady=10)

    labels = []
    for item in globals.dataset_with_decrypted_password:
        lbl = ttk.Label(labels_frame, text=item, font=("Helvetica", 10))
        lbl.pack(pady=2)
        labels.append(lbl)

    disable_db_display = ttk.Button(window, text="Verbergen", command=lambda: hide(labels, labels_frame, disable_db_display, window))
    disable_db_display.pack(pady=10)


def hide(labels, base_label, button, window):
    global iteration
    for lbl in labels:
        lbl.destroy()
    base_label.destroy()
    button.destroy()
    iteration = 0
    window.geometry("450x350")


def close_window(password):
    globals.closewindow = 1
    globals.root.withdraw()
    build_finishwindow(password)


def build_finishwindow(password):
    globals.active_windows += 1

    win = Toplevel()
    win.title("Fertig")
    win.geometry("400x300")
    win.resizable(False, False)
    win.grab_set()
    win.configure(bg="#f0f0f0")

    ttk.Label(win, text=f"Dein Passwort ist:\n{password}", font=("Helvetica", 12), justify="center").pack(pady=40)

    button_frame = ttk.Frame(win)
    button_frame.pack(pady=20)

    home_btn = ttk.Button(button_frame, text="Home", width=12, command=lambda: help_func(win, globals.root))
    home_btn.grid(row=0, column=0, padx=5)

    copy_btn = ttk.Button(button_frame, text="Kopieren", width=12, command=lambda: win.clipboard_append(password))
    copy_btn.grid(row=0, column=1, padx=5)

    save_btn = ttk.Button(button_frame, text="Speichern", width=12, command=lambda: switch_to_database_window(win, password))
    save_btn.grid(row=1, column=0, columnspan=2, pady=10)


def switch_to_database_window(window, password):
    window.withdraw()
    build_password_database_and_save_form(password)


def build_password_database_and_save_form(password):
    win = Toplevel()
    win.title("Passwort speichern")
    win.geometry("400x350")
    win.resizable(False, False)
    win.grab_set()
    win.configure(bg="#f0f0f0")

    ttk.Label(win, text="Passwort speichern", font=("Helvetica", 16, "bold")).pack(pady=15)

    # Form Frame
    form_frame = ttk.Frame(win)
    form_frame.pack(pady=10, padx=20, fill="x")

    # Passwort
    ttk.Label(form_frame, text="Passwort:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
    ttk.Label(form_frame, text=password).grid(row=0, column=1, sticky="w", pady=5)

    # Username
    ttk.Label(form_frame, text="Benutzername:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
    username_entry = ttk.Entry(form_frame)
    username_entry.grid(row=1, column=1, sticky="ew", pady=5)

    # URL
    ttk.Label(form_frame, text="URL:", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
    url_entry = ttk.Entry(form_frame)
    url_entry.grid(row=2, column=1, sticky="ew", pady=5)

    # Service
    ttk.Label(form_frame, text="Service:", font=("Helvetica", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
    service_entry = ttk.Entry(form_frame)
    service_entry.grid(row=3, column=1, sticky="ew", pady=5)

    # Buttons
    button_frame = ttk.Frame(win)
    button_frame.pack(pady=15)

    submit_btn = ttk.Button(button_frame, text="Speichern", width=12,
                            command=lambda: logic.entry_get("DB", username_entry, service_entry, url_entry, password))
    submit_btn.grid(row=0, column=0, padx=5)

    back_btn = ttk.Button(button_frame, text="Zurück", width=12, command=lambda: help_func(win, globals.root))
    back_btn.grid(row=0, column=1, padx=5)


def user_error():
    Messagebox.show_error(title="Error", message="Du darfst nur Zahlen eingeben (5-30).")


def catch_api_problem(page):
    ttk.Label(page, text="Bitte überprüfe, ob die Passwort-Datei beschädigt ist.").pack(pady=10)


def help_func(window1, window2):
    window1.destroy()
    window2.deiconify()
