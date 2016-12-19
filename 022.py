#!/usr/bin/env python

def get_value(name):
	s = 0
	for c in name:
		s += (ord(c) - ord('A') + 1)
	return s

f = open('p022_names.txt', 'r')
txt = f.read().strip().replace('"', '')
names = txt.split(',')
names.sort()
cont = 1
total = 0
for name in names:
	total += cont * get_value(name)
	cont += 1

print total