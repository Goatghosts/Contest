import random
from math import ceil
import os

GROUPS = 5
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def make_groups(memebers, groups_count):
	group_len = ceil(len(memebers)/groups_count)
	return [memebers[group_len*i:group_len*(i+1)] for i in range(groups_count)]

def read_file(file):
	lines = []
	for line in open(os.path.join(THIS_FOLDER, file), "r"):
		lines.append(line.strip())
	return lines

memebers_list = read_file("input.txt")
random.shuffle(memebers_list)
groups_list = make_groups(memebers_list, GROUPS)

with open(os.path.join(THIS_FOLDER, "output.txt"), "w", encoding="utf-8") as out:
	for i, group in enumerate(groups_list):

		out.write(f"\nГРУППА {i+1}:\n")
		for memeber in group:
			out.write(f"-- {memeber}\n")
