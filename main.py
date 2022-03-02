#______IMPORT________#
import tkinter as tk




#______DEFINE_______#



#______FUNCTION_______#









#________MAIN_________#

window = tk.Tk()
window.geometry("600x350")
window.config(bg="#ed9c40")
window.resizable(width=False, height=False)
window.title("Number to Dollars converter")

#_______LABEL________#
lb_title = tk.Label(window, text="Number to dollars converter", font=("Arial", 20), fg="white", bg="#ed9c40")

lb_input = tk.Label(window, text="Type in numbers here", font=("Arial", 10), fg="grey", bg="white")

lb_output = tk.Label(window, text="", font=("Arial", 10), fg="grey", bg="white")

#_______PLACING________#

lb_title.place(x=60, y=20)