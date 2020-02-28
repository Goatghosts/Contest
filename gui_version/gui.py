import random
from math import ceil
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

from tkinter import Tk, Label, Button, StringVar

class MyFirstGUI:
	def __init__(self, master):
		self.master = master
		master.title("Design Code & Robots Contest v 0.0000000001")
		master.geometry('1280x720')
		self.memebers_list = self.read_file("input.txt")

		self.label = Label(master, text="Groups Count:")
		self.label.pack()

		self.combo = Combobox(master, width=50, height=10)
		self.combo['values']= (1, 2, 3, 4, 5, 6, 7)
		self.combo.current(3)
		self.combo.pack()

		self.text_window = scrolledtext.ScrolledText(master, width=100, height=30, borderwidth=3, relief=SUNKEN)
		self.text_window.insert(INSERT,"\n".join(self.memebers_list))
		self.text_window.pack()

		self.greet_button = Button(master, text="Start!", command=self.greet, width=20, height=3, font=('Helvetica', '20'))
		self.greet_button.pack()

	def greet(self):
		random.shuffle(self.memebers_list)
		groups_list = self.make_groups(self.memebers_list, int(self.combo.get()))
		msg = ''
		with open("output.txt", "w", encoding="utf-8") as out:
			for i, group in enumerate(groups_list):
				line = f"\nГРУППА {i+1}:\n"
				msg += line
				out.write(line)
				for memeber in group:
					line = f"-- {memeber}\n"
					msg += line
					out.write(line)
		self.text_window.delete(1.0, END)
		self.text_window.insert(INSERT, msg)

	def read_file(self, file):
		lines = []
		for line in open(file, "r"):
			lines.append(line.strip())
		return lines

	def make_groups(self, memebers, groups_count):
		group_len = ceil(len(memebers)/groups_count)
		return [memebers[group_len*i:group_len*(i+1)] for i in range(groups_count)]

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
