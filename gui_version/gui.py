import random
from math import ceil
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

import os 

from tkinter import Tk, Label, Button, StringVar

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class GUI:
	def __init__(self, master):
		self.THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
		self.master = master
		master.title("Design Code & Robots Contest alpha v 0.01")
		master.geometry('1280x720')
		self.memebers_list = self.read_file("input.txt")

		self.label = Label(master, text="Groups Count:")
		self.label.pack()

		self.combo = Combobox(master, width=50, height=10, state="readonly")
		self.combo['values']= (1, 2, 3, 4, 5, 6, 7)
		self.combo.current(3)
		self.combo.pack()

		self.text_window = scrolledtext.ScrolledText(master, width=100, height=30, borderwidth=3, relief=SUNKEN)
		self.text_window.insert(INSERT,"\n".join(self.memebers_list))
		self.text_window.pack()

		self.greet_button = Button(master, text="START", command=self.greet, width=20, height=3, font=('Helvetica', '20'))
		self.greet_button.pack()

	def greet(self):
		random.shuffle(self.memebers_list)
		groups_list = self.make_groups(self.memebers_list, int(self.combo.get()))
		msg = ''
		with open(os.path.join(self.THIS_FOLDER, "output.txt"), "w", encoding="utf-8") as out:
			for i, group in enumerate(groups_list):
				line = f"\nГРУППА {alphabet[i]}:\n"
				msg += line
				out.write(line)
				for j, memeber in enumerate(group):
					line = f"    {j+1}) {memeber}\n"
					msg += line
					out.write(line)
		self.text_window.delete(1.0, END)
		self.text_window.insert(INSERT, msg)

	def read_file(self, file):
		lines = []
		for line in open(os.path.join(self.THIS_FOLDER, "input.txt"), "r"):
			lines.append(line.strip())
		return lines

	def make_groups(self, memebers, groups_count):
		group_len = ceil(len(memebers)/groups_count)
		return [memebers[group_len*i:group_len*(i+1)] for i in range(groups_count)]

root = Tk()
my_gui = GUI(root)
root.mainloop()
