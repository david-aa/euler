import sys

if len(sys.argv) != 2:
	print "Usage: 028.py <SIZE>"
	sys.exit()

table = []
size = int(sys.argv[1])
if size % 2 == 0:
	print "Only odd numbers"
	sys.exit()

for _ in range(0, size):
	row = []
	for _ in range(0, size):
		row.append(0)
	table.append(row)

directions = ((0,1), (1,0),(0,-1),(-1,0))

def get_next_direction(current): 
	i = directions.index(current)
	if i == len(directions) - 1:
		i = 0
	else:
		i += 1
	return directions[i]

max_num = size**2
x = size/2
y = size/2
diagonal_sum = 0
current_direction = (-1,0)
for a in range(1, max_num+1):
	if x == y or x + y == size - 1:
		diagonal_sum += a
	table[x][y] = a
	new_direction = get_next_direction(current_direction)
	x1 = x + new_direction[0]
	y1 = y + new_direction[1]
	if table[x1][y1] == 0:
		x, y = x1, y1
		current_direction = new_direction
	else:
		x, y = x + current_direction[0], y + current_direction[1]

#for row in table:
#	print row
print "diagonal_sum", diagonal_sum