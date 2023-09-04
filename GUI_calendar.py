from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendar")
root.geometry("600x400")

cal = Calendar(root, year=2023, momth=9, day=4)
cal.pack(pady=50)

root.mainloop()
