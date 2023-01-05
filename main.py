from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Checkbutton
from tkinter import IntVar
from secrets import choice
from tkinter import Entry
from tkinter import ttk

# C:/NeedFolder/code/python programs for pc/Generater password GUI
root = Tk()

root.title("Генератор паролей")
root.resizable(False, False)

def password_generate():
	lenght = int(c.get())
	#print(f"длина : {lenght}")
	upper = c1.get()
	lower = c2.get()
	digit = c3.get()
	symbol = c4.get()
	
	dick = {0 : (upper, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 1 : (lower, "abcdefghijklmnopqrstuvwxyz"),
			2 : (digit, "0123456789"), 3 : (symbol, "!#$%&*+-=?@^_")}
	
	ally = ''

	for value in dick.values():
		if value[0] > 0:
			ally += value[1]

	pasword = ''.join(choice(ally) for i in range(lenght))

	password.set(pasword)

def ChangePasswordLenghtLabelText(scale_val):
	global pass_lenght
	a = scale_val
	a = float(a)
	password_lenght_label["text"] = round(a)

def quit():
	#password = password_generate()
	#print(password)
	root.destroy()

c = IntVar(value=4)
c1 = IntVar(value=1)
c2 = IntVar(value=2)
c3 = IntVar(value=3)
c4 = IntVar()

textmas = ["строчные буквы           ", "пропистные буквы      ", "цифры		         ", "символы	         "]
pass_lenght = 4

password = IntVar()

entry = Entry(root, width=33, bd=2, textvariable=password)
label = Label(root, text="Укажите условия создания пароля")

password_button = Button(root, text="generate password", padx=5, pady=5, command=password_generate)
exit_button = Button(root, text="QUIT", command=quit, pady=5)

password_lenght_label = Label(root, width=2, text=pass_lenght)
password_lenght = ttk.Scale(root, orient="horizontal", from_=4, to=32, value=4, variable=c, command=ChangePasswordLenghtLabelText)

upper_words = Checkbutton(root, text=textmas[0], variable=c1, onvalue=1, offvalue=0)
lower_words = Checkbutton(root, text=textmas[1], variable=c2, onvalue=2, offvalue=0)
numbers = Checkbutton(root, text=textmas[2], variable=c3, onvalue=3, offvalue=0)
symbols = Checkbutton(root, text=textmas[3], variable=c4, onvalue=4, offvalue=0)

label.grid(row=0, column=1)
entry.grid(row=1, column=1)

password_button.grid(row=2, column=1)
password_lenght.grid(row=3, column=1)
password_lenght_label.grid(row=4, column=1)

upper_words.grid(row=5, column=1)
lower_words.grid(row=6, column=1)
numbers.grid(row=7, column=1)
symbols.grid(row=8, column=1)

exit_button.grid(row=9, column=1)

root.mainloop()