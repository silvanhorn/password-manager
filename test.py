import datetime
import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)

entry_get = entry.get()
entry.pack()

root.mainloop()

print(datetime.datetime.now().strftime("%Y-%m-%d"))
