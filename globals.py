from collections import namedtuple
import tkinter as tk

userinformation = namedtuple("Person", ["hash", "service", "url", "username", "Datum"])

active_windows = 0

close_window = 0

rows = None


decrypt_passwords = []

select_results_complete = []

dataset_with_decrypted_password = []


count_regenerating = 0

root = tk.Tk()
